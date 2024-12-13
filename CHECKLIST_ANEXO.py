import streamlit as st
import tempfile
import os
import create_pdf
import suggestions
import sections
import requests
from requests.auth import HTTPBasicAuth


jira_url = st.secrets["jira_url"]
email = st.secrets["email"]
api_token = st.secrets["api_token"]

headers = {"Accept": "application/json"}
auth = HTTPBasicAuth(email, api_token)

st.title("Checklist de Verificação - Logistica")

# Personalizar título do relatório
custom_title = st.text_input("Modelo:", value="")
issue_key = st.text_input("Chave de EQP:", value="")

# Upload de imagens do produto
uploaded_images = st.file_uploader("Foto do produto (opcional)", accept_multiple_files=True, type=["png", "jpg", "jpeg"])

st.write("Selecione se atender ao item")
# Seções do checklist
sections_data = sections.sec()  # Carregar o checklist
# Sugestões de melhorias
suggestions_data = suggestions.sug()  # Carregar sugestões

responses = {}
failed_items_with_suggestions = {}

# Formulário para cada seção e item
for section, items in sections_data.items():
    #st.write(items)
    st.subheader(section)
    section_responses = {}

    for idx, item in enumerate(items):  # Adicionando um índice
        #st.write(item)
        status = st.checkbox(f"{item}", key=f"{section}_{idx}_{item}_status", value=False)
        comments = st.text_area(f"Comentários sobre:", key=f"{section}_{idx}_{item}_comments", value="")
        section_responses[item] = {"status": status, "comments": comments}

    responses[section] = section_responses



#                Buscar sugestões diretamente usando a chave do item
#                item_suggestions = suggestions_data.get(item, ["Sem sugestão disponível"])
#                failed_items_with_suggestions[item] = item_suggestions
#                #st.write(f"Sugestões para '{item}':", item_suggestions)

    responses[section] = section_responses


            # Adicionar itens não conformes às sugestões
#            if not status:
#                failed_items_with_suggestions[item] = suggestions_data.get(section, {}).get(item, ["Sem sugestão disponível"])
#                st.write(failed_items_with_suggestions)

    responses[section] = section_responses

# Novo campo de upload de imagens para falhas
failure_proof_images = st.file_uploader(
    "Prints comprovando falhas (opcional)", accept_multiple_files=True, type=["png", "jpg", "jpeg"]
)


def save_uploaded_images(uploaded_files):
    """Função para salvar arquivos enviados como temporários"""
    file_paths = []
    for uploaded_file in uploaded_files:
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=f"_{uploaded_file.name}")
        temp_file.write(uploaded_file.getbuffer())
        temp_file.close()
        file_paths.append(temp_file.name)
    return file_paths


if st.button("Gerar Relatório"):
    total_items = sum(len(items) for items in responses.values())
    passed_items = sum(
        details["status"] for items in responses.values() for details in items.values()
    )

    # Resultado de validação
    validation_result = (
        f"Total de itens verificados: {total_items}\n"
        f"Itens em conformidade: {passed_items}\n"
    )

    if passed_items == total_items:
        validation_result += "Status final: O dispositivo está em conformidade com todos os critérios."
    elif passed_items >= total_items * 0.8:
        validation_result += "Status final: O dispositivo está parcialmente em conformidade (80% ou mais)."
    else:
        validation_result += "Status final: O dispositivo NÃO está em conformidade com todos os critérios."

    # Salvar imagens separadas
    product_images = save_uploaded_images(uploaded_images) if uploaded_images else []
    failure_images = save_uploaded_images(failure_proof_images) if failure_proof_images else []

    # Gerar o PDF
    filename = create_pdf.main(
        responses,
        custom_title,
        product_images,
        failure_images,
        #validation_result,
        suggestions_data
    )

    # Salvar no estado da sessão
    st.session_state["filename"] = filename

    st.success(f"Relatório gerado com sucesso: {filename}")
    st.text(validation_result)

    # Botão de download
    with open(filename, "rb") as pdf_file:
        st.download_button(
            label="Baixar Relatório",
            data=pdf_file,
            file_name=filename,
            mime="application/pdf"
        )

    # Limpar arquivos temporários
    for image_path in product_images + failure_images:
        os.remove(image_path)


def anexar_arquivo_jira(jira_url, issue_key, email, api_token, file_path):
    """Função para anexar arquivos ao Jira"""
    upload_url = f"{jira_url}/rest/api/3/issue/{issue_key}/attachments"
    headers = {"X-Atlassian-Token": "no-check", "Accept": "application/json"}

    try:
        with open(file_path, "rb") as file:
            files = {"file": (file_path.split("/")[-1], file)}
            response = requests.post(
                upload_url,
                headers=headers,
                files=files,
                auth=HTTPBasicAuth(email, api_token)
            )

        if response.status_code == 200:
            return "Arquivo anexado com sucesso!"
        else:
            return f"Erro ao anexar arquivo: {response.status_code} - {response.text}"

    except FileNotFoundError:
        return "Erro: Arquivo não encontrado."
    except Exception as e:
        return f"Erro inesperado: {str(e)}"


# Botão de anexar ao Jira
if st.button("Anexar ao Jira"):
    if "filename" in st.session_state and st.session_state["filename"]:
        filename = st.session_state["filename"]
        mensagem = anexar_arquivo_jira(jira_url, issue_key, email, api_token, filename)
        if "sucesso" in mensagem.lower():
            st.success(mensagem)
        else:
            st.error(mensagem)
    else:
        st.warning("Nenhum relatório foi gerado para anexar.")
