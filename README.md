<h2>⏪ Digital CV ⏩</h2>
<br>
<a href="https://petrugiurca.streamlit.app/">▶ Visit My Website ◀</a>

<br>

### Installation
`pip install --no-cache-dir -r requirements.txt`

`streamlit run app.py`

Access the application at http://localhost:8501

</br>

### Containerize Streamlit app

+ Build the image:
`docker image build --no-cache -t digital-cv .`

+ Run the container:
`docker container run -d -p 8501:8501 digital-cv`
