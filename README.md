<h1 align="center"> Jet Engine Remaining Useful Life Prediction</h1>

<p align="center"> 
  <img src="assets/engine.png" alt="RUL Prediction">
</p>


<!-- TABLE OF CONTENTS -->
<h2 id="table-of-contents"> :book: Table of Contents</h2>

<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project"> ➤ About The Project</a></li>
    <li><a href="#documentation"> ➤ Documentation</a></li>
    <li><a href="#build-with"> ➤ Build With</a></li>
    <li><a href="#project-files-description"> ➤ Project Files Description</a></li>
    <li><a href="#getting-started"> ➤ Getting Started</a></li>
    <li><a href="#showcase"> ➤ Showcase</a></li>
    <li><a href="#contribution"> ➤ Contribution</a></li>
    <li><a href="#support"> ➤ Support </a></li>
    <li><a href="#license"> ➤ License </a></li>
    <li><a href="#credits"> ➤ Credits </a></li>
  </ol>
</details>


![-----------------------------------------------------](assets/rgb.png)


<!-- ABOUT THE PROJECT -->
<h2 id="about-the-project"> :pencil: About The Project</h2>

<p align="justify"> 
  Jet engines are one of the most sophisticated pieces of tech that humankind has known in its history. They are key components of any modern jet either commercial or military and few missiles and rockets also. Their failures are catastrophic and lead to loss of millions of dollars and precious life. But their maintenance is too costly and time consuming but needs to be done routinely hence costs a fortune to maintain and check them for any type of damage propagation due mechanical tear.  
</p>

<p align="justify">
  To reduce this cost of maintenance by calculating Remaining Utility Life of jet engines based on various sensor data we have designed a robust machine learning solution.
</p>


![-----------------------------------------------------](assets/rgb.png)


<!-- Documentation -->
<h2 id="documentation"> :bookmark: Documentation</h2>

Refer the following documents for better understanding of the dimensions of project.


<ul>
    <li><a href="https://github.com/AbhijeetSrivastav/Jet-Engine-RUL-Prediction/blob/main/documentation/HLD_1.0v_Jet-Engine-RUL-Prediction.pdf" target="_blank">High Level Documentation (HLD)</a></li>
    <li><a href="https://github.com/AbhijeetSrivastav/Jet-Engine-RUL-Prediction/blob/main/documentation/LLD_1.0v_Jet-Engine-RUL-Prediction.pdf" target="_blank">Low Level Documentation (LLD)</a></li>
    <li><a href="https://github.com/AbhijeetSrivastav/Jet-Engine-RUL-Prediction/blob/main/documentation/DPR_1.0v_%20Jet_%20Engine_%20RUL_Prediction.pdf" target="_blank">Detailed Project Report (DPR)</a></li>

</ul>


![-----------------------------------------------------](assets/rgb.png)


<!-- OVERVIEW -->
<h2 id="overview"> :cloud: Overview</h2>
<p align="justify"> 
  The solution proposed is a machine learning model that can be implemented to perform above mentioned use cases. It will predict the RUL of the engine giving the servicing team an estimate of the health of the engine based on which they can decide how much priority they should give to the engine. If an engine has very low RUL they can give more time to check deploy whether this engine should be used further or retired, or if an engine has very high RUL then they should
perform a routine checkup.
</p>

<p align="justify">
  This will reduce the time and money invested in maintenance as well as it will divert attention to only those engines who require it more leading to less accidents.
</p>


![-----------------------------------------------------](assets/rgb.png)


<!-- BUILD WITH -->
<h2 id="build-with"> :hammer: Build With</h2>

<a href="https://www.python.org" target="_blank">
    <img align="left" src="https://github.com/AbhijeetSrivastav/AbhijeetSrivastav/blob/main/LanguageToolsIcon/python/python.svg" alt="Python" height ="42px"/>
</a>

<a href="https://flask.palletsprojects.com/en/2.2.x/" target="_blank">
    <img align="left" src="https://github.com/AbhijeetSrivastav/AbhijeetSrivastav/blob/main/LanguageToolsIcon/flask/flask.jpg" alt="flask" height="42px"/> 
</a>

<a href="https://scipy.org/" target="_blank">
    <img align="left" src="https://github.com/AbhijeetSrivastav/AbhijeetSrivastav/blob/main/LanguageToolsIcon/scipy/scipy.png" alt="scipy" height="42px"/>
</a>

 <a href="https://git-scm.com/" target="_blank">
    <img align="left" src="https://github.com/AbhijeetSrivastav/AbhijeetSrivastav/blob/main/LanguageToolsIcon/git-scm/git-scm.svg" alt="git" height='42px'/>
</a>

<a href="https://www.docker.com/" target="_blank">
    <img align="left" src="https://github.com/AbhijeetSrivastav/AbhijeetSrivastav/blob/main/LanguageToolsIcon/docker/docker.png" alt="docker" height='42px'/>
</a>


![-----------------------------------------------------](assets/rgb.png)


<!-- PROJECT FILES DESCRIPTION -->
<h2 id="project-files-description"> :floppy_disk: Project Files Description</h2>

