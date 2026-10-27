from pyzbar.pyzbar import decode
from PIL import Image
import tempfile
import os


def extract_urls(uploaded_files):
    """
    Read multiple QR images and return all unique URLs.
    """

    urls = []

    for file in uploaded_files:

        # Save uploaded image temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp:

            tmp.write(file.read())
            image_path = tmp.name

        try:

            image = Image.open(image_path)

            decoded = decode(image)

            for obj in decoded:

                url = obj.data.decode("utf-8")

                if url not in urls:
                    urls.append(url)

        except Exception as e:

            print(f"Error reading QR: {e}")

        finally:

            if os.path.exists(image_path):
                os.remove(image_path)

    return urls