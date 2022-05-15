#google_images_downloadをインストール
from google_images_download import google_images_download

def fetch_image(params_dict):
    response = google_images_download.googleimagesdownload()
    arguments = {
      "keywords"        : params_dict['search_keywords'],
      "limit"           : params_dict['limit'],
      "format"          : params_dict['image_format'],
      "output_directory": params_dict['output_directory'],
      "no_directory"    : True
    }
    response.download(arguments)

def input_argument():
    params_dict = {}

    search_keywords=input('search keywords:')
    while not search_keywords:
      search_keywords=input('search keywords:')

    limit=input('How much do you want a image?:')
    while not limit.isdigit():
      limit=input('How much do you want a image?:')

    print("0:'jpg',1:'gif',2:'png',3:'bmp',4:'svg',5:'webp',6:'ico',7:'raw'")
    image_format = ['jpg','gif','png','bmp','svg','webp','ico','raw']
    image_format_number = input('Please select image format number(0~7):')
    while not image_format_number.isdigit() or int(image_format_number) > 7:
      image_format_number = input('Please select image format number(0~7):')

    output_directory = input('Where are you saving download image?')
    if not output_directory:
      output_directory = 'downloads'

    params_dict['search_keywords'] = search_keywords
    params_dict['limit'] = limit
    params_dict['image_format'] = image_format[int(image_format_number)]
    params_dict['output_directory'] = output_directory

    return params_dict

def main():
    params_dict=input_argument()
    fetch_image(params_dict)

if __name__ == '__main__':
    main()