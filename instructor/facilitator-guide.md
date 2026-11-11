# Facilitator Guide: Library Mapathon

A monthly, three-hour drop-in session. After setting up, participants work through three self-paced mapping steps on the cheat sheet: pick a square, trace in iD, save and submit. The host runs a 10-minute walkthrough at :10 and :40 past each hour, and helpers circulate. There are no timers: everyone starts wherever they are when they arrive.

The slide notes at the end of this guide are generated from `slides/slides.qmd` by `scripts/make_guide.py`, so the slide numbers always match the deck. Edit notes in the slides file, never here.

## Each month: setup checklist

### About three weeks before

- Confirm the DRI Lab booking: Wi-Fi, outlets, and a screen for the slides.
- Send Comms the date and graphics for the event page and announcement post.
- Put up posters with the date filled in.

### One to two weeks before

- Choose this month's HOT project and a backup. Check that both are open to all mappers, ask for simple features (buildings, or buildings and roads), have clear imagery, and have at least two unmapped tasks per expected attendee.
- Email the project manager: the date, roughly how many first-time mappers to expect, and the hashtag #AUmapathon. Ask for one sentence on why the data matters.
- Map two or three tasks yourself, so you know the imagery and any tricky features.
- Confirm two or three helpers. New helpers get the helper prep and training first.
- Reserve the Chromebooks and a few spare mice.

### Day before

- Update the THIS MONTH block in `_variables.yml` and in `index.html`, re-render (see README), and check the "This month's project" slide.
- Create this month's entry and exit surveys, then print their QR codes for the tables.
- Print 30 cheat sheets (two-sided) and 3 sign-in sheets.
- Test the slides on the room's screen. Log in to the Tasking Manager on the presenter laptop.

### On the day, before doors open

- Survey QR codes on every table. Sign-in sheets and cheat sheets at the door.
- Slides on slide 1. Wi-Fi details and this month's project number on the whiteboard.
- This month's project open on the presenter laptop, with the project number written on the whiteboard.
- The live stats: slide 13 shows the ohsomeNow dashboard for #AUmapathon. Check it loads on the room's Wi-Fi. If it stays blank, open stats.now.ohsome.org/dashboard#hashtags=aumapathon in a second tab instead.

## Timing: the 30-minute cycle

There is no fixed agenda. This cycle repeats from doors open to close.

| Minute past the hour | Host | Helpers |
| --- | --- | --- |
| :00 to :10 | Greet arrivals, point them to step 1 | Help with accounts and email confirmation |
| :10 to :20 | Walkthrough: context, slides 2 to 5 (ending with why it matters), then setup on slide 6, mapping responsibly and the overview on slides 7 and 8, and the steps on slides 9 to 11, demonstrating them in the live project, then this month's project on slide 12. End on slide 13 (live stats) and leave it up. The YouthMappers pitch is slide 14, right after the stats | Circulate; check people's project number and their first few features |
| :20 to :40 | Circulate | Circulate |
| :40 to :50 | Walkthrough again if anyone new has arrived; otherwise skip | Circulate |
| :50 to :00 | Circulate | Circulate |

Fixed points: at 1:30 into the session, a halfway check-in using the live stats on slide 13. At 2:45, the wrap-up on slide 15 (thank you).

## Controlling the slides

The slides use arrow keys or the space bar. Press **S** for speaker view with these notes, **F** for full screen, **Esc** for the slide overview, and **O** to jump straight to a slide. There are no timers to start or stop.

## Troubleshooting

| Problem | Do this |
| --- | --- |
| Wi-Fi is down or slow | Switch everyone to MapSwipe on phone data. It needs little bandwidth and no training. |
| Tasking Manager is down | Open iD directly at openstreetmap.org over the project area and trace there, with the same hashtags. |
| The project has no available tasks | Move to the backup project (in `_variables.yml` and on the website), and write its number on the whiteboard. |
| Sign-ups stall | Many new accounts from one network can trip OSM's spam protection. Pair people on one laptop and have them finish their accounts at home. |
| No confirmation email | Check spam, then try another address. |
| iD won't open from the Map button | Allow pop-ups for tasks.hotosm.org. |
| iD opens in the wrong place | Go back to the Tasking Manager and click Map on the task again. |
| Imagery is cloudy or blurry | Mark the task as bad imagery in the Tasking Manager and pick another square. |
| Someone can't use a mouse precisely | Offer another way to take part: welcoming new arrivals, MapSwipe on a phone, or mapping in pairs. |

