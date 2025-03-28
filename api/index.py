from rembg import remove
from PIL import Image
import io
import base64

def handler(request):
    if request.method == 'POST':
        file = request.files['image']
        input_image = Image.open(file)
        output_image = remove(input_image)

        img_io = io.BytesIO()
        output_image.save(img_io, format="PNG")
        img_io.seek(0)

        # Convert image to base64
        img_base64 = base64.b64encode(img_io.read()).decode('utf-8')

        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json'
            },
            'body': {
                'image': img_base64
            }
        }

    return {
        'statusCode': 405,
        'body': 'Method Not Allowed'
    }
