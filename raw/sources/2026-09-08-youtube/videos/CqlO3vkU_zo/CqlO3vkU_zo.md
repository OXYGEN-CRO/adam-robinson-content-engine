# Devin.ai is doing 80% of Rivo's Engineering Work

- Video: https://www.youtube.com/watch?v=CqlO3vkU_zo
- Channel: Adam Robinson (UCSHn0Px37BjzMqnZBmVWwcQ)
- Published: 20250807
- Captured: 2026-09-08T07:41:51.013985+00:00
- Transcript: youtube_automatic_captions; en-orig
- Exact captions: CqlO3vkU_zo.en-orig.json3
- Public-use boundary: Publicly accessible source, collected for private research/context; reuse in new public copy is not approved.
- Speaker caution: Captions are not diarized. Guest statements must not be attributed to Adam without contextual verification.

## Transcript

[00:00:00] Well, just taking notes. They're not
[00:00:02] recording. I got sorry to break the
[00:00:04] flow.
[00:00:05] >> No, no, no worries. So, yeah, you know
[00:00:06] when you're working with a team and like
[00:00:09] you're like, dude, I this is a small
[00:00:10] thing, but like it should be fixed and
[00:00:13] like fix it, but you don't want to be
[00:00:15] that guy.
[00:00:16] >> This has been a a game changer for us
[00:00:19] because it's like, hey, the robot just
[00:00:21] told you that you you kind of didn't do
[00:00:23] a good job at this.
[00:00:24] >> Yeah.
[00:00:25] >> Go fix it. And all the humans can see
[00:00:27] it. So, like there's a around it.
[00:00:30] >> Yeah. No one's going to prove like see
[00:00:31] see what the AI said.
[00:00:33] >> Yeah, exactly. And the suggestions it
[00:00:35] gives back are really good. I don't know
[00:00:37] if we've got some here that we can open
[00:00:39] up and show.
[00:00:40] >> Yeah. I'm curious to see
[00:00:42] >> here we go. And something it does as
[00:00:43] well I like is that it summarizes the
[00:00:45] pull request. So, you can just eyeball
[00:00:47] it as well.
[00:00:48] >> Yeah. Yeah. Yeah.
[00:00:49] >> So, this will go through. This one all
[00:00:52] looked good thankfully. And it will tell
[00:00:54] you why it made decisions, how confident
[00:00:57] it was on like going to comment or not.
[00:01:01] Um, is there another one I can show?
[00:01:06] No, these look good. Thankfully, the the
[00:01:08] team is doing good here. So, we don't
[00:01:09] even have any uh inside of here. Maybe
[00:01:12] this one. This is a big one.
[00:01:13] >> They've been drugged through the mud by
[00:01:15] >> Yeah, I see you're going to rail 7
[00:01:17] because we're up like we're updating our
[00:01:19] version of Ruby right now. That's
[00:01:20] actually where we used AI to fix these
[00:01:22] like pedantic things that no one would
[00:01:23] ever think of. I'm really curious to see
[00:01:24] what this did.
[00:01:26] >> Um, again, the internet is down, but
[00:01:29] let's try this. This is what I would do.
[00:01:31] So, what we want to do is the first run
[00:01:34] is ellipsus, like a light touch AI tool
[00:01:37] that will just say like, hey, this is
[00:01:39] clearly wrong and that needs to be
[00:01:41] updated. Uh, the next step we will do
[00:01:44] and what we're starting to automate is
[00:01:45] we bring in Claude. So you just can at
[00:01:48] Claude and you can say, "Can you review
[00:01:51] this, please?"
[00:01:53] >> No [ __ ] Okay.
[00:01:55] >> Can you see this?
[00:01:57] >> Dude, I bet you it's broken right now.
[00:02:00] >> Okay. I have a question. Question for
[00:02:03] when you invoke Claude, like do do you
[00:02:04] set any master prompts at all to give it
[00:02:06] like background on what you how you want
[00:02:08] it to review? Because I I do code
[00:02:10] reviews like that all the time. If
[00:02:11] someone sends me a massive PR, I'm like,
[00:02:12] "Yeah, I'm not going to read this. I'm
[00:02:13] going to read this with AI." How do you
[00:02:15] like do you have any control over what
[00:02:17] Claude looks for? Um,
[00:02:19] >> you know, I believe you do. We just have
[00:02:21] set it up. We only set this up a couple
[00:02:23] of weeks ago as like the second touch
[00:02:25] point.
[00:02:25] >> Um, but I believe you can like tweak
[00:02:28] that um, review bot, we'll call it,
[00:02:31] that's in there.
[00:02:32] >> Yeah. Okay. Yeah.
[00:02:34] >> Yeah, this is working right now. It
[00:02:35] usually takes
[00:02:37] >> three to four minutes and it'll come
[00:02:38] back. Gives you a really comprehensive
[00:02:41] um, review on what's happened. Y
[00:02:43] >> um which is awesome. So the thing we
[00:02:46] want to do is now in general we're
[00:02:49] moving towards 80% of the code that we
[00:02:52] write here we want it to be written by a
[00:02:55] tool called Devon. But the tool doesn't
[00:02:57] really matter. The idea for us is that
[00:02:59] we've changed to a new model where we
[00:03:02] want the first 10% of work to be done by
[00:03:05] a human that comes along and says here's
[00:03:07] exactly what I want. I'm gonna write a
[00:03:10] very good prompt from a template we
[00:03:12] already input.
[00:03:13] >> Uh Devon is gonna go and it's going to
[00:03:16] write 80% of the work. And then my job
[00:03:19] as a human is to come back and review
[00:03:21] the last 10% of the work. And I'm also
[00:03:24] going to review and let the AI do the
[00:03:27] first run of review so it can catch the
[00:03:30] [ __ ] that I don't have to be
[00:03:31] involved in.
[00:03:32] >> Interesting. So human AI AI human.
[00:03:36] >> Exactly. So, we're just the book ends,
[00:03:40] you know. I think there is like a 108010
[00:03:43] rule or something in business or some
[00:03:45] [ __ ] Some anti-grove [ __ ] Yeah.
[00:03:49] >> Um but it's kind of similar what we're
[00:03:51] doing here. So, let me show you um I'll
[00:03:55] kind of wrap that up. That's more like
[00:03:58] if you have people who are skeptical,
[00:04:01] >> this is a very good place to start.
[00:04:04] >> Yeah. Yeah, man. reading up reviews.
[00:04:05] Everyone's gonna be happy with that,
[00:04:07] right?
[00:04:07] >> Yeah. So, yeah, going into Devon now.
[00:04:10] Um, so yeah, I've been writing Ruby on
[00:04:12] Rails since 2008,
[00:04:15] pretty much every day. PHP before that.
[00:04:18] Um, but even still today, I like barely
[00:04:21] miss a day a year that I'm not writing
[00:04:23] code.
[00:04:24] >> Yeah.
[00:04:25] >> Yep. So the way I think about this and
[00:04:27] I'm try trying to like it took a little
[00:04:30] while to convince the rest of the team
[00:04:31] but when we actually laid it out and
[00:04:33] like just push forward and you show
[00:04:35] people results they actually will will
[00:04:37] jump on board um okay
[00:04:39] >> a lot sooner.
[00:04:40] >> So what we did was we looked at a few
[00:04:42] different agentic coding tools. There's
[00:04:45] a guy called Sahil Lavinga. He is the
[00:04:50] Gumroad CEO if you ever heard of that
[00:04:52] product.
[00:04:52] >> Yeah. Okay. Yeah. Yeah. Yeah. Yep.
[00:04:54] >> Yeah. He uh his content turned me on to
[00:04:58] this which is he was using Devon with
[00:05:01] the exact same thing 108010 80% of the
[00:05:04] work done by Devon.
[00:05:06] >> Um and let me show you here how we've
[00:05:09] got this set up and how we think about
[00:05:11] it. So when we first turn this on,
[00:05:13] right, you got to go and you basically
[00:05:15] replicate your workspace here. So, it'll
[00:05:18] take you about an hour and you go and
[00:05:20] you set up your uh like workspace that
[00:05:23] you would have on your machine. You just
[00:05:25] replicate it inside of Devon. I'm going
[00:05:27] to install RVM, Git, all that. Um get it
[00:05:32] set up.
[00:05:33] >> Um which is fine, right? But I think a
[00:05:36] lot of people stopped at,
[00:05:37] >> hey, this thing should just work the day
[00:05:39] you turn it on. It's definitely not what
[00:05:42] we found. So we actually spent I would
[00:05:45] say three months um
[00:05:48] rebuilding the code base and how we work
[00:05:51] around this.
[00:05:51] >> Yeah. Can you expl So because like I
[00:05:53] know exact like I think what you're
[00:05:54] trying to say is Devon needs to be able
[00:05:56] to execute and run like full integration
[00:05:58] test truly be effective and to do that
[00:06:00] you need a proper environment kind of
[00:06:02] like CI/CD right like you want CI/CD to
[00:06:03] run. So it's effectively like building
[00:06:05] up a proper pipeline. So when you say
[00:06:08] what do you mean by like adapting the
[00:06:09] codebase? Can you like did you what does
[00:06:11] it mean? Super curious.
[00:06:12] >> Yeah.
[00:06:13] >> Yeah. So,
[00:06:16] the main thing we wanted to do was give
[00:06:19] these guard rails to Devon, right? So,
[00:06:22] you ever see even in like a chat GPT
[00:06:25] claude or cursor or co-pilot, there's
[00:06:28] way too much hallucinations. And when
[00:06:31] you get
[00:06:31] >> when you get a few hallucinations back
[00:06:33] and you're trying to get your team on
[00:06:34] board, they'll just tune out and they'll
[00:06:37] be like, "Dude, the thing sucks." Right?
[00:06:39] But the real problem is that there just
[00:06:40] aren't enough guard rails. So what we
[00:06:42] did instead was we spent probably a
[00:06:44] month reducing technical debt on the
[00:06:46] codebase itself,
[00:06:48] >> we our goal was, hey, for this LLM to
[00:06:53] work on the codebase, we need to rewrite
[00:06:56] the codebase to be LLM friendly.
[00:06:59] >> So that means cleaning everything the
[00:07:02] [ __ ] up. If something's not being used
[00:07:04] and it's hanging around, get it the [ __ ]
[00:07:06] out of the repo. Um, we need to clean up
[00:07:09] all of our uh docs. So, docs was a big
[00:07:12] thing as well. So, like I can show you
[00:07:14] here,
[00:07:16] >> man. Yeah,
[00:07:17] >> we set up these docs, right? Which is
[00:07:20] basically like, hey, LLM, this is how we
[00:07:24] write code. And do not think even think
[00:07:28] about writing it any other way. So, we
[00:07:32] have it all set up here. This is basic
[00:07:33] highlevel stuff. like when in doubt,
[00:07:36] search the codebase for similar
[00:07:37] implementations.
[00:07:39] >> Um all this kind of stuff. Yeah. So we
[00:07:42] we worked our way through this even down
[00:07:44] into like here's an example of a Rails
[00:07:48] controller, how I want you to write it
[00:07:50] and like
[00:07:51] >> we we're still seeing
[00:07:54] >> Sorry. I see. But like F. So you
[00:07:57] actually
[00:07:59] I'm excited to see this, but like Yeah.
[00:08:01] So how did you did you get it like how
[00:08:03] did you come up with these guard? Is it
[00:08:05] just trial and error? Pretty much like
[00:08:07] >> pretty much. Yeah.
[00:08:08] >> Yeah.
[00:08:08] >> Um, show my screen anyway
[00:08:11] >> cuz Yeah, you just said like how do you
[00:08:13] how do you Here's
[00:08:14] >> During the cleanup process, did you lean
[00:08:17] into any AI to help you actually clean
[00:08:21] out your noise and garbage?
[00:08:24] >> Yeah. Um, yeah, as much as we could, but
[00:08:27] a lot of it was a lot of there was a lot
[00:08:28] of like grunt work in there, like
[00:08:30] changing the name of a file.
[00:08:33] Instead of being like worker manager,
[00:08:35] it's like, hey, it's actually like
[00:08:38] customer VIP updater, you know what I
[00:08:41] mean? Like
[00:08:42] >> very descriptive.
[00:08:43] >> Um, can you guys see my screen or am I
[00:08:46] still [ __ ]
[00:08:47] >> See,
[00:08:49] >> I'd love to see it. I can definitely
[00:08:51] follow along. I think I was following
[00:08:52] along with your examples for sure. It's
[00:08:54] like
[00:08:54] >> let me try this
[00:08:55] >> controller template.
[00:08:56] >> Okay. No.
[00:08:59] >> No. Julie. No.
[00:09:00] >> [ __ ] it. Here. I'll show you just uh
[00:09:03] just the GitHub instead. It's easier.
[00:09:05] Here we go.
[00:09:07] One second.
[00:09:13] All right, we're back. Here we go.
[00:09:16] >> You can see GitHub right now.
[00:09:18] >> Yes.
[00:09:19] >> All right. So if we go into here docs
[00:09:22] llm how to write rails code
[00:09:25] >> here we go
[00:09:27] >> you can see here everything hey it's
[00:09:29] extremely important to maintain code
[00:09:31] uniformity and follow established
[00:09:33] patterns we have like all these docs
[00:09:36] that's like
[00:09:37] >> don't do this this is wrong do this um
[00:09:41] this is how we want controllers to be
[00:09:43] written best practices like we go pretty
[00:09:47] detailed like we got thousands of lines
[00:09:49] lines of code that it has to read. So
[00:09:52] again, we cleaned up the whole uh code
[00:09:55] base. We wrote all of these docs, which
[00:09:57] is like, hey, I'm going to clobber you
[00:10:01] over the head until you like do not
[00:10:04] write or return anything that does not
[00:10:06] go by the guidelines that we have.
[00:10:10] >> Holy [ __ ]
[00:10:11] >> And then like, okay, for writing tests,
[00:10:13] here's how I want you to do it. So like
[00:10:15] super detailed like that.
[00:10:18] all the R spec like Wow.
[00:10:19] >> Yeah. I like bang my head against the
[00:10:22] wall. It was like three months of
[00:10:23] absolute torture, but like to get out
[00:10:25] the other side of it, it's like just
[00:10:27] make things so much easier.
[00:10:28] >> Yeah. Yeah. Yeah.
[00:10:29] >> Um so then what we did was we went to
[00:10:33] Devon and like anything else, it's the
[00:10:37] prompt that you put into it is the
[00:10:38] output that you get back out, right? So
[00:10:41] >> we made this template that we tested um
[00:10:45] over the course of like a few weeks and
[00:10:47] this is the only way that the team can
[00:10:49] submit a um a prompt to dev
[00:10:53] >> is we have this shortcut right where
[00:10:55] it's xdevon
[00:10:57] and this will just open up um like it'll
[00:11:00] pop this in. So that's 90% of the work
[00:11:02] done and actually writing it.
[00:11:04] >> Yeah. Master pro. Okay. Yeah. Yeah.
[00:11:06] Yeah.
[00:11:06] >> Yeah. So this is where I do a quick
[00:11:08] oneliner. Hey, this is what you need to
[00:11:10] do. Like the overall description if it
[00:11:12] needs to go into any more detail. We've
[00:11:14] also found that referencing files of
[00:11:17] where you know that there's similar
[00:11:18] code.
[00:11:19] >> Yep.
[00:11:20] >> Way better.
[00:11:20] >> Okay.
[00:11:21] >> Um so we'll like drop that into there as
[00:11:23] well. Hey, check out this file because
[00:11:24] this is what it's very similar.
[00:11:26] >> Um before you start, you must read this
[00:11:30] doc on how to on how we write code.
[00:11:33] >> That's before you. So at the end when
[00:11:36] it's when it's done and it's about to
[00:11:37] submit its work, here's the checklist
[00:11:40] that it has to check off before it can
[00:11:42] do that. It needs to submit a test with
[00:11:44] the work, it needs to run our llinter,
[00:11:48] so our rubu copy.
[00:11:50] >> That's another big part of keeping guard
[00:11:51] rails on. So we want the code to really
[00:11:55] be like Lego blocks, right? Yeah,
[00:11:57] >> like in a perfect world if you can just
[00:11:59] think of it like Lego blocks because
[00:12:01] really most engineers will like turn
[00:12:04] their nose up at you and be like, "Dude,
[00:12:06] you're you know what I mean? You're not
[00:12:08] cultured or whatever, but like we're
[00:12:09] here to [ __ ] build businesses and
[00:12:11] make money." So like,
[00:12:12] >> you know, that's the biggest struggle,
[00:12:14] right? It's like, yeah, that's nice, but
[00:12:15] we're here to sell value. Yeah. Yeah.
[00:12:17] Yeah. Totally
[00:12:18] >> right. Exactly. So like to me, I'm just
[00:12:21] trying to make this like this is the
[00:12:23] feature, you know, everything. We want
[00:12:25] this to be inside the little world that
[00:12:28] we built for you and do not go outside
[00:12:30] of it or start making [ __ ] up.
[00:12:33] >> Okay.
[00:12:33] >> And then
[00:12:34] >> got it.
[00:12:34] >> So every bit of the way you got to be
[00:12:36] like here's the checklist just checking
[00:12:39] in to make sure that you're like on side
[00:12:41] with this.
[00:12:42] >> Um and then before submitting they have
[00:12:44] to run the full test suite. Um we've
[00:12:47] also got it set up for um integration
[00:12:50] tests but we do that in GitHub because
[00:12:52] it takes a bit too long. So, we want the
[00:12:55] final run to be an integration test on
[00:12:57] GitHub. You could have it uh here, but
[00:13:00] we just decided against it. Um, and
[00:13:02] again, this just goes through pretty
[00:13:04] much everything and just saying like
[00:13:06] here's what to do.
[00:13:08] >> Like it's it gets kind of mind-numbing,
[00:13:10] but once you do it once, you just need
[00:13:12] to do it like pop it in like this. Um,
[00:13:15] >> totally.
[00:13:16] >> So, like we've built a lot from here. So
[00:13:19] like if I show here,
[00:13:26] so like we actually only changed this.
[00:13:29] This should look a lot more impressive,
[00:13:31] but I only realized that there's a
[00:13:32] setting to change your who runs it was
[00:13:35] coming through as Stuart. So a lot of
[00:13:37] the tests that were being done.
[00:13:39] >> Yeah. Yeah.
[00:13:40] >> Coming through as me. So it's probably
[00:13:42] more like 450 I would say that was done
[00:13:45] by Devon. And if you look at the next
[00:13:46] person down, it's like a 100. So it's
[00:13:48] like a 4x
[00:13:49] >> Jesus.
[00:13:50] >> Uh above the next engineer. This guy's
[00:13:53] [ __ ] super talented. But again, like
[00:13:56] just a lot more volume because it works
[00:13:59] 24/7 by itself, right? Um
[00:14:03] >> crazy, man.
[00:14:04] >> So let me show you then.
[00:14:08] So getting back to
[00:14:12] how do we get the team involved in this
[00:14:15] and then going back to
[00:14:17] hey the reviews is a great place to
[00:14:20] start and then the next place I found is
[00:14:22] really good
[00:14:24] >> that it's not going to like make people
[00:14:26] skittish.
[00:14:27] >> Yeah.
[00:14:28] >> Uh is intercom help docs. This one has
[00:14:31] been [ __ ] killer for us. Um and we're
[00:14:34] actually really doubling down on it
[00:14:37] right now. In fact, we've got a lot of
[00:14:38] open poll requests. I'm running it
[00:14:40] literally right now. Um, so I can show
[00:14:43] you exactly what we're doing here. So,
[00:14:46] we switched like a week ago um from this
[00:14:52] playbook we've been running on Shopify
[00:14:54] for the last 10 years has been jump on a
[00:14:57] live chat with somebody and um they'll
[00:15:00] leave a review on your Shopify app and
[00:15:02] you get the number one in the rankings
[00:15:03] for Shopify. Right.
[00:15:04] >> Okay. That playbook is dead. Like it is
[00:15:08] absolutely gone. They I'm not sure if
[00:15:10] you saw it. Shopify nuked like 60% of
[00:15:12] the reviews on the platform.
[00:15:14] >> I did
[00:15:14] >> and they just dep prioritized that as
[00:15:16] being a like
[00:15:18] >> reason to go.
[00:15:19] >> Um which turned out to be actually
[00:15:22] fantastic for us because now we're just
[00:15:24] actually going to be able to build a
[00:15:25] better product, not have to have these
[00:15:27] kind of goofy
[00:15:29] >> um actions that didn't need to exist in
[00:15:31] the first place, right?
[00:15:32] >> Yeah. Yeah. Yeah. Okay, fair enough.
[00:15:34] What we've done instead is we turned on
[00:15:37] Finn, uh, which you guys obviously use
[00:15:39] as well.
[00:15:40] >> Um, and we've just been blown away by
[00:15:43] how good it is. We tried it like when it
[00:15:45] first came out, it was fine. Now it's
[00:15:48] just really good what we found.
[00:15:51] >> Yeah.
[00:15:52] >> I'm sure you in fact I think you guys
[00:15:54] have a case study with them, right?
[00:15:55] >> I think.
[00:15:56] >> Yeah. Yeah. They love us,
[00:15:57] >> right? Nice.
[00:15:59] >> Yeah. So,
[00:16:01] >> can I ask you a question about that?
[00:16:02] Because here's my biggest concern at
[00:16:03] least on on the Yeah.
[00:16:05] >> How do you get how do you get Finn?
[00:16:07] Because I I assume I know and Adam
[00:16:09] mentioned this, but you and like Devon
[00:16:10] and Finn are the two of them are working
[00:16:13] together. How do you prevent proprietary
[00:16:15] knowledge from seeping out? Like are you
[00:16:16] doing a full review on everything it
[00:16:18] generates?
[00:16:19] >> Yeah. So, let me show you here.
[00:16:21] >> Okay. See how you do that.
[00:16:23] >> Here's what we do. We literally have a
[00:16:25] You could automate this, but do you just
[00:16:27] run this every two weeks? You're gonna
[00:16:29] be fine.
[00:16:30] >> Yeah. Um, here's what we do. I go to
[00:16:33] Claude, right? Uh, so Claude code.
[00:16:36] >> Oh, shoot. Screen share might have died
[00:16:38] again. Damn.
[00:16:39] >> Oh, [ __ ] me. Um, I won't be able to show
[00:16:42] it then, but you'll you'll get it.
[00:16:44] >> Oh, yeah.
[00:16:45] >> I go to cloud code in my terminal and I
[00:16:48] paste this in. Usually I'll do like 25
[00:16:50] or something like that. Um, and I'll
[00:16:52] just say, oh, wait, I'm in the wrong
[00:16:54] one. That's for writing tests you can do
[00:16:57] automatically. This is for writing
[00:16:59] articles here.
[00:17:00] >> Reason I can't see. So question, did you
[00:17:02] set up like do you have like a master
[00:17:04] prompt or like a workspace and claude
[00:17:06] specifically designed with your
[00:17:08] guardrails in this domain as well then?
[00:17:11] >> Yeah. Um
[00:17:12] >> okay.
[00:17:15] I'll show you on the page right now
[00:17:16] somehow. Uh yeah, and what I've done is
[00:17:20] we have we downloaded all of the
[00:17:23] intercom articles to our repository,
[00:17:27] right? So if we go here, we go to docs
[00:17:33] intercom. This is all of our intercom
[00:17:36] articles right here in HTML, right?
[00:17:40] >> [ __ ] Okay. And what we do then is we go
[00:17:43] to this script
[00:17:46] and I say, "Hey, give me all of those
[00:17:48] files that I just showed you in that big
[00:17:50] list. That's all of our intercom
[00:17:52] articles.
[00:17:53] >> Skip this [ __ ] because it's like stuff
[00:17:55] we don't want to improve anyway, like
[00:17:56] office hours. Who gives a shit?"
[00:17:58] >> Uh, go through each one. Make sure it's
[00:18:01] the right files. And now we get to here.
[00:18:04] >> And this is going to be run from my
[00:18:05] Rails console, right? where I go
[00:18:07] >> and I say update and improve our
[00:18:10] existing customerf facing help doc
[00:18:12] located at the file
[00:18:14] >> uh update it you are an expert at
[00:18:16] writing customerf facing help doc so
[00:18:18] just a really good prompt or as good as
[00:18:20] we can say it's primarily a knowledge
[00:18:22] base for our AI chatbot deeply research
[00:18:26] do not provide any technical detail to
[00:18:28] the codebase in your work this is a
[00:18:30] customer helping facing help doc we're
[00:18:33] creating
[00:18:34] >> just that line has actually stopped it
[00:18:36] ever providing any information. Now, if
[00:18:39] we ever saw anything otherwise, we would
[00:18:42] like tighten that up.
[00:18:44] >> Um,
[00:18:45] >> so yeah, and again, I can just like
[00:18:47] share this with you here.
[00:18:50] >> It's just Yeah. So, you
[00:18:53] >> Interesting. So, you're going to pass
[00:18:55] every doc in with the prompt. It will do
[00:18:57] what it needs to. So, yeah. Actually,
[00:18:59] sorry. What is the Sorry. What is the
[00:19:00] rest of that workflow? So, you have this
[00:19:01] workflow. Oh, well, you said it
[00:19:02] yourself. You're connecting to the Devon
[00:19:04] API.
[00:19:04] >> Yep. So then from here, we just made a
[00:19:07] prompt. Um, and now we're going to send
[00:19:08] it to Devon. So, um, that is the request
[00:19:12] to Devon right there because look, we're
[00:19:14] going to Devon to create a new session.
[00:19:17] >> Yeah.
[00:19:17] >> Uh, and this is one I literally just ran
[00:19:20] today, but we're going like all in on
[00:19:22] this now.
[00:19:23] >> Um, so like let's take a look at what's
[00:19:27] one here.
[00:19:28] >> All right, let's go.
[00:19:31] So here's what Devin did.
[00:19:34] Devon took this is the prompt that I
[00:19:35] just showed you that I ran with the API.
[00:19:39] >> Devon broke this down. It thought about
[00:19:41] it. Um, it said it confidence was low
[00:19:46] and then it keeps working. It searches
[00:19:48] the the browser. It searches the
[00:19:50] internet. It searches all the code bases
[00:19:53] how this thing actually works. And then
[00:19:55] it comes back and it says, "Okay, I've
[00:19:57] now talked through this. Um, here's the
[00:20:00] help doc we're going to update. here is
[00:20:02] what we're going to do. And then it goes
[00:20:04] back and and executes on that.
[00:20:07] >> Then it will come back and it will
[00:20:09] create a pull request inside of GitHub,
[00:20:12] which again we're just going to update
[00:20:13] the intercom article with an API call.
[00:20:17] So
[00:20:18] >> here, this was the previous doc. Look at
[00:20:21] this.
[00:20:22] >> Like it was one line, right? So like
[00:20:25] >> way dude,
[00:20:29] >> let's leave. curious to see. There's no
[00:20:32] like
[00:20:33] >> look at that. That was the
[00:20:35] >> That was the
[00:20:38] when you come here like
[00:20:40] >> Yeah, I see all this markup. It's like
[00:20:42] it just wrote a whole damn article.
[00:20:44] >> Context explains exactly how the feature
[00:20:46] works and Yeah.
[00:20:48] >> So like here I can show you what this
[00:20:50] looked like. This will
[00:20:54] >> interesting, man. That's really
[00:20:55] interesting.
[00:20:56] >> One sec. I'm just gonna pop this open.
[00:20:59] I'm just thinking of
[00:21:00] >> you. We can see then actually how good
[00:21:02] it is.
[00:21:05] >> All right, I'm on the new branch. Now
[00:21:07] I'm going to open up this.
[00:21:12] >> All right, so that one liner is now all
[00:21:16] this
[00:21:17] >> and like just eyeballed this, it's
[00:21:20] correct and it's right.
[00:21:22] >> Yep.
[00:21:23] >> Yeah. So you just do like your expert
[00:21:25] human in the loop review to make sure it
[00:21:26] didn't completely lose it mind.
[00:21:28] >> And honestly at this stage we've seen
[00:21:31] we've reviewed so many of these now that
[00:21:33] we don't even review them anymore. We
[00:21:35] >> we just we have a script that auto
[00:21:38] merges them from GitHub just because we
[00:21:40] so much
[00:21:41] >> so funny man.
[00:21:42] >> Um so this right here what we do then is
[00:21:46] we say yeah this looks fantastic. We are
[00:21:48] going to merge this in. I would merge
[00:21:52] the pull request into
[00:21:55] our codebase. In fact, let me like do it
[00:21:58] right now over here.
[00:22:03] >> Even though everything's broken on the
[00:22:05] internet, we will
[00:22:08] >> probably not going to fail any tests.
[00:22:12] >> Rob, Rob, what do you think? Is this is
[00:22:13] this something along these lines like
[00:22:17] accomplish our mission of just like
[00:22:19] systematically eradicating
[00:22:21] categories of tickets?
[00:22:26] >> Yeah. Um
[00:22:28] from the development perspective, it's
[00:22:30] more like I I don't have any keys to
[00:22:34] that kingdom whatsoever.
[00:22:35] >> Yeah. Yeah. Yeah. I mean, we got to get
[00:22:36] Tate to buy into it.
[00:22:37] >> No. Yeah.
[00:22:38] >> I don't want to take Hold on. I don't
[00:22:39] want I don't want to take Stuart's time
[00:22:40] talking to you about that. I can talk to
[00:22:41] you.
[00:22:41] >> No. No. But you're good. I'm happy.
[00:22:43] >> The concept and everything. Oh god. Yes.
[00:22:45] Like to be able to come in here and give
[00:22:49] a really like that 10% prompt of, hey,
[00:22:52] this is what we need to solve. We need
[00:22:53] to be able to do this. Go do the thing.
[00:22:56] Review yourself. Go do that. Blah blah
[00:22:59] blah blah blah. Like
[00:23:02] hate's time is finite. There's only so
[00:23:04] many hours in a day. And
[00:23:07] if he's able to accomplish 10 side
[00:23:11] quests,
[00:23:12] >> yeah,
[00:23:13] >> by going, hey, this is what I need to
[00:23:16] do. You go do the thing. And then let it
[00:23:18] go off on a side quest form. And then
[00:23:21] then it comes back and he does this 10%
[00:23:23] like review going,
[00:23:24] >> "Yeah, that's going to do exactly what I
[00:23:26] want."
[00:23:27] >> Yeah.
[00:23:28] >> God, yes. And that's that's our biggest
[00:23:30] hurdle right now is that again, there's
[00:23:32] only so many hours in a day and Tate is
[00:23:34] human. Yeah.
[00:23:35] >> And as great as he is, he he he's either
[00:23:39] doing a main quest or a side quest, but
[00:23:42] it'd be great if he could do the main
[00:23:44] quest and side quest at the same time,
[00:23:46] which this would
[00:23:47] >> this concept would allow him to do.
[00:23:49] >> Now,
[00:23:51] he's going to have to guard rail stuff
[00:23:53] like
[00:23:55] >> Yeah, probably. So, yeah, Stuart, if you
[00:23:59] don't mind, I have a bunch of like
[00:24:00] operational questions like how you point
[00:24:02] and I know we touched on it. So one
[00:24:04] thing for us like we build like we we
[00:24:05] similar to you we build and support a
[00:24:07] ton integrations and so we're we're
[00:24:08] doing this refactoring project going
[00:24:09] from this old messy pattern to this
[00:24:11] refactored one and funny enough AI
[00:24:13] helped suggest the pattern and so I know
[00:24:15] for sure it could implement it. So I was
[00:24:17] trying to think through it's like
[00:24:19] when you were starting like I imagine
[00:24:20] you started off with like little like
[00:24:22] little projects and little things in a
[00:24:23] in a in a confined space until you
[00:24:25] worked your way up across the whole code
[00:24:27] base. How do you um
[00:24:29] is that how you recommend getting
[00:24:30] started? Like I'm kind of picturing now
[00:24:32] it's like here's an old pattern and you
[00:24:33] the documentation we'd give a human
[00:24:35] here's the new pattern go build like a
[00:24:36] new integration for this and just give
[00:24:39] it API docs like is that something you
[00:24:42] say in it relatively in its scope. Um
[00:24:45] >> yeah in fact speaking of integrations is
[00:24:48] actually a great place to start.
[00:24:52] >> That's what I thought because it's
[00:24:53] relatively deterministic and it's
[00:24:55] timeconuming as [ __ ]
[00:24:57] >> Exactly. A win-win, you know. So,
[00:25:00] there's this old boomer, uh, in fact,
[00:25:04] maybe Adam might know it. You know,
[00:25:06] Braves, it's like an ESP.
[00:25:08] >> Dude, yeah,
[00:25:09] >> Braze [ __ ] hates us.
[00:25:11] >> Yeah. Okay, perfect.
[00:25:12] >> They [ __ ] hate us.
[00:25:14] >> So, like, nobody on our team wants to
[00:25:17] touch [ __ ] Braze integration. I I'd
[00:25:20] rather walk across traffic than do this.
[00:25:23] So, like,
[00:25:23] >> yeah, sounds right.
[00:25:24] >> What we did was went here, said, "Here's
[00:25:27] the original." Look at this. Isn't
[00:25:30] >> Yeah.
[00:25:30] >> You know what? Actually, funny enough, I
[00:25:32] did this one from my phone. Like I
[00:25:36] [Music]
[00:25:37] >> you can like just give it a task. It'll
[00:25:40] run the template and like do it. So I
[00:25:42] was like, "Okay, hey, go and make this
[00:25:44] brace integration. It's kind of like
[00:25:46] clavion attentive." Um I didn't even
[00:25:48] give it the docs. It went
[00:25:51] >> link any code or anything.
[00:25:53] >> Yeah. like um this as well is Claude.
[00:25:57] Claude did the review on this and I
[00:25:59] found some things that were actually
[00:26:00] legit
[00:26:01] >> and then Devon goes back and it actually
[00:26:04] looks at Claude's review and it says,
[00:26:06] "Hey, you know what? That was right." So
[00:26:08] now we've got uh and there was zero
[00:26:12] human um interference in this pull
[00:26:17] request whatsoever. I wrote the prompt.
[00:26:20] AI Devon went and wrote the um the code
[00:26:24] and you can see here it added the first
[00:26:26] one and then it started getting feedback
[00:26:28] on the work it had done. So it got
[00:26:29] feedback from the um the tests.
[00:26:32] >> Yeah.
[00:26:33] >> Updated some stuff. It then got feedback
[00:26:35] from Claude and it said, "Hey, you know
[00:26:38] what? Brings up some good points. So
[00:26:40] look, Devin, look at Claude's feedback
[00:26:42] and determine what is factually
[00:26:43] accurate. Consider updating the PR based
[00:26:46] on your findings."
[00:26:48] Um, so like
[00:26:50] >> we turned it on and the [ __ ] thing
[00:26:51] works and that's probably I don't know
[00:26:54] three days of work that would take
[00:26:56] >> yeah to do like it there's 13 behind it
[00:27:01] >> nine files like
[00:27:05] >> there all the
[00:27:07] >> exactly it came back with the test too
[00:27:09] >> that dude
[00:27:11] >> no there was not one line of this that
[00:27:13] was written by me or anyone on the team
[00:27:16] >> that's that like That's unreal because I
[00:27:18] I I think that's what our goal is and I
[00:27:19] think this is like we have an awesome I
[00:27:21] love working with Jorge. He's built all
[00:27:23] our integrations and he's the one who
[00:27:24] loves AI. He's the most forward thinking
[00:27:26] there. Do you if you're cool, can you
[00:27:28] share me the the initial prompt? I'd
[00:27:30] love to show because um that's going to
[00:27:32] be I think one of my challenges for him
[00:27:34] and kind of his like quarterly goal. Hey
[00:27:36] man, go build an integration without
[00:27:37] touching a line of code.
[00:27:38] >> Right. Like I think and I actually have
[00:27:41] some more operational questions because
[00:27:43] you spent you said you spent was it one
[00:27:44] month refactoring or up to three? Like
[00:27:46] like I know it's iterative but like how
[00:27:48] much time realistically is like how many
[00:27:51] lines of code are we at? It doesn't
[00:27:53] really matter. I'm just curious like I
[00:27:54] think I understand what you're trying to
[00:27:56] say with that but um
[00:27:57] >> oh dude well was kind of like uh here
[00:28:03] I'll show you. It probably depends on
[00:28:05] how much technical debt there is and how
[00:28:07] old the codebase is and
[00:28:08] >> Oh yeah.
[00:28:09] >> So after after we set up
[00:28:11] >> in advance, sorry,
[00:28:12] >> I know you're good. Um we spent a
[00:28:15] shitload of time writing docs and then
[00:28:17] like the next week Devin released this.
[00:28:20] This is so incredibly good. Like this is
[00:28:25] >> astounding how good this is. Nobody
[00:28:27] wrote this. This just showed up one day
[00:28:31] >> in Devon and it's a complete
[00:28:33] architectural breakdown
[00:28:35] >> of our entire code base and how things
[00:28:38] works. Like here's how our loyalty
[00:28:41] system works in extreme detail and every
[00:28:44] single detail inside of here.
[00:28:46] >> Yeah.
[00:28:47] >> Like imagine how long it would have
[00:28:49] taken a human to to write all of this.
[00:28:52] would have been it would have zapped all
[00:28:53] my energy for who knows
[00:28:55] >> like
[00:28:56] >> I mean
[00:28:57] >> yeah that that right there is like a
[00:29:00] quarterly rock.
[00:29:01] >> Yeah.
[00:29:02] >> For a person.
[00:29:03] >> Yeah.
[00:29:03] >> You know like it's like all right I'm
[00:29:05] going to do my job by the end. I'm gonna
[00:29:07] have this
[00:29:08] >> document
[00:29:09] >> super clear PRD. You know every little
[00:29:12] detail about our loyalty system actually
[00:29:14] documented so everybody can use it.
[00:29:16] >> Yeah. Heaven forbid somebody
[00:29:18] >> and it just [ __ ] showed up. showed up
[00:29:20] one day,
[00:29:22] >> man. How many models, if you don't mind
[00:29:23] me asking that, how many models do you
[00:29:25] have in in Revo? I think it was Revo
[00:29:27] Commerce.
[00:29:27] >> That's big, man. Probably a hundred.
[00:29:30] >> Yeah. Okay. Because we're probably
[00:29:31] there, too. That's awesome, man.
[00:29:33] >> It's Monolith. Um, Monolith is the way
[00:29:36] to go as well, I found, just because
[00:29:38] it's like
[00:29:38] >> it's all the cont. Yeah.
[00:29:40] >> Yeah. Services where like everyone's
[00:29:42] like, "Yeah, what's what the hell? No
[00:29:43] one does Monolith anymore." Then AI came
[00:29:45] along. It's actually
[00:29:46] >> Yeah, exactly. So, we got lucky with
[00:29:48] that. Uh
[00:29:50] >> no no it was forward thinking
[00:29:53] >> but so when you look at that right this
[00:29:56] is what brought us to the intercom help
[00:29:58] docs cuz at the end of the day when you
[00:30:01] tell somebody you ask somebody hey can
[00:30:03] you write a help article on this thing
[00:30:05] oh yeah dude I got it on my list I'll do
[00:30:07] it blah blah blah but like
[00:30:09] >> nobody knows the code better than Devon
[00:30:11] because look at what I just had there so
[00:30:13] if you say to it make a customerf facing
[00:30:15] help doc it'll go yes because I
[00:30:18] absolutely absolutely understand how
[00:30:19] this works better probably than the guy
[00:30:21] who wrote the thing.
[00:30:22] >> Yeah. Yeah. I know
[00:30:26] the way like Yeah.
[00:30:29] >> So having having the help articles as
[00:30:31] the first place will kind of
[00:30:35] not spook any developers but it will
[00:30:38] also show what it can do. And then what
[00:30:41] I would do is I would start with
[00:30:43] integrations. Look, I just showed like,
[00:30:45] hey, nobody on the team wants to touch
[00:30:46] this thing with a 10- foot pole, but we
[00:30:50] actually did it with Devon and you're
[00:30:53] welcome. You know, you know what I mean?
[00:30:55] >> Yeah.
[00:30:58] >> We're in lucky spot like the owner of
[00:31:01] integrations. It's it's one guy. He's
[00:31:02] incredible. He loves like he's so good.
[00:31:04] He loves AI. So that's where I'm like
[00:31:06] that's I think my first deliverable with
[00:31:08] getting this started and that's going to
[00:31:09] like you said all the cracks will begin
[00:31:11] to show right when it loses its mind and
[00:31:12] we're like what is it doing? Um,
[00:31:14] >> yeah.
[00:31:14] >> So, it's just chipping away at that.
[00:31:16] That's really interesting. Then, um, how
[00:31:18] many, so, if you don't mind me asking,
[00:31:19] how many people are contributing to the
[00:31:20] repo right now? Like, you're full.
[00:31:22] >> Uh, there there was two of us here until
[00:31:25] three months ago. So, there's three of
[00:31:27] us now.
[00:31:27] >> Three of you guys. Yeah. Yeah. Okay.
[00:31:30] That that then we're think we're four or
[00:31:33] five now. But I think it's reasonable.
[00:31:37] >> It's more than reasonable. That's cool,
[00:31:38] man.
[00:31:38] >> Yeah. like um I mean hopefully this
[00:31:41] recording isn't shown by people who I'm
[00:31:42] about to talk about but like uh between
[00:31:45] us it's like if someone on the team
[00:31:48] wasn't bought in that
[00:31:52] >> way is the way forward I'm like dude I
[00:31:54] just can't work with you like
[00:31:57] >> we're on two different paths here
[00:31:59] >> I don't have time to like
[00:32:01] >> fully convince you from zero you know
[00:32:03] >> yeah I I made a similar decision with
[00:32:06] Adam well not with that like when we
[00:32:07] were in Toronto actually made a long
[00:32:09] time ago. But yeah, totally, man. It's
[00:32:11] you have to you just have to. It's
[00:32:13] impossible. Like, man,
[00:32:14] >> well, when you see stuff like this
[00:32:17] >> Yeah.
[00:32:18] >> like the first example. I mean, I'm not
[00:32:19] an engineer, but so I and this was the
[00:32:23] first example of
[00:32:26] it's doing 80%, you know, the 10 8010
[00:32:29] like, you know, I've heard from
[00:32:30] Microsoft 20 or 30 and then, you know,
[00:32:32] Tate's like, I use it to debug or
[00:32:34] whatever the [ __ ] Like,
[00:32:35] >> yeah,
[00:32:36] >> this is the first systematic. Yeah, man.
[00:32:38] >> Successful execution that I've actually
[00:32:40] seen a plan for.
[00:32:42] >> Um,
[00:32:43] >> yeah. And
[00:32:45] >> and dude, I think Tate's probably
[00:32:46] waiting on on this, too. You know,
[00:32:49] I don't know. You tell me like if he
[00:32:51] actually sort of had a clear
[00:32:53] understanding of the whole system.
[00:32:56] >> I Well, I have a couple questions for
[00:32:58] you about that, Stuart, actually,
[00:32:59] because it's don't like how good is it
[00:33:01] at the zero to what I where I think
[00:33:03] where where Tate would push back and
[00:33:04] rightfully so. How how have you found it
[00:33:06] for the zero to one? Like building
[00:33:07] integration is not zero to one. It's
[00:33:09] it's one to many, right? Like you've
[00:33:11] done it before even in your I saw in
[00:33:12] your uh your like in the the PRD there,
[00:33:15] if you will. You're like, "Hey, we have
[00:33:16] Claio
[00:33:18] kind of." Yeah.
[00:33:19] >> I'll be it. How How are you finding it
[00:33:21] for zero to one? Because I find when I
[00:33:22] like when I I I do I do not tons of PRs,
[00:33:25] but I usually do like complex business
[00:33:27] logic. I just it would take me way
[00:33:28] longer to explain. I'll just program it
[00:33:29] kind of thing. Uh how do but how do you
[00:33:31] find it does with like I call it zero to
[00:33:34] one but just like new stuff like you
[00:33:37] know what I'm trying to say.
[00:33:38] >> Yeah. I know maybe ours is slightly
[00:33:41] different because I've been building in
[00:33:43] just the Shopify like little bubble for
[00:33:46] the last 10 years. So like the amount of
[00:33:49] net new stuff that comes across is like
[00:33:52] not much which is where I get back like
[00:33:54] the Lego blocks.
[00:33:55] >> Yeah. Would I put it at a zero to one?
[00:33:58] >> Like at the moment Devon really does
[00:34:02] really kills it. Sometimes it'll just do
[00:34:04] like a one shot on junior and midlevel,
[00:34:08] right? Like like integration stuff we
[00:34:10] showed. I think the next step for it and
[00:34:12] the way it's gonna go um is you would
[00:34:16] use either what we found works well is
[00:34:20] using deep research um on chat GPT to
[00:34:24] spend 20 minutes breaking down the
[00:34:25] actual problem. You ask it to break it
[00:34:28] into separate digestible sections that
[00:34:30] you can run and then you actually do
[00:34:33] those as the Devon task.
[00:34:35] >> Yeah. So instead of giving it one big
[00:34:37] thing, you give it five little things
[00:34:39] and and incrementally build it.
[00:34:41] >> Yeah. Okay. Interest. That's so cool,
[00:34:44] man. That makes perfect sense. Yeah.
[00:34:46] >> Yeah. I I find that's where AI excel.
[00:34:48] The more you give AI
[00:34:51] in general, the the higher the
[00:34:54] probability that it loses its way as it
[00:34:57] goes. But if you can break it into
[00:34:59] digestible chunks, like you said, hey, I
[00:35:01] want to accomplish A
[00:35:04] and then afterwards, we're gonna move on
[00:35:05] to B. Um it's it's so much better at
[00:35:10] handling all that. And
[00:35:12] >> yeah,
[00:35:12] >> what you're showing here is
[00:35:15] the way nothing makes me like cringe
[00:35:19] more than all the people on LinkedIn
[00:35:20] going, "Oh, I'm vibe coding this
[00:35:22] weekend." I'm like,
[00:35:24] you have no idea what the AI just spit
[00:35:26] out. and that's going to backfire in a
[00:35:29] month when something doesn't work and
[00:35:31] you have no idea how to fix it. It's
[00:35:33] it's the people that don't know how to
[00:35:34] code that they're using AI to code
[00:35:36] something
[00:35:37] >> and they're going this is my product.
[00:35:40] >> You're doing the opposite. You know
[00:35:41] exactly like you could write all this
[00:35:44] yourself,
[00:35:45] >> but you're not. You're you're giving it
[00:35:47] that prompt. You're having it do all the
[00:35:48] work and then you're coming in
[00:35:50] afterwards going, "I'm going to
[00:35:52] proofread it." Like what you've done,
[00:35:54] make sure it works. And that only works
[00:35:56] if the person doing it can do it
[00:35:58] themselves in general.
[00:36:00] >> Yeah. You're more like a manager than a
[00:36:02] doer. That's the change.
[00:36:04] >> Yeah.
[00:36:04] >> Right. And that's that's the problem
[00:36:06] with all the vibe coders is they don't
[00:36:08] actually know how to do it. So it's all
[00:36:12] going to backfire and that's why it's
[00:36:13] going to go sideways. But you need a
[00:36:15] Steuart, a Tate, a A Chate Tate, a Mike
[00:36:19] that actually understands it, could
[00:36:21] write it themselves, and is just using
[00:36:23] this as a tool to expedite processes.
[00:36:26] >> Yeah. This is just saving time or
[00:36:28] accelerating time. We can build 10x
[00:36:30] faster than like we used to.
[00:36:33] >> Exactly.
[00:36:33] >> Yeah.
[00:36:34] >> Yeah.
[00:36:35] >> One more two more maybe two more
[00:36:37] questions. So sorry like
[00:36:39] >> like I I mean I think like the advantage
[00:36:40] that we have is that we know what we
[00:36:41] have a lot of context on the business
[00:36:43] and we have the vision for like what
[00:36:44] this thing actually does not not the
[00:36:46] code
[00:36:47] >> and I guess what I'm trying to figure
[00:36:48] out is how do you how have you found you
[00:36:50] said you just recently brought someone
[00:36:51] in like I guess my concern is someone
[00:36:53] who like typically engineers don't share
[00:36:55] the amount of context so a lot of the
[00:36:56] work is giving them the context to do
[00:36:58] the work. Um and I guess where I'm
[00:37:00] getting concerned is if they don't have
[00:37:01] enough context how are they going to
[00:37:02] give the AI the context? How have you
[00:37:04] found that transition for that for that
[00:37:05] new person that you added? Like are like
[00:37:08] did you hire someone really senior? Like
[00:37:10] how did you get over that piece?
[00:37:12] >> Yeah. He's a a longtime friend of mine
[00:37:14] of worked before. He's CTO.
[00:37:17] >> Oh [ __ ] Yeah. He's like Yeah. Yeah.
[00:37:19] Yeah.
[00:37:19] >> Yeah. But like again,
[00:37:22] >> it's just coming back to the the guard
[00:37:24] rails. Like here's the 90% of the like
[00:37:27] prompt or the person that So we're we're
[00:37:31] actually changing the whole business.
[00:37:33] >> Um we're trying to take exactly what we
[00:37:36] just showed you here
[00:37:37] >> and apply it [ __ ] everywhere.
[00:37:41] >> So like we're starting from scratch. Um
[00:37:43] but something we're trying to do is just
[00:37:45] put those guard rails in place. So,
[00:37:48] >> how do these tickets get to be developed
[00:37:50] in the first place? Well, they start out
[00:37:52] on GitHub issues or linear or sana or
[00:37:55] whatever you guys use.
[00:37:56] >> Yeah, totally.
[00:37:57] >> We're now we're making guard rails
[00:37:59] around those tickets where when a ticket
[00:38:01] gets submitted, if this ticket is not
[00:38:04] good enough, the robot is going to come
[00:38:06] back and say, "Steuart, this ticket
[00:38:09] sucks. Here's where it needs to improve
[00:38:10] because our engineers can't work on this
[00:38:12] unless they have context."
[00:38:13] >> Yep. Um, and again, the next step of
[00:38:15] that is actually getting those linear
[00:38:17] tickets to go straight to Devon, but
[00:38:19] that's a different story altogether.
[00:38:21] >> Um, that's like the next the next step
[00:38:23] we're trying to get to. But
[00:38:25] >> having using something like uh this is
[00:38:28] actually a fantastic tool that's
[00:38:30] probably down, but uh have you heard of
[00:38:32] this?
[00:38:32] >> Yep.
[00:38:33] >> Yeah. This is the next the next [ __ ]
[00:38:36] here. So, this will set up a trigger.
[00:38:39] It'll say uh linear ticket was created.
[00:38:42] You say AI go and do your agent stuff
[00:38:46] and go through this and make sure that
[00:38:48] it hits all of these requirements that
[00:38:50] we have for the ticket. If not, comment
[00:38:52] back and at the person and say, "You
[00:38:55] need to update this. We don't have
[00:38:56] enough information for our engineers to
[00:38:58] work on it
[00:38:59] >> because you know, man, ours want to like
[00:39:03] some of the tickets that come through
[00:39:04] and it's like this is broken." And I'm
[00:39:06] like, "What's broken?"
[00:39:08] >> You know what I mean? It's like a not
[00:39:09] even a screenshot or nothing. Yeah,
[00:39:12] >> I can feel that pain. Yeah,
[00:39:13] >> that's like sometimes that's like three
[00:39:16] days you get lost because you're talking
[00:39:17] back and forth on a ticket that just is
[00:39:19] not good enough.
[00:39:20] >> Interesting.
[00:39:21] >> Yeah, totally.
[00:39:22] >> So stuff like that. Just making the t
[00:39:24] the initial ticket has to be like the
[00:39:27] same idea behind it here.
[00:39:30] >> Totally. It's just all Yeah, you're
[00:39:32] right. It's guardrails and context.
[00:39:33] That's literally what like that's how
[00:39:35] we've always operated. We just never had
[00:39:36] to think about it because we're not
[00:39:37] prompting a machine. We're just talking
[00:39:38] to people. But like
[00:39:39] >> Yeah. And when it's a human humans don't
[00:39:41] like telling the truth 100% but the
[00:39:45] robots don't know so they'll tell you it
[00:39:47] sucks
[00:39:48] >> I don't like overseas developers but it
[00:39:51] feels like I'm working with like the top
[00:39:52] of the top guy who doesn't really speak
[00:39:54] like sounds weird to say it that way but
[00:39:55] you know what I'm trying to say it's
[00:39:56] like
[00:39:57] >> I need to be so careful with how I
[00:39:58] communicate you and if I am you'll do a
[00:40:00] great job and if I'm not you will you
[00:40:01] fail beyond belief. Um yeah that's cool
[00:40:06] man. Okay this is really helpful. I'm
[00:40:07] trying to I'm already picturing ways
[00:40:09] like I think I think the way I almost
[00:40:11] want to do this is I want to get those
[00:40:12] incremental wins. Um I think it was the
[00:40:14] Eclipse the review bot. I'm gonna
[00:40:16] absolutely try that.
[00:40:17] >> Uh Ellipse.
[00:40:20] >> Yeah, that's Thank you. Yeah, I'm going
[00:40:21] to absolutely get that in. That's an
[00:40:23] easy win. No one's like I think
[00:40:24] everyone's going to be relieved when
[00:40:26] they're getting a review of posting a
[00:40:28] PR.
[00:40:28] >> Oh, you know what? I don't think that
[00:40:30] the full prompt came through in the
[00:40:31] chat. I'll uh I'll email you the uh the
[00:40:34] still
[00:40:35] >> please. Yeah, cuz I I really like I
[00:40:39] don't know what I don't know. And like
[00:40:40] you said, it did take that time to kind
[00:40:42] of tackle that tech debt. Like you got
[00:40:43] to go slow to go fast.
[00:40:45] >> Yeah.
[00:40:46] >> But I'm a little greedy. I kind of want
[00:40:47] to try to see what how fast we can go
[00:40:49] without doing a lot of that work first
[00:40:50] and then figuring out, okay, [ __ ] I've
[00:40:52] pushed a little too hard here. Here's
[00:40:53] how we build those guardrails.
[00:40:55] >> And I think I think just doing the help
[00:40:57] articles first is going to be the best
[00:40:59] way to do it.
[00:41:00] >> Yum. Because it's not code critical.
[00:41:02] It's just help articles. developers
[00:41:04] won't get their pants in a twist or
[00:41:06] whatever, you know?
[00:41:08] >> Yeah.
[00:41:09] >> Easiest way to start it.
[00:41:10] >> Yeah. Yeah.
[00:41:13] >> This is awesome, man. Thank you. This is
[00:41:14] like It's nice. I think what Adam nailed
[00:41:16] it, like it's nice to actually see it in
[00:41:18] real life adding value to a real
[00:41:20] business, not someone talking about on
[00:41:22] YouTube or wherever. It's like, oh [ __ ]
[00:41:24] makes sense.
[00:41:25] >> Yeah, things are going to get weird,
[00:41:27] man. It's um it's weird times.
[00:41:30] >> Yeah, things are weird, man.
[00:41:33] Yeah,
[00:41:33] >> but hey, it's good to be it's good to
[00:41:35] capture and know what to do in the weird
[00:41:37] because then you're set. So,
[00:41:39] >> yeah, absolutely. I'm like, I think I
[00:41:40] think we might have emailed before like
[00:41:42] a couple of years ago or a year ago.
[00:41:44] >> Yeah, definitely.
[00:41:44] >> Yeah. So, you have my email. So, any
[00:41:46] questions you have or anything like
[00:41:47] that, feel free to hit me up.
[00:41:48] >> I appreciate that, man. Thank you so
[00:41:49] much for your time. This was like this
[00:41:51] is cool. You're definitely I don't know,
[00:41:53] man. You're doing really good stuff. I'm
[00:41:55] just say like that was awesome to see,
[00:41:57] dude. Thank you.
[00:41:58] >> Yeah, man. I appreciate it. Absolutely.
[00:42:00] >> Agree. George, can I ask you one more
[00:42:01] question?
[00:42:02] >> Yeah. Yeah.
[00:42:03] >> So, do you now that you're not getting
[00:42:05] reviews from free users, do you still
[00:42:07] have the view that if you're not getting
[00:42:08] something from them, you're being an
[00:42:10] idiot? Because this has been tormenting
[00:42:12] me for the last 15 months. Like, we're
[00:42:14] not getting anything from these [ __ ]
[00:42:15] free guys.
[00:42:19] >> Yeah. I mean, ours is kind of we made
[00:42:22] the move up market. Um, where anyone
[00:42:25] who's using our product who's doing
[00:42:27] under 500 grand a year, a million, just
[00:42:30] like you're definitely going to turn
[00:42:32] like I don't even recommend you install
[00:42:34] this thing at all.
[00:42:35] >> Yeah.
[00:42:36] >> Um, but in your case, I'm sure there's
[00:42:39] still some other stuff. I remember we
[00:42:41] first talked, you were talking about
[00:42:43] like free people have to post UGC to
[00:42:46] keep
[00:42:47] >> Yeah, something like that. I don't know.
[00:42:49] It's we we had another Yeah. problem
[00:42:51] with UGC is like to get people to put
[00:42:54] out good posts, it needs to benefit them
[00:42:56] too,
[00:42:56] >> you know,
[00:42:57] >> right?
[00:42:57] >> So like the agency ecosystem for Clay
[00:43:00] was great for us, but then it stopped
[00:43:03] being great because our use case really
[00:43:07] you have to have a ton of traffic to
[00:43:08] like use Clay and Smart Lead and like
[00:43:10] actually make it work. So it's like
[00:43:13] >> it was just it was it was not great. And
[00:43:15] it's like how much can you write about
[00:43:16] one signal? Clay's Clay UGC is amazing
[00:43:19] because you can create anything,
[00:43:21] you know,
[00:43:22] >> right?
[00:43:23] >> Their ecosystem. Anyway, um yeah, I'll
[00:43:26] keep thinking about it.
[00:43:26] >> Is there are they like draining
[00:43:28] resources? The free people like
[00:43:30] >> No, they're not doing [ __ ] By the way,
[00:43:31] we just let two people go. We're going
[00:43:32] to try to get to 10 million with three
[00:43:34] bodies. Me, Rob, and Tate.
[00:43:38] >> Rob. No, but I'm actually I'm going to
[00:43:40] start I'm going to start answering
[00:43:42] tickets and doing I I was spending way
[00:43:45] too much of my week on [ __ ] that was not
[00:43:48] related to RB2B and I'm not in touch
[00:43:50] with the customer at all. So like I
[00:43:52] basically just quit my other job of I'm
[00:43:55] gonna I'm going to write LinkedIn posts,
[00:43:56] answer customer support tickets, and
[00:43:58] talk to customers for the next six
[00:43:59] months and that's it. So
[00:44:02] >> well, dude, it's worked out so far. some
[00:44:04] of the some of the burden off of Rob.
[00:44:08] >> He's he's about to have his finger on
[00:44:10] many many many pulses.
[00:44:13] >> Yeah.
[00:44:13] >> Love it.
[00:44:14] >> Exactly.
[00:44:15] >> Instead of just hearing about me telling
[00:44:17] him what the pulse is. So,
[00:44:19] >> yeah.
[00:44:19] >> Yeah.
[00:44:21] >> Um,
[00:44:22] >> dude, Stuart, you're the man. If you
[00:44:24] ever need anything from us, please.
[00:44:27] >> I appreciate it, guys. Always good to
[00:44:29] chat.
[00:44:30] >> Yeah, man. Thank you so much.
[00:44:32] >> Bye.
[00:44:32] >> Thanks, Stuart. Take care everyone. See
[00:44:34] everyone. Thank you.
