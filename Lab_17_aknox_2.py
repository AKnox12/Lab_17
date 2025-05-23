# Python
# Autumn Knox
# Plotting other language repos
# May 7th 2025

'''All the imports for the program'''
import requests

from plotly.graph_objs import Bar
from plotly import offline

'''Setting up the main'''
def main():
    visualizer = Cpp_repo_visualizer()
    visualizer.Viaualize()

'''Beginning class for the visualizer'''
class Cpp_repo_visualizer: 
    def Viaualize(self):

        '''API calls and store response'''
        url = 'https://api.github.com/search/repositories?q=language:cpp&sort=stars'
        headers = {'Accept': 'application/vnd.github.v3+json'}
        r = requests.get(url, headers=headers)
        print(f"Status code: {r.status_code}")

        '''Process results'''
        response_dict = r.json()
        repo_dicts = response_dict['items']
        repo_links, stars, labels = [], [], []
        for repo_dict in repo_dicts:
            repo_name = repo_dict['name']
            repo_url = repo_dict['html_url']
            repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
            repo_links.append(repo_link)
            
            stars.append(repo_dict['stargazers_count'])

            owner = repo_dict['owner']['login']
            description = repo_dict['description']
            label = f"{owner}<br />{description}"
            labels.append(label)

        '''Make visualization'''
        data = [{
            'type': 'bar',
            'x': repo_links,
            'y': stars,
            'hovertext': labels,
            'marker': {
                'color': 'rgb(60, 100, 150)',
                'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
            },
            'opacity': 0.6,
        }]

        '''Font size and stylization in graph'''
        my_layout = {
            'title': 'Most-Starred CPP Projects on GitHub',
            'font': {'size': 28},
            'xaxis': {
                'title': 'Repository',
                'tickfont': {'size': 14},
            },
            'yaxis': {
                'title': 'Stars',
                'tickfont': {'size': 14},
            },
        }

        fig = {'data': data, 'layout': my_layout}
        offline.plot(fig, filename='cpp_repos.html')

if __name__=="__main__":
    main()