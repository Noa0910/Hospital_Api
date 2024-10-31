import streamlit as st
import requests
from streamlit_option_menu import option_menu
from datetime import date
import pandas as pd

# Configurar la URL base de la API de FastAPI
BASE_URL = "http://localhost:8000/api"

# Barra de navegación
st.sidebar.title("Navegación")
with st.sidebar:
    selected = option_menu(
        "Insertar Datos",
        ["Pacientes", "Responsables", "Diagnósticos", "Hospitales", "Citas", "Cargar Excel"],
        icons=["person-plus", "people", "clipboard-plus", "building", "calendar", "file-earmark-excel"],
        menu_icon="cast",
        default_index=0
    )

# Formularios para cada tabla
if selected == "Pacientes":
    st.title("Registrar Paciente")
    with st.form(key="patient_form"):
        first_name = st.text_input("Nombre del Paciente")
        last_name = st.text_input("Apellido del Paciente")
        diagnosis_id = st.number_input("ID del Diagnóstico", min_value=1)
        hospital_id = st.number_input("ID del Hospital", min_value=1)
        date_of_birth = st.date_input("Fecha de Nacimiento")

        submit_button = st.form_submit_button(label="Registrar Paciente")

        if submit_button:
            patient_data = {
                "first_name": first_name,
                "last_name": last_name,
                "diagnosis_id": diagnosis_id,
                "hospital_id": hospital_id,
                "date_of_birth": str(date_of_birth)
            }
            try:
                response = requests.post(f"{BASE_URL}/patients/", json=patient_data)
                if response.status_code == 200:
                    st.success("Paciente registrado con éxito!")
                else:
                    st.error(f"Error al registrar el paciente: {response.text}")
            except requests.RequestException as e:
                st.error(f"Error de conexión: {str(e)}")

elif selected == "Responsables":
    st.title("Registrar Responsable")
    with st.form(key="responsible_form"):
        name = st.text_input("Nombre del Responsable")
        relationship = st.text_input("Relación con el Paciente")
        phone = st.text_input("Teléfono")
        email = st.text_input("Correo Electrónico")

        submit_button = st.form_submit_button(label="Registrar Responsable")

        if submit_button:
            responsible_data = {
                "name": name,
                "relationship": relationship,
                "phone": phone,
                "email": email
            }
            try:
                response = requests.post(f"{BASE_URL}/responsibles/", json=responsible_data)
                if response.status_code == 200:
                    st.success("Responsable registrado con éxito!")
                else:
                    st.error(f"Error al registrar el responsable: {response.text}")
            except requests.RequestException as e:
                st.error(f"Error de conexión: {str(e)}")

elif selected == "Diagnósticos":
    st.title("Registrar Diagnóstico")
    with st.form(key="diagnosis_form"):
        name = st.text_input("Nombre del Diagnóstico")

        submit_button = st.form_submit_button(label="Registrar Diagnóstico")

        if submit_button:
            diagnosis_data = {"name": name}
            try:
                response = requests.post(f"{BASE_URL}/diagnoses/", json=diagnosis_data)
                if response.status_code == 200:
                    st.success("Diagnóstico registrado con éxito!")
                else:
                    st.error(f"Error al registrar el diagnóstico: {response.text}")
            except requests.RequestException as e:
                st.error(f"Error de conexión: {str(e)}")

elif selected == "Hospitales":
    st.title("Registrar Hospital")
    with st.form(key="hospital_form"):
        name = st.text_input("Nombre del Hospital")
        address = st.text_input("Dirección")
        city = st.text_input("Ciudad")

        submit_button = st.form_submit_button(label="Registrar Hospital")

        if submit_button:
            hospital_data = {
                "name": name,
                "address": address,
                "city": city
            }
            try:
                response = requests.post(f"{BASE_URL}/hospitals/", json=hospital_data)
                if response.status_code == 200:
                    st.success("Hospital registrado con éxito!")
                else:
                    st.error(f"Error al registrar el hospital: {response.text}")
            except requests.RequestException as e:
                st.error(f"Error de conexión: {str(e)}")

elif selected == "Citas":
    st.title("Registrar Cita")
    with st.form(key="appointment_form"):
        patient_id = st.number_input("ID del Paciente", min_value=1)
        hospital_id = st.number_input("ID del Hospital", min_value=1)
        appointment_date = st.date_input("Fecha de la Cita")
        notes = st.text_area("Notas")

        submit_button = st.form_submit_button(label="Registrar Cita")

        if submit_button:
            appointment_data = {
                "patient_id": patient_id,
                "hospital_id": hospital_id,
                "appointment_date": str(appointment_date),
                "notes": notes
            }
            try:
                response = requests.post(f"{BASE_URL}/appointments/", json=appointment_data)
                if response.status_code == 200:
                    st.success("Cita registrada con éxito!")
                else:
                    st.error(f"Error al registrar la cita: {response.text}")
            except requests.RequestException as e:
                st.error(f"Error de conexión: {str(e)}")

elif selected == "Cargar Excel":
    st.title("Cargar Archivo Excel")
    uploaded_file = st.file_uploader("Elige un archivo Excel", type="xlsx")
    if uploaded_file is not None:
        df = pd.read_excel(uploaded_file)
        st.write(df)
        if st.button("Cargar Datos"):
            files = {"file": uploaded_file.getvalue()}
            response = requests.post(f"{BASE_URL}/upload-excel/", files=files)
            if response.status_code == 200:
                st.success("Datos cargados exitosamente!")
            else:
                st.error(f"Error al cargar los datos: {response.text}")