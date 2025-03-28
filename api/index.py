from rembg import remove
from PIL import Image
import io

def handler(request):
    if request.method == 'POST':
        file = request.files['image']
        input_image = Image.open(file)
        output_image = remove(input_image)

        img_io = io.BytesIO()
        output_image.save(img_io, format="PNG")
        img_io.seek(0)

        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'image/png'
            },
            'body': img_io.read(),
            'isBase64Encoded': True
        }

    return {
        'statusCode': 405,
        'body': 'Method Not Allowed'
    }
