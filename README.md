![alt text](https://chat.google.com/u/3/api/get_attachment_url?url_type=FIFE_URL&content_type=image%2Fpng&attachment_token=AOo0EEXl54xzS7O2ft51J7rrQjKB69rc8JT3zh0i%2BQseewNKu7duT3SXWH5vc%2B8o9JF9BHe7r%2FxB%2BPyro7fv0iijaDyHgElIjZ435VxwOcalSn8kfeVe85T0y9PmHW3AMA%2Bq5XSVcos2Ke7UzmmJ%2FdNyaA4dxc5hdLrLI2wYluTfZxt6a4vz%2Bd4AlDjQp39FBcqoYJb1lpFI%2By3py6dbF3gWWqVs3zb3TyzfQf0fmp%2FnKO%2FnL98WY0y45bPKQ1Eft5rl2coviQJXStVfuA5DYK6pSk%2FiXm6AmxA%2BHXd%2B9l05pYzyDG72CJer%2BONiEhUy7XHp5VpKvscvdwHSvguGDXDqJ9NCQkq0%2FtGvXlfccxAlwYkDEN2xGXBPdqovpbEodfHTlLdNtPKOgiC8EWeQQFNfvT%2BmWqkBXKuJF4YBkDCGHBAlAjiIgPMFOtN2F0klj8k7byMpSjYMPbBU9kbeiecg33kY4Igt14l0VEKtIe9BO9wcWFubAq%2FSGc1jghomSpOs4Q%2B6bqtYS0qfAGWSTHD349vufCxd8ADLFmf1bSUQPpnQBi80LTWbHEv5mzkBnvk%3D&sz=w512&authuser=3)
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
