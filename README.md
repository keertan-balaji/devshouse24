![alt text](https://![Q](https://github.com/keertan-balaji/devshouse24/assets/121657323/d0f676f6-0dbd-4020-99b5-c321cc98cd65)
# EquiGuard
Connect, Respect, Chat!

- The following repository is the backend implementation of an AI system that was created for the DEVSHOUSE'24 hackathon conducted at the Vellore Institute of Technology, Chennai

- Our project is a simple yet efficient approach to tackle toxicity and hateful texts and Chats on the Internet. This was done by implementing a Bi-Directional LSTM trained on a vast corpus of hateful texts.

- The following repository contains the 'app' folder that was dockerized and deployed into AWS Lambda Function. This is to provide a quick and seamless integration with the existing systems

- The trained model was tested by implementing a Discord - bot on a group chat. The video of the demonstration of the work is provided in the DevFolio Website

- To run the backend of the Application Locally
```
cd app
uvicorn main:app --reload  
```
- The repository also has the following files:-
  - Devhouse24OLID.ipynb - Used to train the model
  - Model - The folder containing the saved model along with a few utility files
  - DicordBOT - The Python file used to deploy the model as a Discord Bot
