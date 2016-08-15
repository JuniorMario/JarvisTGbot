#!/usr/bin/python

from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser


# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.



def pesquisa(arg):
  DEVELOPER_KEY = "AIzaSyD9YO_dl4jmsNfKBHq4OuYCZ77d-9Tut7s"
  YOUTUBE_API_SERVICE_NAME = "youtube"
  YOUTUBE_API_VERSION = "v3"
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)

  # Call the search.list method to retrieve results matching the specified
  # query term.
  search_response = youtube.search().list(
    q=arg,
    part="id,snippet",
    maxResults=7
  ).execute()

  videos = []
  channels = []
  playlists = []

  # Add each result to the appropriate list, and then display the lists of
  # matching videos, channels, and playlists.
  for search_result in search_response.get("items", []):
    if search_result["id"]["kind"] == "youtube#video":
      videos.append("%s (%s)" % (search_result["snippet"]["title"],
                                 search_result["id"]["videoId"]))
    elif search_result["id"]["kind"] == "youtube#channel":
      channels.append("%s (%s)" % (search_result["snippet"]["title"],
                                   search_result["id"]["channelId"]))
    elif search_result["id"]["kind"] == "youtube#playlist":
      playlists.append("%s (%s)" % (search_result["snippet"]["title"],
                                    search_result["id"]["playlistId"]))
  videoss = videos
  channelss = "Channels:\n", "\n".join(channels), "\n"
  playlistss = "Playlists:\n", "\n".join(playlists), "\n"
  res = []
  for resu in videoss:
    res.append(resu)
  print(res)
  res1 = str(res[0].encode('utf-8'))
  res2 = str(res[1].encode('utf-8'))
  res3 = str(res[2].encode('utf-8'))
  res4 = str(res[3].encode('utf-8'))
  res5 = str(res[4].encode('utf-8'))
  res1 = res1.split('(')
  res2 = res2.split('(')
  res3 = res3.split('(')
  res4 = res4.split('(')
  res5 = res5.split('(')
  link1 = res1[1].strip(')')
  link2 = res2[1].strip(')')
  link3 = res3[1].strip(')')
  link4 = res4[1].strip(')')
  link5 = res5[1].strip(')')
  youbegin = 'https://www.youtube.com/watch?v='
  strires = "[{}]({}{})\n\n[{}]({}{})\n\n[{}]({}{})\n\n[{}]({}{})\n\n[{}]({}{})".format(res1[0], youbegin, link1,res2[0], youbegin, link2, res3[0],youbegin, link3, res4[0], youbegin, link4, res5[0], youbegin, link5)
  return strires