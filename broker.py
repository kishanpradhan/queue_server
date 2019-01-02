from celery import Celery
import urllib.request
import os

# Where the downloaded files will be stored
BASEDIR=os.path.dirname(os.path.realpath(__file__))

# Create the app and set the broker location (RabbitMQ)
app = Celery('UploaderApp',
             backend='rpc://',
             broker='pyamqp://guest@localhost//')


@app.task
def download(file_name, data, path):
    """
    Append data to file given
      data: the data to append
      filename: the filename used to save the data in filepath
    """
    # data = response.read()
    print("Download file called", file_name, path, data)
    with open(BASE_DIR + "/result/" + path.strip("/") + "/" + file_name, 'a') as file:
        # file.write(bytes(data))
        # file.write(data.encode())
        file.write(data)
    file.close()

@app.task
def list():
    """ Return an array of all downloaded files """
    return os.listdir(BASEDIR)

    