## Notes for every slide

### Slide 1: Drop in. Map something.

**Say:** Leave this slide up while people arrive. Point each newcomer to the sign-in sheet and the cheat sheet, and to the survey codes on the tables.

**Why:** The surveys are how the library counts and evaluates these sessions, so ask everyone, not only first-timers. Searching for the project number gets laptops straight to this month's project.

**Watch for:** People skip the sign-in sheet and the survey when the room is busy. A helper at the door fixes this better than a reminder later.

### Slide 2: What's a mapathon?

**Say:** Start every half-hourly walkthrough here. A mapathon is a group mapping session for a project that needs data. Everyone works on their own small square, and nobody needs to be an expert, because every square is checked afterward.

**Why:** Many walk-ins have never heard the word "mapathon." The context slides (this one to Contributing to the map, slide 8, with setup on slide 6) answer "what is this and why does it matter" before anyone touches a laptop.

**Watch for:** People who already started on their own. Let them keep going; this loop is for newcomers.

### Slide 3: The free, editable map of the whole world, built by volunteers

**Say:** OSM is to maps what Wikipedia is to encyclopedias. Everything we add today is immediately available to anyone, anywhere.

**Why:** Beginners often think HOT and OSM are the same thing. This slide and the next keep the map and the coordinators apart.

**Watch for:** "Is this Google Maps?" No. OSM is open data that anyone can use, including apps people may already use without knowing it.

### Slide 4: The Humanitarian OpenStreetMap Team connects mappers with responders

**Say:** HOT is one organization that coordinates humanitarian projects on OpenStreetMap, with aid partners and local communities.

**Why:** HOT is also a partner in Missing Maps, whose organizer guides this kit draws on.

**Watch for:** People who think HOT owns the map. It doesn't: OSM belongs to its contributors.

### Slide 5: Responders can’t reach people who aren’t on the map

**Say:** Commercial maps follow markets. Open, volunteer maps can follow need.

**Why:** People stay longer when they know the edits are real and someone asked for them.

**Watch for:** Someone asks whether tracing from far away is appropriate. Say yes, there's a slide on that shortly (slide 7), and come back to it there.

### Slide 6: Before you start

**Say:** Most people did this before they came. If you didn't, start here; it takes about 15 minutes, mostly waiting for the confirmation email. Your username and edits are public, so your username doesn't have to be your real name.

**Why:** Email confirmation is the slowest part of the session, so get newcomers started on it before they start mapping.

**Watch for:** Many sign-ups from the campus network at once can trip OSM's spam protection. If sign-ups stall, don't keep retrying: pair people and move on. Fast participants can skip the walkthrough; send anyone who struggles with closing shapes back to it.

Checkpoint (on the cheat sheet): your OSM username shows at the top right of the Tasking Manager.

### Slide 7: What we trace today is step one. People who live there finish the map.

**Say:** Missing Maps describes field mapping as the second step after remote tracing: local volunteers capture what imagery can't show, and help represent the voices of the people who live there.

**Why:** It answers the "outsiders mapping someone else's home" question honestly, and it explains rules that otherwise look arbitrary, like not adding names.

**Watch for:** Someone wants to label a building as a school or clinic because it looks like one. Ask them to leave it as a plain building.

### Slide 8: Contributing to the map

**Say:** That's the whole job: pick a square, trace, save and submit. We'll go through each one in a minute.

**Why:** A short overview lets people see the whole job before the details.

**Watch for:** People who want to start right now. Let them; they can follow along on the cheat sheet.

### Slide 9: Step 1: Pick a square

**Say:** Show the project page: the number at the top, who asked for the data, and the Instructions tab, which says what to map. Then the task map: big projects are split into squares, and the colors show which are free, taken, mapped or checked. Picking a square locks it, so nobody else maps the same area at the same time.

