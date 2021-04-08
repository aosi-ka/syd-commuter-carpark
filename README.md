# syd-commuter-carpark
Only currently available offline, will eventually be deploying this on a website so I don't have to run the app on my personal computer every morning.

# Iteration 1

## Description:
A web application using Python Flask determining whether if a commuter car park possess any available parking spots. Ever since moving to a new suburb in Sydney, I have had to drive to the train station, which takes approximately ~7 minutes to get to the station, only to find out that there is no parking spots, as a result make me miss the train. Usually if I find that the car park is full, I would go to the next closest station to park, which takes an additional 5 minutes. App is quite trivial, following the Transport for NSW's API and its recommendation.

## Inputs
Type in a station that is supported by TfNSW's API and it'll return whether if the station's commuter car park is full or not

## Takeways
* Learnt how to utilise python flask to deliever a frontend and read off the backend APIs.
* Will eventually learn how to deploy on a website
* Utilising CSS bootstraps to not "re-invent the wheel"

## Further Updates in the Future
* Will eventually support metro lines , have a graphics to determine which zones have parking spots (Sydney Metro have zoned out the commuter car park)
* Utilise parking history to help users out when the commuter car park is usually free (include some graphics and some previous data hourly basis)
* Add the current time of request for clarity.
* Increase security around API calls, need a better way to abstract the API_KEY (sorry for the freeloaders, however it is free to signup to Transport for NSW Open Data!)
* Make classes for API requests
