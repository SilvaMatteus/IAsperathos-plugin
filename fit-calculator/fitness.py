from PIL import Image, ImageDraw
from skimage.measure import compare_ssim as ssim
from numpy import array
from pickle import loads
from flask import Flask, request
from os import path
import genetic.individual
import json
from base64 import b64decode

image_path = '/home/ubuntu/image.jpg'
individual_path = '/home/ubuntu/individual'

def compare(img1, img2):
    cv_img1 = array(img1)
    cv_img2 = array(img2)
    
    return ssim(cv_img1, cv_img2)

def get_fitness(data):
  image = Image.open(image_path)
  image.load()
  image = image.convert('L')
  
  im = Image.new("L", (image.width, image.height))
  dr = ImageDraw.Draw(im)
  
  individual = loads(b64decode(data["individual"]))
  genome = sorted(individual.genome, key=(lambda g : g.z))
  
  for gene in genome:
    pos = (gene.x-gene.r, gene.y-gene.r, gene.x+gene.r, gene.y+gene.r)
    dr.ellipse(pos,fill=gene.color)

  return compare(image, im)

app = Flask(__name__)

@app.route('/calculate-fitness', methods=['POST'])
def calculate_fitness():
  data = json.loads(request.data)
  return json.dumps({'fitness': get_fitness(data)})

if __name__ == '__main__':
  import sys
  app.run(host='0.0.0.0', port=sys.argv[1], debug=True)
