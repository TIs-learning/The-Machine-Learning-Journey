import streamlit as st
from PIL import Image
import requests
from io import BytesIO
import json
import base64
import time

# =========================================================
# CONFIG
# =========================================================
st.set_page_config(
    page_title="AI Image Generator",
    layout="wide"
)

# =========================================================
# API TOKEN
# =========================================================
TOKEN_AUTH = "YOUR_TOKEN"

# =========================================================
# HELPER FUNCTIONS
# =========================================================
def create_placeholder(width=400, height=400):
    """
    Membuat placeholder image sederhana
    """
    return Image.new("RGB", (width, height), (230, 230, 230))


def upload_image_to_api(image, filename):
    """
    Upload gambar ke API
    """

    try:
        buffered = BytesIO()

        image.save(buffered, format="PNG")

        img_base64 = base64.b64encode(
            buffered.getvalue()
        ).decode()

        payload = {
            "base64Data": f"data:image/png;base64,{img_base64}",
            "uploadPath": "images/base64",
            "fileName": filename
        }

        response = requests.post(
            "https://kieai.redpandaai.co/api/file-base64-upload",
            headers={
                "Authorization": f"Bearer {TOKEN_AUTH}",
                "Content-Type": "application/json"
            },
            json=payload
        )

        response.raise_for_status()

        result = response.json()

        if result.get("code") == 200:
            return True, result["data"]["downloadUrl"]

        return False, result.get("msg", "Upload gagal")

    except Exception as e:
        return False, str(e)


def process_ai(image_url, prompt):
    """
    Mengirim request AI generate image
    """

    try:
        payload = {
            "model": (
                "flux-2/pro-image-to-image"
                if image_url
                else "flux-2/pro-text-to-image"
            ),
            "input": {
                "prompt": prompt,
                "input_urls": [image_url] if image_url else []
            }
        }

        response = requests.post(
            "https://api.kie.ai/api/v1/jobs/createTask",
            headers={
                "Authorization": f"Bearer {TOKEN_AUTH}",
                "Content-Type": "application/json"
            },
            json=payload
        )

        response.raise_for_status()

        result = response.json()

        if result.get("code") == 200:
            return True, result["data"]["taskId"]

        return False, result.get("msg", "Gagal membuat task")

    except Exception as e:
        return False, str(e)


def get_result(task_id):
    """
    Mengambil hasil generate image
    """

    try:
        response = requests.get(
            f"https://api.kie.ai/api/v1/jobs/recordInfo?taskId={task_id}",
            headers={
                "Authorization": f"Bearer {TOKEN_AUTH}"
            }
        )

        response.raise_for_status()

        result = response.json()

        if result.get("code") == 200:
            return True, result["data"]

        return False, result

    except Exception as e:
        return False, str(e)


# =========================================================
# UI HEADER
# =========================================================
st.title("🧠 AI Image Generator")

st.write(
    "Upload gambar lalu masukkan prompt untuk menghasilkan gambar AI."
)

# =========================================================
# INPUT SECTION
# =========================================================
with st.container(border=True):

    st.subheader("Input")

    uploaded_file = st.file_uploader(
        "Upload Image",
        type=["png", "jpg", "jpeg"]
    )

    prompt = st.text_area(
        "Prompt",
        placeholder="Contoh: cinematic cyberpunk cat with neon lights"
    )

    run_button = st.button(
        "🚀 Generate",
        type="primary",
        use_container_width=True
    )

# =========================================================
# DISPLAY COLUMNS
# =========================================================
col1, col2 = st.columns(2)

# =========================================================
# INPUT PREVIEW
# =========================================================
with col1:

    st.subheader("Input Image")

    image = None

    if uploaded_file:
        image = Image.open(uploaded_file)

        st.image(
            image,
            use_container_width=True
        )

    else:
        st.image(
            create_placeholder(),
            caption="No Image",
            use_container_width=True
        )

# =========================================================
# OUTPUT SECTION
# =========================================================
with col2:

    st.subheader("Generated Output")

    if run_button:

        # Validasi prompt
        if not prompt.strip():
            st.error("Prompt wajib diisi.")
            st.stop()

        image_url = None

        # =====================================
        # Upload image jika ada
        # =====================================
        if uploaded_file:

            with st.spinner("Uploading image..."):

                success, result = upload_image_to_api(
                    image,
                    uploaded_file.name
                )

                if not success:
                    st.error(f"Upload gagal: {result}")
                    st.stop()

                image_url = result

        # =====================================
        # Generate AI
        # =====================================
        with st.spinner("Generating AI image..."):

            success, task_result = process_ai(
                image_url,
                prompt
            )

            if not success:
                st.error(task_result)
                st.stop()

            task_id = task_result

        st.info(f"Task ID: {task_id}")

        # =====================================
        # Polling result
        # =====================================
        progress_bar = st.progress(0)

        max_attempts = 30

        for attempt in range(max_attempts):

            time.sleep(5)

            progress = int(((attempt + 1) / max_attempts) * 100)

            progress_bar.progress(progress)

            success, data = get_result(task_id)

            if success:

                state = data.get("state")

                # SUCCESS
                if state == "success":

                    result_json = json.loads(
                        data.get("resultJson", "{}")
                    )

                    result_urls = result_json.get(
                        "resultUrls",
                        []
                    )

                    if result_urls:

                        st.success("Image generated successfully!")

                        st.image(
                            result_urls[0],
                            use_container_width=True
                        )

                    else:
                        st.warning("Tidak ada hasil gambar.")

                    break

                # FAILED
                elif state == "fail":

                    st.error("AI gagal memproses gambar.")
                    break

        else:
            st.warning("Request timeout.")

    else:

        st.image(
            create_placeholder(),
            caption="Output Preview",
            use_container_width=True
        )