# Devpost Writeup

# Inspiration
People think rashly and make bad decisions when their emotions take the best of them, and they are in the “heat of the moment.” Many times, this leads to people venting out by posting controversial stuff on social media. Our team saw the implications controversial posts had and the damage it was causing. People were getting fired from their jobs, getting rescinded from colleges, losing sponsorships etc. By no means did we agree with the message behind these posts, but we knew that if people had known the repercussions behind such posts, they certainly would not have posted.

With social media playing a large part in our society, there is little monitoring done on any of the major social media platforms to make sure that one does not make a bad decision regarding a post. Our team wanted to fix this.


# What it does

To solve this issue, our team created PreTweet. When someone is the “heat of the moment” or if someone is unsure about a Tweet they are about to post, we encourage them to come to our site. The user will enter their email address and type up the Tweet they plan to publish. But instead of posting the Tweet right away, our software will send the user an email 3 days later asking if they want to post the Tweet. The reason we chose 3 days is that by this point, we hope the user would have calmed down and hopefully they can make a better decision about their tweet. Our website also shows the user how negative or positive their Tweet is. If the user **does not** want the tweet to post they do not have to do anything. If the user **does** wants to post the tweet, they can come to our website to do so. If the user is still unsure about whether they want to post their Tweet or not, our site also offers the ability for the Tweet to be sent to a professional for review.


# How we built it

In the process of building our application all of us ventured out and got to expand our knowledge in new languages, libraries, and frameworks. Some of the major frameworks used were Flask and Svelte. Along with Flask many other libraries such as Flask-Dance, Flask-Login, and Flask-SqlAlchemy were used in order to support and add some of our extra features like the login with Twitter, keeping track of users, and easy database entry which flask couldn’t do alone. For the front end framework we made use of Svelte and the rest of the front end was mostly written in HTML, CSS, javascript, and typescript. For the sentiment analysis we used textblob which helped us analyze a positive or negative sentiment of the text for each post and to send emails we used the Python libraries of email and smtplib, and finally in order to send tweets we used tweepy which made it easy for us to interface with the Twitter API and tweet out our users' posts.


# Challenges we ran into

One of the major challenges that we faced was virtual collaboration. Being far away from each other meant that we could not as readily communicate with our teammates or as easily share code. Another problem that this presented was that there were more potential distractions that the real world which would distrupt demo recording and make calls harder to coordinate. All of this made it so that communication and coordination became even more important that they usually are for in-person hackathons.


# Accomplishments that we're proud of

As a team I think one of our greatest achievements reflecting on this past weekend would be our ability to split up work, work together, and help each other. I think that working on a hackathon remotely was started out as a challenge for us but we were quickly able to conquer it and work productively. Being able to work with different technologies and implement everything together was also a big achievement. Many of us learned many new things and stepped out of our comfort zones and were able to succeed. In that sense, this has been possibly one of our biggest achievements individually and in the larger goal of helping people make good decisions on social media.

# What's next for PreTweet
We want to help people make the right decisions on what they post to ANY social media platform. So, in the future, we plan to expand PreTweet to Facebook, Instagram, Whatsapp etc.
