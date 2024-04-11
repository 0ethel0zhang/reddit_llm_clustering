# reddit_llm_clustering
Clustering using LLM API for reddit threads.
As of 2023/04/10, the latest LLM model being used is Gemini.

## Prerequisites
You MUST input a LLM API key (i.e. Gemini) to cluster. Check out [this official website](https://ai.google.dev/?gad_source=1&gclid=CjwKCAjw8diwBhAbEiwA7i_sJZLCB0xID1tawREFrEBdVmAftMUKdaKT7N-vFo2-1umEFBzgtAc0txoCEmEQAvD_BwE) for the how-to.<br>
<br>
(OPTIONAL) If you want to get live hot reddit posts. ([This is a good repo on GitHub](https://rymur.github.io/) to help to set up your reddit API. You might also want to check out [the official reddit developer website](https://www.reddit.com/wiki/api/) for how to set up your own API.)<br>

## Instructions:

1. Copy this repository:

  `git clone https://github.com/0ethel0zhang/reddit_llm_clustering.git`

2. Create a virtual environment running the following command in command line (Replace the NAMEYOULIKE part with whatever name you want to call your virtual environment):

  `conda create -f environment.yml -n NAMEYOULIKE`

3. Activate the environment using:

  `conda activate NAMEYOULIKE`

4. Create a .env file in the main directory with the following access information (use your own keys and tokens): <br>
   <br>
   You MUST input a LLM API key (Gemini) to cluster. Check out [this official website](https://ai.google.dev/?gad_source=1&gclid=CjwKCAjw8diwBhAbEiwA7i_sJZLCB0xID1tawREFrEBdVmAftMUKdaKT7N-vFo2-1umEFBzgtAc0txoCEmEQAvD_BwE) for the how-to.<br>
   <br>
   (OPTIONAL) If you want to get live hot reddit posts.    ([This is a good repo on GitHub](https://rymur.github.io/) to help to set up your reddit API. You might also want to check out [the official reddit developer website](https://www.reddit.com/wiki/api/) for how to set up your own API.)<br>

  `export user_name = "whatever"`<br>
	`export client_id = "whatever"`<br>
	`export client_secret = "whatever"`<br>
	`export redirect_uri = "whatever"`<br>
	`export app_name = "whatever"`<br>
  `export access_token = "whatever"`<br>
  `export API_KEY = "whatever"`<br>

5. There are two programs that you can run:

   5.1 (OPTIONAL) Allows you to use **your reddit API** (prerequisite for running this program) to get live data. The default subreddit is r/yoga. You can edit the `thread` based on your interest.<br>
   `python reddit_r_yoga.py`
  
   5.2 Clusters sub-reddit titles into groups and print out each cluster and the underlying titles. You can check out the methodology more on [my GitHub tutorial dedicated to the methodology](https://github.com/0ethel0zhang/quantcon2022).<br>
   `python get_titles.py`
  
## OUTPUT
After everything finished running, **Viola**, you have:
  1) a document called output.py with the Reddit top hot threads in json format. (If you ran the reddit program, you'd have the latest Reddit hot threads.)
  2) a csv file that has the result of the clustering with the following columns of data `cluster`,`title`,`permalink`.
