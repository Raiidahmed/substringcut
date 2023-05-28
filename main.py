def split_string(long_string, max_length=2048):
    return [long_string[i:i + max_length] for i in range(0, len(long_string), max_length)]

# Example usage
long_string = """I’m just going to share it with you because of those issues of propped up with my presence in Butte 
last week to everybody and Jew. We had a couple talking about the user journey the way that we approach this problem 
but we kind of just want to focus on main leave, as you know, it’s mainly because of the maximizer decommission. And 
yes, this is just a graphic for the experience that you were probably familiar with some utilizing XP design of the 
mock ups. We kind of zoomed in on the mapping out to use a journeyz pacifically on the part where I act and we saw 
that mean issues that we’re coming with me or what is the act of getting these fields over two weeks. Having 
everything structured right in terms of objectivity and the page paths at times, took it out the zoom that out a 
little bit and did some design. We came down with a couple options and it our base MVP is to essentially Create all 
of the values that need to be copy and pasted over to XP within CMS mainly the objective idea if that’s all presented 
to the user in an organized fashion so we have some basic or preliminary Marcos on how this drop-down this menu can 
look with fields, and then we’ve got a few ideas of where exactly to place these items, and feel free to come in with 
any feedback or any questions so this is essentially the preliminary a drop-down idea on the first screen user comes 
in and experience fragments that they want to use on this experiments dropped on automatically displays a different 
variations of sad experience fragments and the user anchor ideas which corresponds they want to track for this 
experiment after completing these fields, and confirming we have the output screen where we have school tips and the 
difference is into the 1XP experiment experiment form is dimension, names, variations and then we also have dimension 
name control different variation names on third URLs copy buttons on the right side here just have this window, 
open the window, open translate, everything over and we have a little diagram of how these fields would be ported 
over to the experience experiment form Jump in to be have or do you happen to have like a example because I’m just 
having a hard time actions and just having trouble connecting the definitions of the titles here and I understand 
they correspond to the XP experiment form but as a business user, still a little technical Dimension name and I 
control things yeah yeah they’re just a little a little technical so I’m not sure that without really knowing if I 
would know what that meant it’s just I don’t know if dies language but that’s not the language we use. Just wonder if 
there’s an opportunity to make that may be a little more user-friendly but I see why it’s map the way it is so you 
can see how it corresponds to the form. Yeah I mean I can’t explain off the top of my head. we also have some 
resources, but essentially for this, we would also and that’s going to be one of my projects, essentially making sure 
that is the names are readable in a way that does make sense. Yeah, I mean George you like for me to run through like 
what each of these items mean no I was just thinking like if we had like a meeting that you do later on and Tatian 
but a test of scenarios so that I could see how the objective ID is map Also so the way previous side quickly yes so 
in the CMS side you’re putting in this information on the left so you’re going to select your experience fragments 
that’s like the experiment and to select your variations like your master variation and then your very should be etc. 
and then the anchor ID is like for the tracking so let’s say you want to measure how many button clicks you get based 
off of one variation you like math I didn’t see a mass but the output piece that is just oh I see exactly how it said 
an XP so I think the XPT would actually have to speak to OK business friendly like Justin Charante I guess around 
like do you ever have users expressing confusion around those names of those fields are no I mean that’s kind of like 
standard way of all the pillows are named on our side And what we can do is we can probably connect with Raiid. We 
can also include like excuse definition of what each of the fields means that I think there’s no exactly what they 
are talking about objective IDs, and like the ones that are not in the mood should be pre-populated with whatever, 
they don’t they won’t necessarily need to like figure out what it means inside it’s more like copy and paste 
exercise. Yeah I will say I really like the idea because I feel like at least inside, but I would love to have a 
reference and confused anchorite like I cannot recall with anchor ideas so I love I love the tool tips, so I think 
that is going to be essential. OK cool yeah Yeah so like you as a user, you would be having to fill out this input 
column and then we will generate the output and all you would do is copy and then going into the XP portal and just 
pasting it in the fields that align that makes sense yeah all right Before we move on to the specific locations, 
I also want to like I guess like guide the potential discussion a little bit into zoom out on a kind of vision for 
this hello I thought I think the comment that you made regarding was really good especially the reasoning behind that 
is it Andrew have like all the resources for you right now it’s just that they aren’t into rid of the resources are 
is into live leave waste together in this process, so what is trying to accomplish? Is Paul resources like the 
experiments guide pad where these are, these items are being put together, pulled out into the Stool and then also 
pull over all the user with really need to have open is the original one CMS page and the experiment XP experiment 
form only those two windows so with that in mind no yet feel free to create a may make any suggestions or let me know 
if there is anything from the user side that we are missing Anything else that you think would be necessary for the 
experience on this form the drop-down on the input and why I am also totally new to this babe the difference between 
the drop-down and then actually typing in whatever you need to type and yeah in the smoke up is because of the things 
like the experience fragments The anchor ideas when you use a journey, those items have already been created 
experience fragments experiencing the fragments are the pieces of the dynamic content on the page that can actually 
be changed and banker ideas are meant to label and connect to say like a button or a metric being tracked Act during 
this experiments, so when the users like these is it already been made and the drop down is just so that you know 
being able to already been made rather than having to remember the names of what you’ve already put together and copy 
and pasting them over into the field and end up having to double check if things go wrong Yeah that’s exactly it. 
It’s like we’re trying to make it as streamlined and as intuitive as possible for the users so only a drop-down 
you’re not able to input anything at all that’s how we envisioned it but we obviously like through testing could see 
if we want to be able to add it in manually as well And create it totally going to certain and not and not even 
allowed because then it’s on the field. Yeah essentially and then also like the reason I have nothing to do with 
experiments for that reason but yeah, the actual part of like clearing in and finding it’s gonna be like so we’ll 
have to see how that gets developed or to function properly quick question where with this where were the one CMS 
input Moto pop-up is that determined yet so we’ve got a few ideas in the next couple slides if you’re fine with going 
forward on this or that none of this as a whole but like just yeah message you get your question answered. Sorry I 
didn’t wanna jump ahead prematurely. Yeah yeah no that’s good night Exclamation OK so we have two potential ideas for 
a location experiment experience one of them is just within page properties you know we have an extra tab Sharon and 
we just placed this form there. We might have to have like some sort of a submit button around here then we have a 
confirmation that the user And goes over to the output tab where is display something like this within the same as 
paid properties form the other idea that we had is with some tool called Chromebook, and in this case the user would 
go down next to preview GQ and validation in the drop-down, you know user would say Then this pops up from the side 
you get here you get the form essentially and the same thing go you go over to stop and get this outperform it just 
the difference is is that you don’t have to navigated the page properties you just access it from the edit mode on 
the page Yeah, I was still like what if I had a preference between the two of you almost rather live in the page 
properties just because we’ve already got some in Elise for me for my for my brain publish that page anyway, 
I know we also have to publish the experience fragments, but it might make more sense in a user experience fragments. 
Then we go to the page with a test run, drop it in there and then set the properties Activate to me that makes more 
sense as opposed to it sounds like it might be experiencing a couple menus, so just just based off my usage I’m not a 
power user by any means, but I feel like this set up is a little more intuitive I would agree with Hannah on that But 
I think this clearly just has it has its own kind of come out which I think could be easier till I fully understand 
that all right now I’m saying that sounds good and yeah definitely submit button am I and you know maybe it’s just 
like for MVP but if you haven’t shared this XP dashboard link is that is that going to be the experiment that’s 
created I was thinking of a quick way to jump it to 1XP like whenever this menus pulled up so that you could 
configure your test and I know it’s just as easy as what is it that you are I was like XP daddy EXT what’s up XP 
specific experiment is XP – or just a link to maybe it should be free name the 2XP experiments or something like that 
but it was linked to Chili there’s two different options here I could either like I was originally thinking that I 
could just link directly to create an experiment for a button in the XP and just bring you straight to The form but 
there may be some issues with that the other option is for link to the fields shows you on your service list used to 
create an experiment from that page Noah quick question does he do SSOHS yes OK cool thing I would think point to 
completely transparent. I am not super familiar with the dashboard so I can’t really speak to which one makes more 
sense but I feel like you could it would be fine either way it might be nice to just be able to look at the 
dashboard, if you are all over the Over the dashboard is where you can click click on what type of experiment you 
want to create which is like 80 and maybe or NBT and then you can start your mouth I see yeah it sounds like maybe 
before but I think that would be fine. Whatever’s easiest to do like it sounds like jumping right into an experiment 
creation from this link me I’ll be feasible, so I think dashboard sounds good, all right. OK sounds good. No, 
we have any other agenda item there’s like one or two I am go ahead, but intuitive. Yeah that’s my feeling just from 
publishing pages like you know I know we go into the experience fragment to set it up but we have to publish the page 
regardless instead of those experience fragments, so I feel like and I’m curious, feel free to correct because we 
only successfully set up like one or two longer with the company so I would’ve loved to of gotten his feedback before 
his departure, but I would think that the flow would kind of be like OK. We set up the experience fragments first 
then we go into the pages that we want to run the experiment on and plug-in those experience fragments and then we 
set up experimentation here publish the page And experience greatness is that the flow? Yeah, I think you were 
published experience fragments first in the page for the matter if we like our publishing on the same go I mean, 
does it what do you have to do you do each experience fragment variation so it needs to go experience, 
fragment variation, a variation B, and then the page last year we won’t see it, yeah but here wherever adding adding 
in the information, the crown peach to plug-in Raiid if you wanna go to the next side that to as it’s like the same 
flow it’s just a different place in on the page so either side there or you go to the page properties to do it yeah 
well here’s a question so let’s say we are running a well. OK let’s say we’ve we’ve published the test on the page, 
what will show on this menu like we’ve already published a task will it just have a pre-filled information there like 
what if we want to publish another test on the same page when we have the ability to to like submit a new one yeah so 
I think the idea is like you were just modify the fields I submit and then get the new information to put in text to 
you Page so we won’t have I guess but I was kind of hoping to maybe see you almost see what the able to tell what we 
submitted to Ron the page that makes sense by looking at experimentation so I could go into pages property look at 
experimentation and see like OK we’ve already created or like generated some thing for this page, some sort of log in 
on it and then to get in-depth analytics the dashboard that’s just again it maybe not MVP but I think it would be 
helpful to keep track of what tests are running on which pages OK yeah let’s note that down there also been thought 
of because I know you mentioned that it Hass to be done like experience fragment page has there been a consideration 
for like maybe a publish button that could automatically queue up a selected experience fragment send the page that 
way it’s just like a one click publish situation so it’s limiting Windows and the tabs you have to have open in order 
to publish. I don’t know if they capability probably to be on the page to initiate the workflow but it’s just a 
thought a bundle publish it possible would make things a lot easier. Yeah let’s see you I mean that would be like in 
an Adobe feature. I feel like oh OK yeah yeah I don’t know if it’s like a limitation it’s just some thing that came 
to mind because I know you know redo show me to getting that there’s a lots of windows to jump around in, 
so I was just trying to think of how can we minimize having Sy decide and things like that it may not be possible 
especially over MVP yeah I could’ve definitely check that is a great solution like if it knows where to put these 
things or if I can, you know, I can tell by copying pasting from you that would make it so much easier because I just 
got completely lost but I’m grabbing the URLs I don’t know like the wrapping the right part of the URL is this the 
right I’m not sure so that’s what David and I struggled a lot was to mentally labile yeah Think this will be a great 
solution ha ha cool yeah that’s kind of like the main theme song for yes OK sir feel free to stop me if we already 
had this information but I and I just wanted to ask him what is it like to create an experiment some isn’t maximizer 
like right now I know that you have like in assistance with distance with him they have I’d like what information do 
you need to bring to the table to them, yes so we need to tell them what you are a test on usually provide a mock up 
the PowerPoint mock up of what we want the variance to look like what we want to track and I’m trying to think any 
special let’s do we want to capture all of the button clips all of you know or do we just want to catch up on button 
and it’s clicks which I’m assuming correlates with getting Paredes on typically will track we check all the buttons 
are landing page which I want to see her like five or more so we can track multiple actions for a variant and that’s 
what we provide to them in a CAD in like user story the format I can send an example over to you asking for campaign 
acceptance document off on that all the time and where we want to see the traffic on mobile browsers do we wanna see 
you then and how we want the traffic split the other one all right"""

substrings = split_string(long_string)

print("Split: \n")
for i, substring in enumerate(substrings):
    print(substring + "\nRemember, you are still waiting for me to paste in the rest of the transcript until I say the "
                      "key word for you to start summarizing.")
    print("Split: \n")
