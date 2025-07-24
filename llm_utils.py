import openai

# Replace this with your actual OpenAI API key
openai.api_key = "your_openai_api_key"

def get_llm_explanation_unique(data, confidence, batting_team, bowling_team, target, venue):
    """
    Generate a unique, human-like strategic explanation and prediction summary.
    """

    overs_completed = data['over_ball'][0]
    runs_scored = data['current_score'][0]
    wickets_lost = data['wickets'][0]
    runs_left = data['runs_left'][0]
    balls_left = data['balls_left'][0]
    crr = data['crr'][0]
    rrr = data['rrr'][0]

    response = f"""
## MATCH INSIGHTS AND PREDICTION

**BATTLE LINE-UP:**  
- **Batting:** {batting_team}  
- **Bowling:** {bowling_team}  
- **Venue:** {venue}  
- **Chase Target:** {target}

---

## CURRENT MATCH SITUATION

| Metric                    | Value |
|-------------------------|------:|
| Overs Completed        | {overs_completed:.1f} |
| Runs Scored            | {runs_scored} |
| Wickets Lost           | {wickets_lost} |
| Runs Left              | {runs_left} |
| Balls Remaining        | {balls_left} |
| Current Run Rate (CRR) | {crr:.2f} |
| Required Run Rate (RRR)| {rrr:.2f} |

✅ **Confidence in {batting_team} winning:** {confidence:.2f}

---

## TACTICAL VIEWPOINT

With the target set at {target}, {batting_team} can pace themselves carefully. The pressure tilts towards the bowlers, knowing a single error can shift the match. Although the required run rate looks comfortable, cricket is known for unexpected twists — early wickets or tight bowling spells can still make things interesting.

{batting_team} will aim to stay composed, rotate strike, and avoid risky shots until the chase is under control.  

*Key takeaway:* Even with the numbers in their favor, momentum can flip anytime — but {batting_team} clearly holds the upper hand here.

"""

    return response