- **research** - Contains base research paper and `experiments.ipynb` notebook
- **CMaps** - Data collected on different settings and configurations by NASA
- **rul** - Contains all the components, configurations, artifacts and pipelines
  - `components` - Components of Data Pipelines
  - `entity` - Configuration and artifact entity of components
  - `pipeline` - Training and Batch pipeline
  - `config.py` - Configuration of `rul` package
  - `exception.py` - Exception handler of `rul` package
  - `logger.py` - Logger of `rul` package
  - `predictor.py` - Model Resolver
  - `utils.py` - Collection of utility functions
- **static** - Static files for flask app
- **templates** - Templates of flask app
  

![-----------------------------------------------------](assets/rgb.png)


<!-- GETTING STARTED -->
<h2 id="getting-started"> :pushpin: Getting Started</h2>

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

1. Clone the repo
<pre><code>$ git clone https://github.com/AbhijeetSrivastav/Jet-Engine-RUL-Prediction.git</code></pre>

1. Create conda environment
<pre><code>$ conda create -n jet-rul</code></pre>

1. Activate the conda environment
<pre><code>$ conda activate jet-rul </code></pre>

1. Install requirements to conda environment
<pre><code>$ pip install -r requirements.txt</code></pre>

1. Navigate to project directory
<pre><code>$ cd "Project Directory"</code></pre>

1. Run flask app to get access to pipelines UI
<pre><code>$ python app.py </code></pre>


**Note:-** After step 5 make sure to create your MongoDB database and dump the base dataset `rul.csv` in it using `data_dump.py` script after updating MongoDb client in it and also don't forget to create `.env` file and mention your MongoDb credential within it which are accessed by the `config.py` in `rul` package to run the pipelines. 


![-----------------------------------------------------](assets/rgb.png)


<!-- Showcase -->
<h2 id="showcase"> :camera: Showcase</h2>

<center>
  <table>
    <tr>
      <td><img width="600" alt="Show 1" src="assets\show (8).png"></td>
      <td><img width="600" alt="show 2" src="assets\show (9).png"></td>
    </tr>
    <tr>
      <td><img width="600" alt="show 3" src="assets\show (10).png"></td>
      <td><img width="600" alt="show 4" src="assets\show (11).png"></td>
    </tr>
    <tr>
      <td><img width="600" alt="show 5" src="assets\show (12).png"></td>
      <td><img width="600" alt="show 6" src="assets\show (13).png"></td>
    </tr>
    <tr>
      <td><img width="600" alt="show 7" src="assets\show (14).png"></td>
      <td><img width="600" alt="show 8" src="assets\show (15).png"></td>
    </tr>
  </table>
</center>


<a href="https://drive.google.com/file/d/14HazGAvVN9XcPZuk_mXXZ9oR06NvWi5I/view?usp=sharing" target="_blank"><b>Demo Video</b></a>


![-----------------------------------------------------](assets/rgb.png)


<!-- Contribution -->
<h2 id="contribution"> :paperclip: Contribution</h2>

The Machine Learning Guide Project is a open source project. I a committed to a fully transparent development process and highly appreciate any contributions. Whether you are helping me fixing bugs, proposing new feature, improving our documentation or spreading the word - we would love to have you as part of this project.

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b main/feature`)
3. Commit your Changes (`git commit -m 'Add some feature'`)
4. Push to the Branch (`git push origin feature`)
5. Open a Pull Request


![-----------------------------------------------------](assets/rgb.png)


<!-- Support -->
<h2 id="support"> :sparkling_heart: Support</h2>

I open-source almost everything I can, and I try to reply to everyone needing help using these projects. Obviously,
this takes time. You can use this service for free.

However, if you are using this project and are happy with it or just want to encourage me to continue creating stuff, there are few ways you can do it :-

- Giving proper credit when you use Machine Learning Guide, linking back to it :D
- Starring and sharing the project :rocket:
  
Thanks! :heart:


![-----------------------------------------------------](assets/rgb.png)


<!-- License -->
<h2 id="license"> :book: License</h2>


```text
Apache License 
Copyright (c) 2022 Abhijeet Srivastav
 
  "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.

      "Licensor" shall mean the copyright owner or entity authorized by
      the copyright owner that is granting the License.

      "Legal Entity" shall mean the union of the acting entity and all
      other entities that control, are controlled by, or are under common
      control with that entity. For the purposes of this definition,
      "control" means (i) the power, direct or indirect, to cause the
      direction or management of such entity, whether by contract or
      otherwise, or (ii) ownership of fifty percent (50%) or more of the
      outstanding shares, or (iii) beneficial ownership of such entity.

      "You" (or "Your") shall mean an individual or Legal Entity
      exercising permissions granted by this License........
```
[Apache License](https://github.com/AbhijeetSrivastav/Jet-Engine-RUL-Prediction/blob/main/LICENSE)

![-----------------------------------------------------](assets/rgb.png)


<!-- Credits -->
<h2 id="credits"> :scroll: Credits</h2>

Abhijeet Srivastav

- [![GitHub Badge](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/AbhijeetSrivastav)

- [![Linkedin Badge](https://img.shields.io/badge/-LinkedIn-0e76a8?style=style=for-the-badge&logo=Linkedin&logoColor=white)](https://www.linkedin.com/in/abhijeet-srivastav-02245a18b/)

- [![Instagram Badge](https://img.shields.io/badge/-Instagram-e4405f?style=style=for-thebadge&logo=Instagram&logoColor=white)](https://instagram.com/abhijeet.codes/)



![-----------------------------------------------------](assets/rgb.png)
