import os

cred_filename = "app-hospede-firebase-adminsdk-fbsvc-60dd1f5f36.json"
# Caminho sempre na raiz do projeto
cred_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", cred_filename)

# --- GARANTE a criação do arquivo antes de qualquer coisa ---
json_env = os.environ.get("FIREBASE_CREDENTIAL_JSON")
if json_env:
    if not os.path.exists(cred_path):
        with open(cred_path, "w") as f:
            f.write(json_env)
else:
    print("ATENÇÃO: Variável de ambiente FIREBASE_CREDENTIAL_JSON não encontrada.")

import firebase_admin
from firebase_admin import credentials, firestore

if not firebase_admin._apps:
    cred = credentials.Certificate(cred_path)
    firebase_admin.initialize_app(cred)
db = firestore.client()

def atualizar_link_hospede(document_id, link):
    try:
        doc_ref = db.collection("hospedes").document(document_id)
        doc_ref.update({"link": link})
        return True
    except Exception as e:
        print("Erro ao atualizar Firebase:", e)
        return False
