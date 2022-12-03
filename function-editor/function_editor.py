from kubernetes import client, config

import yaml
import streamlit as st

st.set_page_config(layout="wide")
st.header("Easy-Faas")

api_client = None

DEFINED_NAMESPACE = "easy-faas"

setting_tab, editor_tab, log_tab = st.tabs(["k8s setting", "Function Editor", "Logs"])

with setting_tab:
    # Initialization(k8s connection)
    kubeconfig_login = st.empty()

    if "kubeconfig" not in st.session_state:
        kubeconfig_input = kubeconfig_login.text_area(
            label="kubeconfig :",
            placeholder="enter kubeconfig value",
        )

        if kubeconfig_input != "":
            st.session_state["kubeconfig"] = yaml.safe_load(kubeconfig_input)

            try:
                config.load_kube_config_from_dict(st.session_state["kubeconfig"])
                api_client = client.CoreV1Api()
                custom_client = client.CustomObjectsApi()
                kubeconfig_login.empty()
                st.warning("k8s connection success!")

                if api_client is not None:
                    # namespace / CRD / operator check

                    ## check namespace
                    is_namespace_exist = False
                    namespace_list = api_client.list_namespace().items
                    for ns in namespace_list:
                        if ns.metadata.name == DEFINED_NAMESPACE:
                            is_namespace_exist = True
                            break

                    ## check CRD
                    crd_list = custom_client.list_namespaced_custom_object

            except:
                st.error("k8s connection fail!")
