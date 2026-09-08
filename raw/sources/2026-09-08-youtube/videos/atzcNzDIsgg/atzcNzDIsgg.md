# LIVE BUILD: We Vibe-Coded a SaaS App in 60 Minutes (No-Code Founder Builds a Business From Scratch)

- Video: https://www.youtube.com/watch?v=atzcNzDIsgg
- Channel: Adam Robinson (UCSHn0Px37BjzMqnZBmVWwcQ)
- Published: 20250911
- Captured: 2026-09-08T07:41:45.543828+00:00
- Transcript: youtube_automatic_captions; en-orig
- Exact captions: atzcNzDIsgg.en-orig.json3
- Public-use boundary: Publicly accessible source, collected for private research/context; reuse in new public copy is not approved.
- Speaker caution: Captions are not diarized. Guest statements must not be attributed to Adam without contextual verification.

## Transcript

[00:00:00] And now I could ship this app and
[00:00:01] probably charge people for it.
[00:00:03] >> And when I when Jesse has shown me those
[00:00:06] apps or I mean even what we're looking
[00:00:08] at right now and he's doing it live like
[00:00:11] this is another one this lead magic
[00:00:12] command center.
[00:00:13] >> It took me like a day probably uh to
[00:00:15] build. Basically I just wanted to track
[00:00:17] every time somebody mentioned our
[00:00:19] company uh on LinkedIn. So I just built
[00:00:22] this basically and this was all a vibe
[00:00:24] code right now. I could ship this app
[00:00:26] and probably charge people for it. they
[00:00:28] would probably buy it because it's
[00:00:29] valuable and it updates every day. But
[00:00:31] like this took me like a day to build
[00:00:33] now and you know I would say this is on
[00:00:35] par with any sort of SAS application
[00:00:37] that's out there from a um you know just
[00:00:41] looking at it. But this what I want to
[00:00:42] track is like are they talking about us?
[00:00:46] What are they saying about our company?
[00:00:48] You know, we get a lot of uh inbound
[00:00:50] leads just because people mention us,
[00:00:52] but this is like an internal application
[00:00:54] for our company, right? We have a CRM
[00:00:57] that's internal. We basically just built
[00:00:59] every app internally instead.
[00:01:03] [Music]
[00:01:19] Welcome back to the show. Today I'm
[00:01:22] super excited for this one. We are
[00:01:24] joined by really one of the most elite
[00:01:26] vibe coders around. Our guest today is
[00:01:29] the founder and CEO of Lead Magic, Jesse
[00:01:32] Wlette. Lead Magic is an online
[00:01:34] platform. It takes your prospecting
[00:01:35] data, turns it into customers, giving
[00:01:38] you accurate emails, mobile numbers, and
[00:01:40] validating all of your data seamlessly.
[00:01:43] Jesse, welcome to the show, my friend.
[00:01:45] how you doing?
[00:01:47] >> Good chatting with you, man. Good to
[00:01:49] good to talk to you again, Pete.
[00:01:51] >> Absolutely. Okay, now Jesse, we know
[00:01:53] what we're going through today, but I
[00:01:55] want to uh give the audience a big
[00:01:58] context for what we're doing on this
[00:01:59] show.
[00:02:01] Today, Jesse is going to live vibe code
[00:02:05] a full SAS app, a full platform, and
[00:02:09] actually launch the thing. So, for folks
[00:02:12] who don't know what vibe coding is, if
[00:02:14] this is a new term to you, AI has given
[00:02:17] us the power to give text inputs and
[00:02:20] have all of these incredible outputs.
[00:02:22] I'm sure we've all made videos,
[00:02:24] pictures. Uh, I made a bunch of memes
[00:02:28] for my fantasy football team last week.
[00:02:30] That was a good time. You can really do
[00:02:31] anything with just this text input. Uh,
[00:02:34] and something incredibly valuable is,
[00:02:37] you know, text input to code output.
[00:02:40] Now, when I originally started doing
[00:02:42] text input to code output, Jesse, it was
[00:02:44] really just that HTML kind of stuff. I
[00:02:46] could make nice I could kind of turn a
[00:02:48] PDF into a nice web app. You're going
[00:02:50] way deeper than that. You're actually
[00:02:52] building functional SAS software with
[00:02:55] robust backends, admin panels, the whole
[00:02:58] bit. Uh, so that was the setup. Can you
[00:03:02] tell the folks what we're going to build
[00:03:04] today? What type of app is going to be
[00:03:05] built here? And Yeah.
[00:03:07] >> Yeah. Yeah. So, uh, so really when you
[00:03:11] think about it is the presentation layer
[00:03:13] of his applications when you have them,
[00:03:16] you you start to look at the, uh, like
[00:03:18] what comes out to the user. And really
[00:03:21] all of that is driven by APIs. And APIs
[00:03:26] can come from really a lot of places,
[00:03:27] right? Your web browser reads APIs and
[00:03:30] then renders the graphics. But what
[00:03:32] we're going to do today is one of the
[00:03:34] things that a lot of people uh sort of
[00:03:37] want to do is they use tools like
[00:03:39] Lovable. They use Bolt V0. I'll just
[00:03:42] show people how to use it with like
[00:03:43] Vzero just just for the simplicity of
[00:03:46] this thing today. But what what it is is
[00:03:49] you really want to be able to get uh you
[00:03:51] know so we we started with a prompt.
[00:03:52] We're building a champion tracker. uh
[00:03:55] there's a lot of tools out there that do
[00:03:56] this in the market and really it starts
[00:03:59] with uh you know an API that you're
[00:04:01] going to use to get the data and really
[00:04:05] what you do is you think about it this
[00:04:07] way you say all right I can make the
[00:04:08] presentation layer it's going to be some
[00:04:11] sort of uh sidebar so what I did is I
[00:04:14] came into the application and I said all
[00:04:16] right let's say I want to make a a
[00:04:18] sidebar SAS where you know we'll share
[00:04:21] this later but it's going to use an API
[00:04:23] that exists which is documented. So
[00:04:26] that's the best way to do it. Find one
[00:04:28] that's documented and then what you're
[00:04:30] going to do is you're going to say we're
[00:04:31] going to get it out of that API and then
[00:04:33] you're going to have statuses. You're
[00:04:35] going to display that to the user. So
[00:04:36] you're going to have that. Uh so I built
[00:04:40] the prompt for people. This is a oneshot
[00:04:42] sort of yellow type prompt. Uh yellow
[00:04:45] stands for you only live once kind of
[00:04:47] prompt. Uh developers might not like
[00:04:49] this, but it's sort of easier now,
[00:04:51] right? You can get these applications
[00:04:53] built pretty quickly, right?
[00:04:56] >> Yeah.
[00:04:57] >> Real quick, Jesse, could you shrink the
[00:04:59] width of your screen? It'll make the
[00:05:02] text bigger
[00:05:03] >> uh for the folks. That is beautiful.
[00:05:07] How's that everybody? Is that good? Um
[00:05:10] and so, and then just to so we have so
[00:05:13] we're we have this yolo prompt, this
[00:05:15] huge freaking prompt that you're going
[00:05:16] to put into Vzero. So chat GBT is not
[00:05:20] going to be doing the coding itself, but
[00:05:22] what you're doing with chat GBT is
[00:05:24] formulating this really really long
[00:05:26] prompt that would take probably forever
[00:05:29] and wouldn't be as clean for a another
[00:05:32] bot to understand. So we're like having
[00:05:34] one bot draftable prompt for another bot
[00:05:37] and this as you described as the YOLO
[00:05:39] prompt has everything. So what are the
[00:05:42] the main sort of things in here? We have
[00:05:43] the data and API integration.
[00:05:46] What else is in here?
[00:05:47] >> So you get So basically for the
[00:05:49] application, you know, and look, we took
[00:05:51] a pretty big chance here by doing this
[00:05:52] live. Of course, there could be bugs.
[00:05:54] We're not sure. That's why we want to
[00:05:56] keep you in suspense here. But basically
[00:05:58] what we're doing is we're building a an
[00:06:00] application on uh you know, some of the
[00:06:03] latest technologies that's out there.
[00:06:05] It's a champion tracker app. It's going
[00:06:07] to have a login screen, a dashboard. uh
[00:06:10] in there it's going to have sort of two
[00:06:12] uh it's going to have like a dashboard
[00:06:14] with a bunch of cards that are
[00:06:15] summarizing a watch list. Now what a
[00:06:18] watch list will be is that'll be your
[00:06:20] your standard uh like champions that
[00:06:22] you're watching. So some people have
[00:06:24] used like user jams or things like that.
[00:06:26] I mean they have a lot more in their
[00:06:28] platforms but this is similar to those
[00:06:29] types of technologies right uh you know
[00:06:32] they they kind of watch champions to see
[00:06:34] if they move companies. That's sort of
[00:06:36] the the mindset is is if your champion
[00:06:38] moves to another company, you might be
[00:06:40] able to sell them more technology.
[00:06:43] Um, so that's sort of where that goes.
[00:06:48] And then you're going to be able to add
[00:06:50] uh some champions to the the to the list
[00:06:54] and you give it the company name and
[00:06:56] you'll they'll know then you know where
[00:06:58] they've moved to.
[00:07:00] >> So
[00:07:02] Oh yeah, sorry. Continue.
[00:07:04] >> Yeah. So just that that's the dashboard
[00:07:06] side. So yeah, if you have any questions
[00:07:07] there, that'll be like what's on the
[00:07:09] dashboard.
[00:07:11] >> So what is the So and let's just connect
[00:07:13] this back to the original prompt. So the
[00:07:15] original prompt from you. So like you
[00:07:17] have a prompt and we'll we'll guys we'll
[00:07:20] find some way to give you this prompt
[00:07:21] after the show. Maybe we'll follow Jesse
[00:07:23] on LinkedIn and we'll we'll we'll
[00:07:24] promote it or something and we'll send
[00:07:26] it to you. But um let's connect this to
[00:07:28] the the smaller prompt that we're going
[00:07:32] to say prompt a billion times during
[00:07:33] this show. the smaller prompt generated
[00:07:36] this prompt which you're going to give
[00:07:38] to v 0ero. What was the line in the
[00:07:41] smaller prompt that sort of outlined
[00:07:43] that that was what you needed?
[00:07:45] >> Just I just put like a like build a
[00:07:47] vzero prompt and then gave it sort of
[00:07:49] the API information that I wanted to use
[00:07:51] and then sort of inspiration of where I
[00:07:55] wanted how I wanted to scaffold the the
[00:07:57] actual application. So it started
[00:08:00] >> there was a lot of invention from chat
[00:08:01] GPT here like it it really kind of
[00:08:04] >> Yeah. Yeah. Yeah, that's the key.
[00:08:05] >> Yeah.
[00:08:07] >> And this type of prompt, you could
[00:08:09] convert it to Bolt, you could convert it
[00:08:11] to Vzero, you could convert it to
[00:08:13] lovable or whatever technology system
[00:08:15] you wanted to, uh, you know, and build
[00:08:18] whatever app. And this is where I think
[00:08:20] it gets really interesting because
[00:08:21] really anybody can build an app as good
[00:08:23] as the ones that are out on the market
[00:08:25] today, right? uh there is security and
[00:08:28] there's some some other issues and I've
[00:08:31] tried to like mitigate a lot of that in
[00:08:33] this app but you know you'd want to uh
[00:08:36] security governance operation you want
[00:08:38] to be very careful there before you ship
[00:08:40] it like completely ship it but there's
[00:08:43] definitely services out there that could
[00:08:45] do that. So, if you're like in your
[00:08:46] career right now and you absolutely hate
[00:08:48] your job, you might want to think about
[00:08:51] um getting an MVP ready because, you
[00:08:54] know, I'm always like, you know,
[00:08:55] somebody's like, "Yeah, I'm thinking
[00:08:56] about an MVP." But like the more you
[00:08:57] think about these things, you could
[00:08:59] probably be already have revenue and
[00:09:00] you're coming in before you're even
[00:09:02] before you're even there. And I'll add
[00:09:04] to that Vzero and Chat GPT. I mean,
[00:09:07] granted the the beast versions of both
[00:09:09] systems you have to pay a little bit of
[00:09:11] money for. Although, granted, I think
[00:09:12] combined I pay like 40 bucks a month or
[00:09:14] something for Vzero and GPT, but like
[00:09:17] you can literally start doing that for
[00:09:18] free with no expertise. Jesse's a sales
[00:09:21] and marketing guy. I'm a sales and
[00:09:22] marketing guy. Granted, I can't build
[00:09:24] these apps the way Jesse does just yet.
[00:09:26] I'm too new at this, but uh it is it is
[00:09:29] incredibly empowering. Um, I'll continue
[00:09:31] to drop in the tools into the chat here.
[00:09:34] Um, just so you guys at home can uh can
[00:09:37] copy them down into sort of your short
[00:09:38] list of of things to explore. Um, and
[00:09:41] and so we're going to hop over to Vzero
[00:09:43] in just a second. Uh, for folks who
[00:09:45] maybe just joined, Jesse, can you just
[00:09:47] give a high level like very high level
[00:09:50] overview of of of the Champion Tracker?
[00:09:52] What is the overall value and sort of
[00:09:54] pitch of what this app does? the the
[00:09:57] pitch of the app is uh the this one
[00:10:00] right here what it does is it will check
[00:10:02] so if you have people that you want to
[00:10:03] keep an eye on your customers or or
[00:10:05] whatever the v V0 of the app right like
[00:10:09] that's the first version of it the MVP
[00:10:11] like that's what it stands for is going
[00:10:12] to be just like a dashboard and I
[00:10:15] started similarly the same way with my
[00:10:17] app where it was just an email
[00:10:19] validation which everybody does email
[00:10:22] validation right um but you know this is
[00:10:25] the starting point, right? Something
[00:10:26] that you're building on. So, dashboard
[00:10:28] when you got, you know, the person
[00:10:30] hasn't changed jobs. So, you submit what
[00:10:33] the theory is is you submit somebody's
[00:10:35] uh information to this. You submit like
[00:10:37] their their business information and
[00:10:38] then what happens on the other side of
[00:10:40] it is it detects if they've changed
[00:10:43] jobs,
[00:10:44] if they've never worked there or if
[00:10:47] there's no change, right? Like those are
[00:10:49] like the statuses, right? And then you
[00:10:52] could use this is just using an API to
[00:10:55] do that, right? Some of these APIs are
[00:10:57] through like they're in Clay now, but
[00:11:01] obviously Lead Magic has the APIs as
[00:11:03] well to do this, but there's other ways
[00:11:07] to, you know, there's a lot of APIs out
[00:11:09] there and that's the what ends up coming
[00:11:11] to the user, the presentation layer. So,
[00:11:13] it's wherever your mind could go with
[00:11:15] with this, right?
[00:11:16] >> Yeah. And for for the folks at home,
[00:11:18] just think of like what other things do
[00:11:20] I need to connect together because I
[00:11:23] mean shoot if you look at even your own
[00:11:25] SAS platforms. I mean think of how many
[00:11:27] things are connected together in order
[00:11:28] to just make that thing operate. Usually
[00:11:30] in almost every case it's not purely
[00:11:33] your own code you have to use. I mean
[00:11:36] look even if you're just using a payment
[00:11:38] processor like you still have to API
[00:11:40] things over. So, it's really a matter of
[00:11:41] like what outside functionality do I
[00:11:43] need that I can't build myself,
[00:11:45] >> looping that into your prompt, and then
[00:11:48] um really a lot of the heavy lifting um
[00:11:52] uh is is happened by the uh by by the
[00:11:54] bot. Um just a couple things in the
[00:11:56] chat. Laura says, "I'm a strategy girl
[00:11:58] and I've started the process of building
[00:11:59] my own app and chat GBT. It's
[00:12:01] overwhelming and liberating at the same
[00:12:02] time." I hear that. Other Laura said,
[00:12:05] "How do you handle bugs?" We will get to
[00:12:07] bugs. Let's get something buggy.
[00:12:09] >> We have one now actually. So, we got
[00:12:10] some suspense here actually. Uh,
[00:12:14] >> but yeah, we'll get there. Um, this is
[00:12:16] funny. It's kind of happening, but uh
[00:12:19] but yeah, so you know, you we'll keep
[00:12:21] going through it. And then like the UI
[00:12:23] components,
[00:12:25] uh, you know, there's a lot of places
[00:12:26] for the UI components to come now. Like
[00:12:28] one one UI component package that a lot
[00:12:30] of people use is, uh, Shad CN, which is,
[00:12:33] um, you know, there's a lot of different
[00:12:37] dashboards in here and stuff. So you can
[00:12:39] you can sort of do these and yeah it's
[00:12:42] starting to get to the point where all
[00:12:43] of these applications are looking very
[00:12:45] similar now right because they're using
[00:12:46] a lot of the same building blocks but
[00:12:49] you can open these uh you know inside
[00:12:52] VZero to like use them right and that
[00:12:55] allows you to get a lot more out of you
[00:12:59] know your your investment there so you
[00:13:00] don't have to you know the components
[00:13:02] are really built already right uh you
[00:13:05] might make some tweaks to the colors and
[00:13:07] things like that but don't So, don't go
[00:13:09] hiring like a um a lot of people would
[00:13:11] hire like a designer or something. Like
[00:13:13] a lot of that stuff is gone, right? It's
[00:13:15] not really the um the world anymore,
[00:13:18] right?
[00:13:19] >> Even to the point where like you can
[00:13:20] have this app. I don't know if everybody
[00:13:22] in here knows this. Um but you could h
[00:13:25] like let's say Jesse has the app fully
[00:13:27] built. You could literally screenshot
[00:13:29] let's say I built an app. I could
[00:13:31] screenshot if I really love Lead Magic's
[00:13:33] you know interface which is a great
[00:13:35] interface. I could just screenshot them
[00:13:36] and be like, "Make it look more like
[00:13:38] lead magic and it would totally recode
[00:13:40] it to to look like that." So, it's like
[00:13:43] you just have to know what you want uh
[00:13:45] for the most part. Um and it will it'll
[00:13:48] spit it out. Now, there's some questions
[00:13:49] on bugs in the in the chat here. So, um
[00:13:53] Caitlyn said, "I've been I've been
[00:13:54] vibing Cody on Lovable and the dashboard
[00:13:57] looked incredible, but the functionality
[00:13:59] was terrible." Uh she says it literally
[00:14:02] did not work at all. Uh and I saw a
[00:14:04] couple of other thing Nisha said I have
[00:14:06] versile cursor lovable rilet uh she you
[00:14:09] know Nisha just doesn't know what to use
[00:14:11] for which one. So just in the world of
[00:14:13] actually like you know getting something
[00:14:17] for for the beginners getting something
[00:14:19] that's functional and not just a
[00:14:20] beautiful dashboard. Are there certain
[00:14:22] things that you use you know systems you
[00:14:25] use to I guess
[00:14:26] >> uh yeah one of the ones that I so if
[00:14:30] that's happening typically it's about
[00:14:32] how you plan the application in the
[00:14:34] beginning uh and how you use the rules.
[00:14:37] So if for the new the newest users I
[00:14:40] would start with something like a
[00:14:41] lovable or bolt or vzero right or replet
[00:14:46] like more of a less about the code more
[00:14:48] about the uh actual how the UI UX looks
[00:14:52] on the presentation layer but what's
[00:14:56] going to happen is you're going to need
[00:14:57] to get some functionality so you're
[00:14:58] going to need to access like APIs and
[00:15:00] you're going to need to access other
[00:15:01] things. That's the part where it gets a
[00:15:04] little tricky where you might need
[00:15:05] somebody that's done it a few times
[00:15:07] before. Uh, you know, and that is where
[00:15:11] the the problem comes. It's it's usually
[00:15:13] the two areas that people have a problem
[00:15:15] with is like the security like the
[00:15:17] authentication and and the um
[00:15:21] like getting through that is a little
[00:15:24] bit hard, right? And then the other one
[00:15:26] is like operations like does it get all
[00:15:29] of the data where you need it? Does it
[00:15:31] not look right? And that's where you may
[00:15:34] want to pay like what h what's the best
[00:15:37] way to do that is to to possibly hire
[00:15:40] somebody to wing with, you know, a wing
[00:15:42] person with you that is actually a
[00:15:43] developer that could actually help you
[00:15:46] fix that problem, right? Like that's
[00:15:48] where you got where you got to jump off
[00:15:50] a little bit and get some help is around
[00:15:53] um when you're building like when you're
[00:15:55] making API calls and you're moving data
[00:15:57] into a database. That's like the that
[00:15:59] would be the part that I would say you'd
[00:16:01] want to uh start to get people to help
[00:16:02] you.
[00:16:03] >> Yeah. And I I think that's a huge
[00:16:05] developer skill. Like when we think of
[00:16:07] developers, we think of people that type
[00:16:08] code. We're like, yes, for sure. But
[00:16:11] like the knowledge of how to structure
[00:16:14] architecture and and how to like
[00:16:16] structure an application and like that
[00:16:19] is also very much within the developer
[00:16:22] skill set and less so for I mean less so
[00:16:26] virtually non-existent in the beginning
[00:16:28] for a sales and marketing person like
[00:16:30] myself. Um, and and I'll also just note
[00:16:33] Vladen made a great point in the in the
[00:16:35] chat says can't be a doctor overnight. A
[00:16:37] lot of these apps you can just start by
[00:16:39] building something super basic, which I
[00:16:40] encourage everybody to do. Start by
[00:16:42] turning a PDF like a like a blog post
[00:16:44] into like some sort of interactive app
[00:16:47] that's just a single page, something
[00:16:49] super super simple. And um and from
[00:16:52] there you can start, you know, uh
[00:16:55] working your way up. Again, Jesse is
[00:16:57] elite at this. So, um, you're watching a
[00:17:01] a a CTO of Vibe Coding in action.
[00:17:05] >> I was doing a lot of copy pasting before
[00:17:07] the tools are out. That was like the big
[00:17:08] uh where I learned because like I was
[00:17:11] running an agency and then uh I got a
[00:17:13] little bit uh tired of it just because
[00:17:15] of the um the demand the customer like
[00:17:19] demand of anybody who runs an agency
[00:17:22] knows what I'm talking about. So, uh you
[00:17:24] know, I wanted to go SAS. Now, it has
[00:17:25] its pros and cons, but um you know,
[00:17:26] we've got we're doing pretty well from a
[00:17:28] customer perspective. Bootstrapped. I
[00:17:31] think a lot of bootstrappers will come
[00:17:32] out of these agencies because they run
[00:17:34] pretty efficient lean go to market. But,
[00:17:37] you know, if there's an idea that I'm
[00:17:38] thinking about, I just like start start
[00:17:40] thinking about how do I prepare this?
[00:17:42] One site I've used a lot uh for
[00:17:45] preparing, it's called code guide. Uh, I
[00:17:47] I don't know this guy, so I'm not like
[00:17:49] invested in it. But this one's pretty
[00:17:51] good for figuring out how to like
[00:17:55] there's a a lot more of these people are
[00:17:56] on Twitter or X or whatever. Uh, if you
[00:17:59] want to see like some people that talk
[00:18:00] about this a lot, but this allows you to
[00:18:03] build the prompts that build the
[00:18:04] prompts. So, this one's a good This was
[00:18:07] one of the sites I used in the beginning
[00:18:08] uh just to learn how to like really
[00:18:11] there's certain uh things you want to
[00:18:13] plan out before you build the app. And
[00:18:15] this gives you a good like English to
[00:18:20] app, right? Um, so if you want to build,
[00:18:23] you know, like what do I want to build?
[00:18:24] This gives you a way to prompt out of
[00:18:27] the like what you actually want in the
[00:18:29] in VZero or Lovable or those those
[00:18:34] applications.
[00:18:35] >> Yeah. And Joe dropped into the chat,
[00:18:37] too. He says, "If you're constantly
[00:18:38] rebuilding, you're doing it wrong." I
[00:18:40] think that's like a huge highlight of of
[00:18:41] exactly what you're going through now
[00:18:43] with code guide is like how much how
[00:18:47] well can we structure exactly what we
[00:18:50] need off the bat because what happens is
[00:18:53] you go through like the first few
[00:18:55] versions usually and I'm I'm really
[00:18:57] thinking about Vzero here and I've had
[00:18:59] this happen with Gemini and GPT as well
[00:19:02] where it starts to just like it starts
[00:19:05] to slowly morph and not be exactly the
[00:19:08] same as it was before and sort of go
[00:19:10] into a mind of its own. I don't know if
[00:19:12] anybody has seen uh those like like
[00:19:16] time-lapse videos on like on on whatever
[00:19:19] Reddit or Instagram or wherever you you
[00:19:20] have videos where it's like you're
[00:19:22] asking an AI bot to replicate a picture
[00:19:24] a 100 times over and then it like slowly
[00:19:26] turns into this just this nonsense. So
[00:19:30] um anyway, all of that tangent just to
[00:19:32] just to elaborate on like the importance
[00:19:35] of that initial prompt being robust,
[00:19:38] being thorough, really spelling out
[00:19:41] exactly what the functionality and
[00:19:42] architecture be will be. That way that
[00:19:44] V1 of the app does not need this crazy
[00:19:47] rebuilding because from there it just
[00:19:50] gets tougher.
[00:19:53] >> Okay.
[00:19:53] >> Yeah. You know, you made a lot of good
[00:19:55] points there. It's like you can you can
[00:19:56] get down a rabbit hole pretty quickly,
[00:19:58] but every time I got down the rabbit
[00:20:01] hole, eventually what happened is I
[00:20:02] started to figure out like what was
[00:20:04] going on. Uh and the best way to figure
[00:20:06] out how to get out of the jam is to
[00:20:09] uh to just do uh just use AI again to to
[00:20:12] get to really get out of it. Uh you
[00:20:14] might have to use some of the newer the
[00:20:16] thinking model. Uh you know, that that
[00:20:19] really helps a lot. Um, you know, Claude
[00:20:21] is is really good for this for for just
[00:20:24] getting yourself out of the jam of like
[00:20:26] there's a bug and I don't know how to
[00:20:27] fix it or you know, look, there's always
[00:20:29] a time to ask for help. And I know
[00:20:31] there's a lot of different groups that
[00:20:32] are forming communities, whatnot that
[00:20:34] are doing this. And I start to see like
[00:20:37] the the advantage sales and marketing
[00:20:39] people have if they're if you're if
[00:20:41] you're coming from sales and marketing
[00:20:42] or you run an agency now, you're going
[00:20:44] to know better what the app should feel
[00:20:46] like than probably somebody who is just
[00:20:49] coming into a cold that's building it on
[00:20:51] a development level
[00:20:53] >> like that that knowledge of you using it
[00:20:56] and you know that's I build sales
[00:20:59] marketing tools but I used them for so
[00:21:02] long you know in my career that it
[00:21:04] really changed like I knew exactly what
[00:21:07] I wanted. It wasn't like it it wasn't up
[00:21:09] for debate. I mean, I followed that
[00:21:10] pretty closely.
[00:21:11] >> Okay, so where So, we have the prompt.
[00:21:13] We have the prompt that created the
[00:21:15] prompt, guys. We will give that away.
[00:21:16] Um, again, we'll we'll drop in LinkedIn.
[00:21:19] Jesse will post it on LinkedIn. I'll put
[00:21:20] his I'll put his I'll put his uh profile
[00:21:23] in the chat here. Um, I'll probably
[00:21:25] share it as well so you can follow me if
[00:21:27] you don't already. Uh, but here, let me
[00:21:29] drop Jesse's thing in here. And if
[00:21:31] you're watching on YouTube, Jesse's
[00:21:33] LinkedIn is in the description. Um,
[00:21:37] okay. So, we have the prompt. This thing
[00:21:39] has just been churning out code.
[00:21:42] >> It's turnurning out some code here,
[00:21:44] right? What I did is I gave it the
[00:21:46] prompt up here, right? More of a
[00:21:48] champion tracker. First thing it had me
[00:21:50] do was set up the database, of course.
[00:21:53] Uh, you know, that gets set up and then
[00:21:55] we're in, right? And then, um, let's see
[00:21:59] here. Right. These are the types of bugs
[00:22:02] that you can have, right? You'll have
[00:22:03] like it doesn't redirect. This is what I
[00:22:06] wanted to show people. Like it won't
[00:22:08] redirect you or or something like that.
[00:22:10] Those are the essentially the types of
[00:22:12] bugs that you can start to have. But
[00:22:14] what I'm doing is I'm publishing it in
[00:22:16] Versel, right? and uh you know I'll give
[00:22:19] it a domain name
[00:22:22] and then uh then basically you know
[00:22:25] it'll have that and then what that will
[00:22:27] do is it'll put it in and and if you're
[00:22:30] not like following this right now
[00:22:31] there's probably more to it. The goal
[00:22:32] was just to start talking about this but
[00:22:34] then it puts it inside your Verscell and
[00:22:37] it starts this is where it's hosting it.
[00:22:39] So you're now hosting it inside here. Uh
[00:22:42] and what we did also is we hooked up a
[00:22:44] database. So it's now got a database
[00:22:47] hooked up to it. Neon, which is good.
[00:22:49] There's two databases most people are
[00:22:51] using right now. Superbase and uh Neon
[00:22:54] are the two. And what we did is we've
[00:22:57] also got environmental variables. These
[00:22:59] are the secret kind of components of the
[00:23:01] application for um for basically for uh
[00:23:06] for dealing with like authentication and
[00:23:09] all that. So you want to it's better to
[00:23:11] use just like if you're beginning you
[00:23:12] should just use it like right out of the
[00:23:14] gate. use their their setup
[00:23:18] um so if you're using so sorry just to
[00:23:21] clarify for the audience so if you're
[00:23:23] using Vzero Vzero is a application under
[00:23:27] Versell you can host you can so like you
[00:23:30] can deploy let's say I make a a a web
[00:23:34] app I was talking earlier about turning
[00:23:36] PDFs into web apps using Vzero
[00:23:40] um you can actually you know what I'll
[00:23:42] do I'm going to make this week's cheat
[00:23:43] sheet uh an interactive app. That's what
[00:23:45] I'll do. I'll post it on LinkedIn
[00:23:46] tomorrow. I'll make it in an active app
[00:23:48] so people can see what I'm talking
[00:23:49] about. But it's all hosted on Vzero and
[00:23:52] Versal. So like I don't it just totally
[00:23:55] simplifies. You know, Jesse's obviously
[00:23:57] an expert and he's hopping between these
[00:23:58] different things. But um starting out
[00:24:00] with with with very simple builds um and
[00:24:03] just deploying it exactly right there on
[00:24:06] the top right through publish. Uh and
[00:24:08] now you can see if you look at the
[00:24:10] address crash right in the app,
[00:24:14] >> right? And that's what will happen to
[00:24:15] many of you when you're when you're
[00:24:16] doing this that this will basically uh
[00:24:20] you go into here and now you're in um
[00:24:23] now you can see your database. So you
[00:24:25] can you can actually see what it what it
[00:24:27] did is it actually created the database.
[00:24:31] So, uh, it created the users, that's for
[00:24:33] logging in or whatever. And then it
[00:24:35] created, um, who you're watching. So,
[00:24:38] this would be like who you're watching
[00:24:40] and and you know what would be that, but
[00:24:43] that would be what the user would
[00:24:45] submit, right? So, the user would submit
[00:24:47] to here uh, in the application when we
[00:24:51] finally get into it, right? So, we're
[00:24:53] building it and this is probably where
[00:24:54] some of the other people have gone, but
[00:24:56] um, you know, with this application. So,
[00:24:59] as it's building here, you're seeing
[00:25:01] that um you're you're seeing that it's
[00:25:03] still struggling to get to like the
[00:25:05] authentication part, which that's that's
[00:25:08] why we're building some suspense here.
[00:25:09] But, um you know, we uh we're building
[00:25:14] we're building on that. And then if you
[00:25:16] continue down the path of this, what
[00:25:18] you're going to end up having is you'll
[00:25:20] you'll be able to grab, you know, so if
[00:25:22] you want to if we want to go to the um
[00:25:24] if we want to just start out here with
[00:25:26] like without the authentication while
[00:25:28] it's loading, uh SAS tracking
[00:25:32] um employees
[00:25:36] employees and then you give it a um then
[00:25:39] you would just give it the uh what it
[00:25:43] would what what the what it would come
[00:25:45] back from the uh API and that's really
[00:25:48] what you want to do. So basically
[00:25:50] >> and sorry what was that thing you
[00:25:52] pasted? What was that? What was
[00:25:54] >> that's just the return response from the
[00:25:56] um from like what comes through the API
[00:25:59] basically.
[00:26:01] >> So what it'll do is it'll you know you
[00:26:04] can you can make the text can you do the
[00:26:06] zoom in text thing again?
[00:26:08] >> Yes. On the on what which one?
[00:26:11] >> Uh is there a way to like Oh sharing
[00:26:13] your whole screen right now. I see. I
[00:26:15] see
[00:26:16] >> this this one, right?
[00:26:18] >> Yeah. Is there like a way to just do the
[00:26:19] whole um like zoom in the whole uh
[00:26:23] browser like do 150% of the browser?
[00:26:27] >> Yeah. Yeah. Oh. Oh, I got it. There you
[00:26:30] go.
[00:26:31] >> Yeah. Yes. Yes. Yes.
[00:26:33] >> Yeah. So you'll be you'll be doing that
[00:26:34] and then you know the things you need to
[00:26:36] set up with it would be authentication a
[00:26:38] database
[00:26:40] and uh you know this the sidebar of
[00:26:43] whatever is going to be in the
[00:26:44] application and then some feed or some
[00:26:46] sort for for API to get to get the APIs
[00:26:50] out of it. Now if you go on there's a
[00:26:52] lot of public APIs. That's the key is
[00:26:54] that um you'll you'll come up with a lot
[00:26:58] of these like public sort of APIs. Now
[00:27:00] you're going to get to see what it looks
[00:27:02] like to have a um like what what
[00:27:05] actually comes into the application. You
[00:27:08] can pick your your sidebar. You can pick
[00:27:11] all of that when it starts. You'll see
[00:27:13] it load up on the screen. So now it's
[00:27:15] it's here. Let's just see um what it
[00:27:19] looks like. It'll load up.
[00:27:21] >> Yeah. There we go. All right.
[00:27:22] >> Right.
[00:27:25] >> So you have that and you know now you're
[00:27:28] building. It's going to go through all
[00:27:29] the tasks. I got it on advanced mode
[00:27:30] here. So, you're just doing building the
[00:27:32] employee over overview, creating the job
[00:27:35] alerts, adding tenure analytics,
[00:27:38] building employee profiles. So, it's
[00:27:41] going to do all of that and then what's
[00:27:43] going to happen is uh you're going to
[00:27:45] get you're going to get an application
[00:27:47] out of it, right? So, it's it's it's
[00:27:49] just takes a little bit of time, but
[00:27:51] it's that was like the whole purpose of
[00:27:52] the show here today, just to keep you in
[00:27:54] suspense.
[00:27:55] Now, Jesse too, I also want to highlight
[00:27:58] um there's there's definitely people we
[00:28:01] have a couple hundred people in here.
[00:28:03] >> There's definitely people who are
[00:28:04] looking at this and probably feeling a
[00:28:05] little overwhelmed like, "Wow, that's
[00:28:06] empowering. If I could do that because
[00:28:08] I'm not a developer, but there's a lot
[00:28:10] going on here." And there is a lot going
[00:28:12] on here. You've been doing this for a
[00:28:14] while. So, someone said, "Hey, it looks
[00:28:16] like I should just hire a developer."
[00:28:18] What would you say to that? Not just the
[00:28:20] developer, but
[00:28:22] >> you you pro you you definitely need
[00:28:23] hire. you probably like this is it's
[00:28:25] there's a another type of way to hire
[00:28:27] developers now, right? The old way you
[00:28:29] would just hire developers and um you
[00:28:32] know you could have that mindset like of
[00:28:33] just hiring developers but like if
[00:28:36] you're building a profitable company and
[00:28:38] you don't like I I didn't have enough
[00:28:40] money like for me I didn't have enough
[00:28:41] money to hire um and I didn't really I
[00:28:44] didn't want to raise I worked for
[00:28:45] companies that were venturebacked and I
[00:28:47] disliked it with passion so I wanted to
[00:28:50] build it myself. Now, what you can
[00:28:52] definitely do is you can hire a
[00:28:54] different uh like cost of a developer,
[00:28:58] right? You you you're probably not
[00:29:00] hiring the developer that's at Google uh
[00:29:03] you know, like an architect at Google.
[00:29:06] You're probably hiring maybe somebody
[00:29:08] who's uh maybe a gig worker or something
[00:29:10] like that that can help you sort of
[00:29:12] publish the app and they can grow with
[00:29:14] you, right? But you're not what what
[00:29:17] people do is they'll spend like
[00:29:19] thousands of dollars on these MVP apps
[00:29:21] from these companies and then they just
[00:29:24] they ship at the end of it and nothing
[00:29:25] they get nothing out of it because they
[00:29:26] don't and they don't really know how it
[00:29:28] works. They don't know if they're
[00:29:28] getting the right stuff. Like it becomes
[00:29:31] pretty
[00:29:33] uh pretty much a waste of time, right?
[00:29:36] >> You know, you could just take that
[00:29:37] mindset of hiring developers, but like
[00:29:39] do you have you don't have money? That's
[00:29:41] hard.
[00:29:42] I would say too, Jesse, like the way to
[00:29:45] sus that out too. Like I mean hiring
[00:29:47] somebody who really uses these tools um
[00:29:50] is
[00:29:51] I mean I think going to get you'll
[00:29:53] basically get like a team of four, you
[00:29:55] know, for the price of one. And I think
[00:29:57] a good way, you know, while you're while
[00:29:59] you're interviewing and and searching
[00:30:01] for uh for developers, like Jesse's
[00:30:04] built a ton of backend stuff for just
[00:30:06] just tools internally for lead magic,
[00:30:09] just stuff for him to use. And when I
[00:30:12] when Jesse has shown me those apps or I
[00:30:15] mean even what we're looking at right
[00:30:16] now and he's doing it live like this is
[00:30:19] another one this lead magic command
[00:30:21] center took me like a day probably uh to
[00:30:24] build basically I just wanted to track
[00:30:25] every time somebody mentioned our
[00:30:27] company uh on LinkedIn. So I just built
[00:30:30] this basically and this was all a vibe
[00:30:33] code, right? I would just add. So what
[00:30:35] we're we look for is like okay, are they
[00:30:37] a partner? Are they more of a
[00:30:39] competitor? Like what's like what's the
[00:30:41] mentions? And now I could ship this app
[00:30:44] and probably charge people for it. They
[00:30:45] would probably buy it because it's
[00:30:46] valuable and it updates every day. But
[00:30:49] like this took me like a day to build
[00:30:50] now. Um, and you know, I would say this
[00:30:53] is on par with any sort of SAS
[00:30:55] application that's out there from a um,
[00:30:58] you know, just looking at it. But this
[00:31:00] what I want to track is like are they
[00:31:02] talking about us?
[00:31:04] What are they saying about our company?
[00:31:06] You know, we get a lot of uh, inbound
[00:31:08] leads just because people mention us.
[00:31:10] But this is like an internal application
[00:31:12] for our company, right? And we have a
[00:31:15] CRM that's internal. We we basically
[00:31:17] just built every app internally instead
[00:31:19] of uh you know
[00:31:22] >> this listening tool is crazy because a
[00:31:24] lot of um I mean the commercialized
[00:31:28] social listening tools for LinkedIn are
[00:31:30] really really spotty. Uh and I've I've
[00:31:34] worked with yours, Jesse. It is not it's
[00:31:36] like crazy accurate. Is that like is
[00:31:40] that because you're not commercializing
[00:31:41] it and you get the advantage of like
[00:31:43] them not knowing about you or like maybe
[00:31:46] your um the rate at which you're you I
[00:31:50] mean because you're really more or ley
[00:31:52] >> is the best out there. The only thing I
[00:31:53] wanted though is I wanted and I'm uh you
[00:31:55] know the reason I'm obviously not even
[00:31:58] doing the uh triggery is is probably the
[00:32:01] best one out there but my focus was only
[00:32:03] on my company. So it was like I don't
[00:32:05] really care and I want to plug it into
[00:32:07] like some of the other data that we
[00:32:10] already have. Like it just helps us
[00:32:13] figure out like hey are people talking
[00:32:14] about our product or like what's going
[00:32:16] on there right? Um,
[00:32:19] >> especially great if you were running an
[00:32:20] influencer campaign or some sort of user
[00:32:23] generated content campaign. Uh, I mean
[00:32:26] that especially on LinkedIn, LinkedIn is
[00:32:29] incredibly tough to dig uh, insights out
[00:32:32] of. Uh, they're they they keep it they
[00:32:35] keep as much behind the curtain as they
[00:32:36] can, which is a lot. And
[00:32:38] >> yeah, you just got to figure that part
[00:32:39] out. Uh then here I'm just going to add
[00:32:41] um add a way add a data table which we
[00:32:47] can add users to from their business
[00:32:51] profile like this and use this API. So
[00:32:55] then you would just have that go in
[00:32:56] there. We let that build and then you
[00:32:59] know but I'll let that build. I just
[00:33:01] want to make sure that builds and then
[00:33:02] you know what basically you can do is
[00:33:05] sort of use this um you know use this to
[00:33:10] figure out what uh actually is going to
[00:33:12] happen and then you can you know you
[00:33:14] could build an employee tracker SAS
[00:33:16] product pretty quickly right and it
[00:33:17] might might even be better than some of
[00:33:19] the ones that are out there because
[00:33:20] you're not using uh the same you know
[00:33:22] this is like the most modern versions of
[00:33:25] all of the tools and hosting providers
[00:33:28] so it's pretty it's pretty solid and you
[00:33:30] I just think getting an MVP out faster
[00:33:33] is better and getting people to try it,
[00:33:36] use it, you'll get to a point where you
[00:33:38] can be good at this. Uh it's it took a
[00:33:41] little bit of time, but it but it it's
[00:33:42] all I do now. Like I don't I don't take
[00:33:45] Zoom calls. I'm not like talking to
[00:33:46] customers every day anymore. I'm just
[00:33:48] doing this now. So everything I do is
[00:33:51] this with Lead Magic. Like I don't not
[00:33:53] doing anything else. So um
[00:33:55] >> which is incredible. And it's V V0 uh
[00:33:58] really is your main tool when it comes
[00:34:01] to actually
[00:34:04] legit
[00:34:06] >> curs if I had to say what I use the most
[00:34:08] it's cursor. So cursor is like it's
[00:34:11] basically you know like where developers
[00:34:12] usually use visual uh studio it's visual
[00:34:15] studio but it's like it's got the
[00:34:18] chatbot chatbot implemented into it
[00:34:20] because but this gets a little this is
[00:34:23] probably a little too much for somebody
[00:34:24] in the beginning. So, you know, you
[00:34:26] stick back to this. So, then you can um
[00:34:30] you know, do that, right? That's the
[00:34:32] that's the the trick there, right? So,
[00:34:36] you know, if we're going to add an
[00:34:37] employee, um we just, you know, see like
[00:34:41] you could add this sort of like employee
[00:34:44] tracker, things are going to not work
[00:34:46] right away. So, the the add employee
[00:34:50] button doesn't work. So, fix it. So it
[00:34:53] store or get the data from the API and
[00:34:58] then you know you can integrate as many
[00:35:00] APIs into these applications as you want
[00:35:02] and that's sort of the you know the way
[00:35:05] to do it and then you then you own the
[00:35:08] code too right like it's not you're not
[00:35:10] using another application you don't have
[00:35:12] any cost associated with this code right
[00:35:15] like this code is yours and you can do
[00:35:17] whatever you want with it right it's all
[00:35:18] right here so there's no IP you're
[00:35:22] losing you own it all. Uh, you know, you
[00:35:25] can do a lot with this.
[00:35:26] >> Download all that. You can just download
[00:35:27] it into one big zip file and send it
[00:35:29] over to some I mean it's it's uh it's
[00:35:32] >> yeah, you put it in GitHub would be the
[00:35:34] best way to do it and then you put it in
[00:35:36] GitHub and then now you're using it. Um,
[00:35:39] and what's what happens is these
[00:35:42] applications you you probably only what
[00:35:44] I would do is start very small like only
[00:35:47] build one thing for one person, right?
[00:35:49] Like you hear this all the time, but
[00:35:50] when you go wide and you come up with
[00:35:52] all these idea, like just build
[00:35:53] something simple that kind of fits your
[00:35:55] current brand or your agency or
[00:35:58] something you know how to do well,
[00:36:00] that's the key. If you can focus there
[00:36:02] and not like people try to bake it all
[00:36:06] into one right away and it just it gets
[00:36:09] really painful. Um
[00:36:11] you know like you just won't be
[00:36:13] successful if you try to do that. I
[00:36:14] started with just email validation.
[00:36:18] now on the Okay. So, like let's let's
[00:36:20] take that that idea of of building it
[00:36:24] kind of bit by bit and just
[00:36:27] contextualize that using the screen
[00:36:28] we're already looking at. Okay. So, we
[00:36:31] have um so we have these different
[00:36:33] functions. We have tenure analytics, job
[00:36:35] changes, let's say employee overview and
[00:36:37] job changes. So, let's say there was a
[00:36:39] bug with job changes and you really had
[00:36:42] to go deeper into kind of debugging
[00:36:44] that. Hey, do you ever find yourself in
[00:36:47] these like uh broken loops essentially
[00:36:50] with the bot? I've done that with V0ero.
[00:36:52] It's like fix with V 0. I click it, it
[00:36:55] spits out another version and then it's
[00:36:57] like broken fixed with V0 and I'm just
[00:36:59] in that loop and then it's almost like
[00:37:01] that that bulk code that I'm trying to
[00:37:04] work on is less usable because it just
[00:37:07] keeps rewriting this thing and not
[00:37:09] really fixing anything.
[00:37:10] >> Uh yes, that happens all the time. And
[00:37:12] best way, one of the best ways to solve
[00:37:14] that uh which is uh I'll show it to sort
[00:37:19] of show you. But one of the best ways
[00:37:20] that's when you start if you really want
[00:37:22] to um you know unless you understand the
[00:37:23] code or whatever I mean at this point
[00:37:25] it's easier now for me. But what you can
[00:37:28] do when you get into that that rut right
[00:37:30] there is, you know, at a very high
[00:37:32] level, you can go and just start a um c
[00:37:37] you can put it into um the best way to
[00:37:40] do that is to probably put it into
[00:37:42] GitHub. Now, it's like kind of free in
[00:37:46] the sense that it can be used in other
[00:37:49] tools. So, what I would do here now is
[00:37:52] um you know, I go into cursor, right?
[00:37:55] Cursor is an IDE. So it's like a little
[00:37:57] bit more technical, a little bit more it
[00:38:00] can connect to it a little bit easier. I
[00:38:02] would clone it in cursor, right? And
[00:38:04] then um then I would have that. Now what
[00:38:07] I would be able to do is
[00:38:10] uh I would be able to open it in cursor
[00:38:12] because I pushed it over here. So now
[00:38:15] you can see the whole codebase. This is
[00:38:17] kind of going now. The good thing the
[00:38:19] fun thing to do is have like five of
[00:38:20] these up at once just like letting you
[00:38:23] know like like letting it go that way.
[00:38:25] But um um you know so now it's in cursor
[00:38:28] it's here. So then you can go in here
[00:38:30] and you could say go through the
[00:38:32] application
[00:38:34] and find the areas where it isn't uh
[00:38:38] where there are bugs. Right now this
[00:38:42] helps a lot of people get out of the
[00:38:43] vzero loops or like lovable loops. And
[00:38:46] what you're doing is you're you're
[00:38:48] basically I put it on ask mode. I don't
[00:38:50] want it to control anything. There's a
[00:38:51] little bit of a difference between ask
[00:38:53] and agent, but essentially what you're
[00:38:55] doing here is you're just like asking it
[00:38:57] what's going on with the code that will
[00:39:00] help you get out of a lot of those jams.
[00:39:02] Right? So,
[00:39:04] >> so that thing of like parsing out
[00:39:07] through GitHub. So, you have you so
[00:39:11] let's just go through the whole process
[00:39:12] kind of from where we started just as a
[00:39:14] as kind of a midway recap. So, we have
[00:39:16] our initial prompt. Again, we'll share
[00:39:18] that with you. That initial prompt spits
[00:39:21] out this more or less this yolo prompt.
[00:39:24] This really long thing that has all the
[00:39:26] architecture and stuff lined out and
[00:39:28] functionality. That way we can put it
[00:39:30] into v 0. V 0 then is spitting out the
[00:39:34] whole thing in one long run. From there,
[00:39:37] once you have all of this, you you can
[00:39:39] you can flip over from the uh the u the
[00:39:42] preview to the code section. you can
[00:39:44] download the full code and it'll have
[00:39:47] all of the little functionality areas.
[00:39:49] So in this case it would have you know
[00:39:51] your employee overview and your you know
[00:39:53] your job changes and things like that to
[00:39:56] debug put it into GitHub and then you
[00:39:59] can start debugging still with text
[00:40:01] prompts. You're just dropping that
[00:40:03] folder of code into here and saying hey
[00:40:08] I'm experiencing this error. You can
[00:40:10] copy and paste the error that you got
[00:40:11] from wherever it was v0ero cursor and
[00:40:14] then have it just fix that specific
[00:40:16] thing. Um, so there's a lot of um
[00:40:21] uh there's there's yeah some things to
[00:40:23] look out for. Again, this is an advanced
[00:40:25] version. The goal here is to show
[00:40:27] everyone the capabilities uh not just
[00:40:31] hey, here's how you can uh nail a
[00:40:33] working app immediately after this call.
[00:40:35] >> Yeah. So the goal so basically what you
[00:40:37] what you found is like there are bugs
[00:40:39] that that have been sort of pushed in
[00:40:41] through here. But what what I think the
[00:40:44] key is is if you get your if you really
[00:40:46] focus on prompting before you send it
[00:40:49] over here getting an MVP of what you
[00:40:52] want the app to look like don't you know
[00:40:55] doing all of that then you're probably
[00:40:57] only you really don't understand you're
[00:40:59] very close to being able to ship that
[00:41:01] application.
[00:41:03] The hard part is probably the harder
[00:41:05] part before was this part of it, right?
[00:41:08] Like this part of it changed quite a
[00:41:10] bit. Now, are there still little
[00:41:12] interaction bugs when you start tying in
[00:41:14] databases and things like that? Yes.
[00:41:16] Authentication usually is a problem. Uh
[00:41:18] the other stuff that's a problem is the
[00:41:19] database like starting it, seeking it,
[00:41:22] you know, doing that stuff like that
[00:41:23] stuff's usually pretty hard. But uh that
[00:41:26] that's where so people are, you know,
[00:41:28] part of this was to show limitations. So
[00:41:30] where you probably want to stop is like
[00:41:32] get this part done first, right? Like
[00:41:34] figure out exactly how you want this to
[00:41:36] look with sample data. Do that and then
[00:41:40] start to incorporate some of the APIs
[00:41:42] that are out there that you could put
[00:41:44] inside your application, right? Whatever
[00:41:46] you want that interaction to be. Try to
[00:41:48] implement them. But I'll tell you,
[00:41:49] that's where you're probably going to
[00:41:50] get stuck first is that part right
[00:41:53] there. And that's also a good spot where
[00:41:55] security will become an issue. So,
[00:41:57] you're probably going to want to be
[00:41:58] careful there, too. Uh, so that's why
[00:42:01] but getting this part done first should
[00:42:03] be pretty easy with any of the tools
[00:42:05] that are out there, right? I think
[00:42:07] that's the way what I was trying to get
[00:42:09] at with people is like start to get the
[00:42:12] application to look like this or
[00:42:14] whatever. Then go from here, figure out
[00:42:17] how you want that to look, then go find
[00:42:19] the data where you need it and find uh,
[00:42:22] you know, that that might be where you
[00:42:23] need a developer.
[00:42:26] >> Yeah. And and and I think just this like
[00:42:28] you know what you were showing before of
[00:42:30] like just take one functionality at a
[00:42:31] time, one small bit at a time. When you
[00:42:33] built lead magic, you were really just
[00:42:34] doing email validation, not just I mean
[00:42:36] that's a big thing.
[00:42:37] >> We just took our agency, we had a no
[00:42:39] code agency portal that we turned into a
[00:42:41] SAS basically, right? That's that's what
[00:42:43] it was. It was like how we did email
[00:42:44] validation and then we just kept going
[00:42:46] like it was just more and more things
[00:42:47] that we shipped. Then we realized uh we
[00:42:50] also had like another way we had a way
[00:42:51] to get like analytics out of our email
[00:42:53] campaigns. That was like the other thing
[00:42:54] we were doing. So we tried both. We
[00:42:57] found that the data part went a lot
[00:43:00] better. Then people started using us in
[00:43:01] clay and they started using us in a lot
[00:43:03] of other tools. We kind of early on
[00:43:05] there and that is how the journey
[00:43:07] started really. But I think getting this
[00:43:10] out the economics are good, right? So if
[00:43:12] you have an API that costs a penny or
[00:43:16] two, right? Three, four cents, whatever.
[00:43:18] And then you have a user that's paying
[00:43:19] $20 a month, $50 a month, $100 a month,
[00:43:22] it's pretty good. The only time it
[00:43:24] becomes bad is when you got a really
[00:43:25] good, you know, it it could get worse
[00:43:27] when you start to have to hire a big
[00:43:29] team, a big a bunch of developers. Then
[00:43:32] you get really high and you go after the
[00:43:34] VC money, right? And you're like, "Oh,
[00:43:35] I'm going to go build this, you know,
[00:43:37] and then you're caught up on one idea.
[00:43:39] It's just I see this happen all the
[00:43:41] time, like try to get it, you know, even
[00:43:43] if it's a few thousand investment to get
[00:43:45] a developer to kind of help you push it
[00:43:47] over the end zone." You probably want to
[00:43:50] do that, right? like that, you know,
[00:43:52] that's what you want to do, right? Um,
[00:43:54] >> which you could even hire on a project
[00:43:56] basis. You don't have to like bring on
[00:43:57] this like CTO or this like full-time. I
[00:44:00] mean, developers are expensive. They're
[00:44:02] a lot of them are super talented and
[00:44:04] with talent in any domain comes expense.
[00:44:08] Um, so if you're able to get to this
[00:44:10] sort of there's a lot of talk in the
[00:44:12] chat right now of this, you know, just
[00:44:14] get it to 80% and then have a developer
[00:44:17] deal with the security and the other
[00:44:18] stuff. Now there you can vibe code that
[00:44:20] as well. Um, but we're getting into more
[00:44:23] of that upper echelon of of knowledge,
[00:44:26] expertise, and just
[00:44:29] >> start with an internal app is what I
[00:44:30] would say. If you're if you're an
[00:44:32] agency, you know, the best way to do it
[00:44:33] is start having somebody build some vi
[00:44:36] start vibe coding some internal
[00:44:38] applications, right? I mean, um, that's
[00:44:41] what we we did, right? So, we were we're
[00:44:43] really good at like building we had we
[00:44:45] had an application to read the emails.
[00:44:47] We had an we had an application to uh
[00:44:50] you know respond. We we did everything
[00:44:53] there because we were doing a lot of
[00:44:54] like cold emails campaigns
[00:44:57] also to build the list um you know like
[00:45:00] we we had a lot of those already rolling
[00:45:04] for us right then what happened but
[00:45:06] those are you know and quite frankly we
[00:45:08] actually scaled to like $30,000 a month
[00:45:12] on uh no code. So the first application
[00:45:15] we had wasn't even code. It was just um
[00:45:19] you know so that was the like that's
[00:45:22] that that's that's the real kicker is
[00:45:24] that people don't really care. They just
[00:45:26] care about the application itself and
[00:45:28] what's
[00:45:30] like what's in it and that's what they
[00:45:32] actually care about. So you got to you
[00:45:34] got to really like if you're going out
[00:45:36] and you're spending 20 $30,000 on an MVP
[00:45:39] you're raising money you're doing all
[00:45:41] this stuff like you're doing stuff
[00:45:42] that's going to cost you a lot of time
[00:45:44] later. And that's why I like Adam's
[00:45:46] approach to the problem with uh you know
[00:45:50] the way that he goes at it with
[00:45:51] bootstrapping and and that because you
[00:45:53] don't even know if you're going to want
[00:45:54] to do it like you might not even like
[00:45:55] selling the product that you make. So
[00:45:58] >> totally and I think this too offer it it
[00:46:01] allows um for this way leaner company
[00:46:05] than you've ever been able to have
[00:46:07] before. So I mean I'll give three
[00:46:10] examples. One is Lead Magic. I mean
[00:46:12] Jesse you have a really small team. you
[00:46:14] have you are
[00:46:15] >> we have like uh we have a we have a
[00:46:17] couple contract we so everybody's on a
[00:46:19] contract um and then we have um you know
[00:46:23] I have like devel a couple of developers
[00:46:25] that I work with that are on a contract
[00:46:26] and then uh you know we have 1300
[00:46:29] customers or so a little over that and
[00:46:32] then you know we're growing pretty quick
[00:46:34] we're obviously in some ecosystems done
[00:46:36] pretty well with community and whatnot
[00:46:38] there but um yeah so it's it's been good
[00:46:41] I mean this is all I do I actually get
[00:46:44] on calls anymore or anything like that.
[00:46:45] I'm just doing this pretty much all day.
[00:46:48] >> Yeah. And you know what this also
[00:46:51] I I'll give the RB2B example and then
[00:46:53] I'll just kind of throw out like what it
[00:46:56] gives you the ability to do, but like I
[00:46:58] mean RB2B now I mean I'm I'm now
[00:47:00] part-time at RB2B. I don't know how many
[00:47:01] folks know that July 1 I launched I I've
[00:47:04] soft launched my own business this this
[00:47:06] summer. Um it's a it's a marketing
[00:47:08] consultancy focused around positioning
[00:47:11] and content marketing things like that.
[00:47:13] Um I'll make a bigger announcement later
[00:47:14] in the fall. Um but um uh you know I I'm
[00:47:19] I'm able to service my clients more
[00:47:23] clients and with more value than I
[00:47:25] possibly would have without any of these
[00:47:27] tools beforehand. I mean the type of
[00:47:29] consultancy I'm I'm I've sort of soft
[00:47:31] launched and I'm building um would not
[00:47:33] have been possible two years ago you
[00:47:35] know three years ago. Um, on the RB2B
[00:47:38] front, it's really Rob who is Rob Clark,
[00:47:42] if you guys follow him on LinkedIn, uh,
[00:47:43] who runs he's like I guess I think he's
[00:47:46] head of AI now is his title, but um, all
[00:47:48] the customer support and sales is run by
[00:47:51] AI now. Um, at at RB2B now that handles
[00:47:56] like 95
[00:47:58] plus% of all the inquiries from a
[00:48:00] support and a sales standpoint. Yeah. Is
[00:48:02] there stuff falling through the cracks?
[00:48:03] Sure. But it's not worth it to actually
[00:48:06] hire somebody to do that. It's worth it
[00:48:08] to have this really lean team of three
[00:48:10] people or in Jesse's, you know, case, a
[00:48:12] couple of contractors and and and
[00:48:15] himself. What it allows you the ability
[00:48:17] to do is like have these crazy offers
[00:48:20] because you don't have this wild
[00:48:21] overhead. You don't have these investors
[00:48:23] that you have to um sort of suffice and
[00:48:26] and make sure they get their, you know,
[00:48:28] some x multiple of their return back.
[00:48:30] You just have to you don't really have
[00:48:32] to worry about anything other than like
[00:48:34] growing your business, doing things that
[00:48:36] are interesting and valuable to your
[00:48:37] market. I mean, Jesse or Adam, which
[00:48:40] both have done at certain points, can
[00:48:42] run these insane premium motions and
[00:48:45] product growth motions, uh, because they
[00:48:48] can just sort of make these decisions
[00:48:50] knowing that there's already great
[00:48:51] margin coming through and this is only
[00:48:53] going to be better for, you know,
[00:48:55] awareness, marketing, stuff like that.
[00:48:56] So it just the the way it allows you to
[00:49:00] um allows you to I guess be more free in
[00:49:04] all aspects of your approach is really
[00:49:06] an amazing thing. Um so um and I see a
[00:49:10] couple people dropped in. Can we see how
[00:49:12] you can help us? Yeah, I'll drop in my
[00:49:14] email here. Um you can uh you can you
[00:49:18] can drop me a uh you can drop me an
[00:49:20] email. Happy to talk with anybody and
[00:49:22] yeah, shoot me an email. Um, I will
[00:49:24] again I'll do it in an actual
[00:49:26] announcement. I've soft launched. We're
[00:49:27] figuring this thing out. Uh, all right,
[00:49:29] Jesse, let's go back to this app. Where
[00:49:32] are we at on the debugging and
[00:49:34] >> Yeah. So, it's um so basically um we'll
[00:49:39] launch
[00:49:42] through the well, so the the application
[00:49:45] itself like basically what you want to
[00:49:47] do is you know you have the API. What
[00:49:50] the API will do is it'll allow you to
[00:49:52] get um so like let's just see um here
[00:49:55] I'll show you on this basically on here
[00:49:59] you would have like this is what so if
[00:50:02] we were going to push this in right this
[00:50:04] would be like what an actual API call
[00:50:06] would look like you'd have that so then
[00:50:08] through here through the app you know
[00:50:10] people could sign in here they could do
[00:50:12] whatever and then um the uh this this
[00:50:16] would be like the the entire application
[00:50:18] really and you would just ship ship with
[00:50:20] this really, you know, so you wouldn't
[00:50:21] have to do anything else.
[00:50:24] >> Incredible.
[00:50:26] >> Um,
[00:50:28] what can you list like what are So you
[00:50:31] have the social listening tool with
[00:50:32] LinkedIn built in internally.
[00:50:34] >> Yeah, that one we have the social
[00:50:36] listening one for us. So this is like
[00:50:39] today this is how many uh you know this
[00:50:41] is like a post that just came out on
[00:50:43] LinkedIn. So then we go here and you
[00:50:46] just respond to it. Um, now the way I
[00:50:49] built this was similar. You just go to,
[00:50:51] you know, you find like the dashboard
[00:50:52] that you want and you vzero through this
[00:50:56] thing and then if you want to add
[00:50:58] companies to the list. So if I want to
[00:50:59] add like Gong or something, I would add
[00:51:02] Gong, you know, but it's I mean this
[00:51:04] would be something you might buy as like
[00:51:06] a SAS application, right? So you'd have
[00:51:09] that and then you can look at the trends
[00:51:11] like I just measure certain things um
[00:51:15] you know like which companies are people
[00:51:17] talking about I'm looking at
[00:51:18] specifically at competitors you know are
[00:51:21] more people talking about find email or
[00:51:23] lead magic you know things like that
[00:51:25] clay getting a lot of mentions you know
[00:51:27] what are like who's talking about them
[00:51:29] th those types of things really
[00:51:32] um
[00:51:34] so that's this is just an internal app
[00:51:37] but
[00:51:38] We do that a lot. So, we just we build a
[00:51:40] lot of these internal apps. It helps us
[00:51:42] really change our uh you know, we get we
[00:51:46] get all the data like we know what's
[00:51:47] going on and it's easier to ship these
[00:51:49] products that way.
[00:51:52] >> This is so crazy. I mean, the amount not
[00:51:54] only the amount that you've like saved
[00:51:56] by doing this, but like the ability to
[00:51:58] build literally build your own world
[00:52:01] without uh you know, basically from a
[00:52:04] sales marketing agency guy. I mean, it's
[00:52:06] it's crazy. So,
[00:52:08] >> it's every agency should be looking at
[00:52:10] this right now because it's gotten so
[00:52:11] much uh it's gotten a lot it's gotten a
[00:52:14] lot easier like um you know what I mean?
[00:52:18] Like it's you really ought to be looking
[00:52:20] at and the people who know are the
[00:52:22] people who are doing the job like what
[00:52:23] needs to be out there. Um here's the
[00:52:25] here's the uh app that we were just
[00:52:28] building with the uh here I'll show you.
[00:52:30] Oops. Um right here. So this is like the
[00:52:34] champion tracker app, right? So you
[00:52:36] would have this. So we added the G, you
[00:52:38] know, we added that. So we have
[00:52:40] essentially this would be your like
[00:52:42] login, your log out, and then what would
[00:52:44] happen is you would just imple you would
[00:52:46] input all of the URLs. This was just
[00:52:48] this is what we vibe coded at the
[00:52:50] beginning. So you know, if you put those
[00:52:52] in, you know, if you put one in that
[00:52:54] would never work there, that's wrong.
[00:52:56] And then you could just enter in all of
[00:52:58] that. So, if it's like um you just put
[00:53:01] them all in the watch list and it just
[00:53:02] shows up here. Now, what's funny is this
[00:53:05] did not work uh when I was doing it in
[00:53:07] VZ, right? I had to bring it into cursor
[00:53:11] to to finish it, right? So, there was a
[00:53:14] bunch of problems and cursor fixed it
[00:53:17] right here. So, um you know, it's still
[00:53:20] fixing it, right? Still going through
[00:53:22] it, making it better, but it's it's all
[00:53:25] done through there and that just allows
[00:53:27] to do it. So if you want to see if
[00:53:28] they're like if they change jobs, you
[00:53:30] just put this on a scheduled update.
[00:53:33] You'd have to call the API
[00:53:36] telling you that the person changed
[00:53:37] jobs.
[00:53:38] >> This is so crazy. So we have we have a
[00:53:40] comment in the chat says, "I had a
[00:53:42] realization that what I need is an AI
[00:53:44] forward developer. My developer is
[00:53:46] always just saying how it's easier to
[00:53:47] just code from scratch because these
[00:53:48] tools create more junk. They can they
[00:53:51] can create you can use them to create."
[00:53:52] That's so I would challenge that u you
[00:53:55] know if you wanted your developer to
[00:53:57] debate you on it I would love to do that
[00:53:58] because um I I'll tell you that was most
[00:54:02] of the mindset of most of the developers
[00:54:04] that I know and I have some really good
[00:54:06] friends who are developers and then I've
[00:54:08] converted a lot of them over and I've
[00:54:11] shown them I've said like all right
[00:54:12] let's do this you you're going to build
[00:54:14] this app I'm going to build this app
[00:54:16] let's see who can build it faster I
[00:54:17] don't know how to code and let's see who
[00:54:18] can build a better app and I will beat
[00:54:21] them 99% of the Like there's no question
[00:54:23] I'm gonna beat them 99% of the time
[00:54:26] because
[00:54:26] >> what are the cases in which you can't
[00:54:27] like what what are some of the
[00:54:29] >> the only case that I couldn't is if it
[00:54:31] was extreme the only I can't think of a
[00:54:34] case actually really um it would be
[00:54:38] I can't really think of a case I think
[00:54:40] it would be like I'm just I never want
[00:54:42] to say 100 because I'm sure somebody
[00:54:43] could figure it out but like here here's
[00:54:45] where they where where it gets really
[00:54:47] crazy when you know how to use the rules
[00:54:50] in cursor
[00:54:52] and you're able to like really box the
[00:54:54] app in and you know how to do like this
[00:54:56] like you're able to do the testing in
[00:54:58] here which is what's happened. So that
[00:55:00] app V 0 the app broke like when I was
[00:55:03] building it like in VZ. So when I
[00:55:06] brought it in here I found every bug and
[00:55:08] fixed every single bug that it found and
[00:55:11] a couple of the issues. There was like
[00:55:12] even a security issue it fixed. Now, if
[00:55:16] the part that you I didn't most people
[00:55:18] wouldn't know how to do, right, is they
[00:55:21] wouldn't know how to um troubleshoot
[00:55:24] that and fix that. Now, I don't know how
[00:55:26] to even do that really. Like, I don't
[00:55:27] even know. I I'd have to go back and
[00:55:28] look and see what happened, but it
[00:55:30] actually did it. And since I have all of
[00:55:32] the stuff connected, it it fixed all of
[00:55:35] the issues. There was actually a
[00:55:36] database issue right here, right? That's
[00:55:38] what happened. There was a database
[00:55:39] issue.
[00:55:41] So, I I don't know. That was like a V 0
[00:55:44] screwed up the when it built the
[00:55:46] database. But now it just fixed it all.
[00:55:48] So now I'm like completely back at zero,
[00:55:51] right? Like you know moment of time
[00:55:52] there was three minutes left on the
[00:55:53] webinar. We just built the whole app.
[00:55:55] Now it's done. Right now I only entered
[00:55:57] in one prompt up here, right? Like if
[00:55:59] you find bugs in your application, you
[00:56:01] know, go to the application to find the
[00:56:03] bugs. Then I said fix the bugs and it
[00:56:05] fixed them all.
[00:56:08] >> Find the bugs.
[00:56:10] So
[00:56:11] >> that's always my favorite thing, Jesse,
[00:56:12] by the way, is when there's this like
[00:56:14] big problem that you need to solve and
[00:56:16] you're like, find the bugs or make this
[00:56:18] shorter and better like
[00:56:21] >> and then it does.
[00:56:22] >> I mean, it's like if you know what the
[00:56:24] modern stack looks like, you're gonna
[00:56:26] have a hard developers are going to have
[00:56:28] a hard time beating you. The best
[00:56:29] developers are using AI now. Best by
[00:56:31] far. None of them are just not using it.
[00:56:34] Like they they know how good it is.
[00:56:35] They're just the good ones are. Yeah, I
[00:56:38] think that is a huge takeaway for the
[00:56:39] folks here because um I'm sure you know
[00:56:42] you you spent a lot of time learning
[00:56:44] this. I'm really in my infancy in this.
[00:56:46] So I it would be tough for I'm working
[00:56:48] on an app uh for for my own business.
[00:56:51] It's it's more of an internal app or
[00:56:53] ones that I can just use with my
[00:56:54] clients. But um even the piece by piece
[00:56:57] of that is like I'm getting quicker but
[00:57:00] like the troubleshooting thing is is
[00:57:02] pretty um can be pretty I guess not
[00:57:05] heavy but it can be a bit of a loop that
[00:57:07] you get stuck in. Uh a little tough. So
[00:57:10] um this is crazy. I mean now guys if
[00:57:12] Jesse wanted to like launch this he'd
[00:57:15] probably make the UI look a little bit
[00:57:16] better with some good screenshots. tack
[00:57:18] on a Stripe integration and then blast
[00:57:21] that out to the world and it could kind
[00:57:24] of be a live a live thing here. So, um
[00:57:27] >> we would I'd have this thing launched
[00:57:29] this afternoon and we we we'd already be
[00:57:30] shipping it. So, we'd have our first
[00:57:32] subscription by the end of the call.
[00:57:34] >> Uh that's
[00:57:35] >> remember you're selling a service too.
[00:57:36] They're buying you, they're buying your
[00:57:38] service. So like if your brand like you
[00:57:39] got to think about that in SAS you're
[00:57:41] you're buying a service like if wherever
[00:57:43] it is now maybe you go on AppSumo launch
[00:57:45] an LTD or something like the good thing
[00:57:47] about it is is the cost of running this
[00:57:49] application is so like it's you could do
[00:57:52] everything I've just done on the free
[00:57:53] tier except for the the data on the um
[00:57:58] uh the data on the figuring out if they
[00:58:01] work at the company anymore.
[00:58:03] >> Yeah. Yes.
[00:58:04] >> Everything else is tier stuff, right?
[00:58:06] >> This is incredible. So, I mean, for
[00:58:08] folks listening, find a problem
[00:58:11] internally that you guys are having or
[00:58:12] maybe something that just takes way too
[00:58:14] long to do manually. Uh, vibe code it
[00:58:17] out. Start your journey. Even if it's
[00:58:19] just from a content basis, uh, hop into
[00:58:22] Vzero, start playing around. Uh, that is
[00:58:26] that is all we can encourage you to do.
[00:58:28] Uh, we Jesse is going to drop the prompt
[00:58:31] uh that he's been using onto LinkedIn.
[00:58:33] Follow him on LinkedIn. I'm popping his
[00:58:36] LinkedIn message or profile there.
[00:58:39] Again, if you're watching on YouTube, it
[00:58:40] will be in the description. Uh Jesse,
[00:58:43] thank you so much for joining, my
[00:58:44] friend. We got to do this again soon.
[00:58:46] We're doing this again soon. Uh next
[00:58:48] week, folks, we have uh the showtime is
[00:58:51] going to be 1:30 Pacific or excuse me,
[00:58:53] 1:30 p.m. Eastern time. We have Josh
[00:58:56] Abramson. He is the founder of College
[00:58:58] Humor, Vimeo, Busted Te's, Teublic,
[00:59:01] total serial entrepreneur, especially
[00:59:03] from the early days of the internet.
[00:59:05] Then I think he launched College Humor
[00:59:06] in like 1999.
[00:59:08] Uh I mean, that was where all the funny
[00:59:10] stuff was online. It's like that and
[00:59:12] Ebomb's world. Uh so it's going to be a
[00:59:14] great episode. We're excited to have
[00:59:16] Josh on. Uh the recording will be live
[00:59:19] on YouTube uh within 24 hours or so,
[00:59:22] folks. Uh,
[00:59:24] and that's all that's all I got. Jesse,
[00:59:27] thank you for showing us. I mean, I've
[00:59:29] gone through this with you and you even
[00:59:30] blew my mind today. So, um, I got to
[00:59:33] thank you so much for coming on and, uh,
[00:59:35] guys, check out Lead Magic. And with
[00:59:38] that, see you next week. Thank you
[00:59:41] everyone.