**Why:** Beginners skip the instructions and then map the wrong things, and the Tasking Manager has thousands of projects that ask for different things. The number check catches anyone in the wrong project before they map anything.

**Watch for:** People who opened a project with a similar name or number. Check the number on their screen; if it's different, have them search for #{{< var project.number >}} again. People picking a square someone else has locked. Pop-up blockers stopping iD from opening: allow pop-ups for tasks.hotosm.org.

Checkpoint (on the cheat sheet): the project number matches, and the task is locked for mapping by you.

### Slide 10: Step 2: Trace in iD

**Say:** Name four parts of iD: the drawing buttons along the top, the map, the left panel that shows what you've selected, and Save at the top right. Then demonstrate whatever this month's project asks for. For buildings, trace the footprint where the building meets the ground, not the roof, which leans in the photo. Ctrl+Z (⌘Z on a Mac) undoes one step at a time.

**Why:** iD looks busy on first open, and naming four parts is enough to start. Squared, ground-level footprints are what validators check for.

**Watch for:** People tracing things the instructions didn't ask for, which often means they're in a different project, so check the number. Also overlapping buildings, buildings joined to roads, and tracing outside the square. The left panel lists many feature types; people only need the one or two their instructions name.

Checkpoint (on the cheat sheet): click something you traced, and the left panel names a feature type the instructions asked for.

### Slide 11: Step 3: Save and submit

**Say:** The comment is your log. It tells everyone, including you later, what you did and for which project. Then hand the square back: either submit it as done or stop mapping so someone else can finish it. Both are fine; a careful partial job beats a fast, messy one.

**Why:** Documenting each change is part of good mapping, and the hashtag is how we count what the library mapped together. A task left locked blocks other mappers until the lock times out.

**Watch for:** People who write nothing in the comment, or delete the project hashtag the Tasking Manager filled in. Check the comment box over their shoulder the first time. People who close the tab without submitting or stopping: remind the room at the halfway check-in and the wrap-up.

Checkpoint (on the cheat sheet): the Save button shows 0 unsaved edits, and your square changes color on the project map.

### Slide 12: This month's project

**Say:** Read the project's purpose aloud. Name who asked for the data and what they will do with it.

**Why:** Knowing who asked for the data is what keeps people mapping past the first building.

**Watch for:** Update these lines every month in _variables.yml, and the matching block on the website. Keep the requester's own wording short and credit them.

### Slide 13: What we've mapped: live stats for #AUmapathon

**Say:** Nothing. Leave this slide up between walkthroughs. It's the live ohsomeNow dashboard for #AUmapathon, so the numbers grow as people save. Click into it to change the date range, for example to today's hours. When the next walkthrough starts, press Home to go back to slide 1.

**Why:** Seeing the count go up keeps people mapping, and it shows newcomers what the room is doing.

**Watch for:** A blank slide means the dashboard didn't load: check the Wi-Fi, or ohsomeNow may not allow embedding. Then open https://stats.now.ohsome.org/dashboard#hashtags=aumapathon in a separate browser tab and switch to it between walkthroughs. New edits can take a few minutes to show up.

### Slide 14: “We don’t build maps. We build mappers.”

**Say:** Officer roles look great on a résumé, you get mentoring from library staff, and you can run a mapathon with this kit. We're looking for a president plus two or three others, across class years.

**Why:** The chapter needs students to restart it, and mapathon regulars are the best candidates.

**Watch for:** Interested people who don't check the box. Ask them to add their email to the sign-up sheet before they leave.

### Slide 15: Thank you for mapping

**Say:** Read out the session's totals if you have them. Thank people for coming, and mention next month's date.

**Why:** Seeing the total makes the contribution feel real, and the survey only works if people take it before they leave.

**Watch for:** Most people leave quietly before the wrap-up. Helpers should mention the exit survey to anyone heading out.

### Slide 16: Sources and credits

**Say:** Nothing. Leave this slide at the end of the deck.

**Why:** Credits keep the open-licensed material reusable.

**Watch for:** Nothing.
