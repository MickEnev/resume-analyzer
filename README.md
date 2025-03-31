## AI Powered Resume Analyzer

This is an app that will take in a resume and parse it for key words then use Gemini to match those keywords to a job description and indicate whether or not you will be a good fit for the job as well as other insights. Currently, the user is able to upload both a pdf of their resume, and a text file containing the job description. The resume is then parsed and skills are extracted from the user's resume. These skills as well as the job description are passed to Gemini and it generates a response based on how suited the selected role is for the user. 

![Example-Response](https://github.com/user-attachments/assets/7bfc8ef9-fbfa-49d3-b5d9-30b51b72e5c1)


## Usage

**Backend:** A gemini api key is needed which can be placed in a .env file. Flask is also required which can be installed with pip install flask. Once flask is installed you can run the backend by running pip flask --app app run. 

**Frontend:** Before running the front end you need to make sure you have the appropriate packages installed by running npm i. Then you can simple run npm run dev from the frontend/res-analyzer directory.

When both are running you should be able to upload your resume as well as the job description and receive personalized feedback.

## Roadmap

Next steps are to add buttons so the user can further prompt the LLM. Buttons will include: Next steps, Skill match percentage, and Check another job description.
