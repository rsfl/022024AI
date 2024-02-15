#r8_Mx4c5p56uH1JQzNmRWMiAb8ubMFrbVi4E33yT
import os
os.environ["REPLICATE_API_TOKEN"] = ""
import replicate 
from PIL import Image
from urllib.request import urlretrieve 

out = replicate.run(
    "stability-ai/stable-diffusion:27b93a2413e7f36cd83da926f3656280b2931564ff050bf9575f1fdf9bcd7478",
    input={"prompt": "Miami Beach"}
    )

urlretrieve(out[0], "/tmp/out.png")
background = Image.open("/tmp/out.png")