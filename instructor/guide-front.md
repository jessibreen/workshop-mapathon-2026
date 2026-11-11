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
