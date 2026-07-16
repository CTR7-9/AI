/*
 Copyright 2024 Google LLC

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

      https://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
 */

// create a class of prompts
class Prompts {
    constructor() {
        this.SITUATION_PROMPT_PREFIX = `
Available: The channel is currently not involved in any activity, or constrained by any environmental factors. It takes low to zero effort to use the channel to do a new task. Example: A user is sitting at their desk with their hands free, eyes not engaged in any task, and no background noise interfering with their hearing or speech. 
Slightly Affected: The channel is engaged in an activity or constrained by an environmental factor. Given a new task that requires the channel, users can multitask, easily pause and resume to the current activity, or easily overcome the situation. Example: A user is holding a remote control, which can be quickly put down to free up their hand for another task. 
Affected: The channel is involved in an activity or constrained by an environmental factor. Given a new task, the user may experience inconvenience or require effort to use the channel. Example: A user is carrying grocery bags in both hands, making it challenging to use the hands for other tasks without putting the bags down first. 
Unavailable: The channel is completely unavailable due to an activity or environmental factor, and the user cannot use it for a new task without substantial adaptation or changing the environment. Example: A user is attending a loud concert, making it impossible for them to hear incoming notifications or carry on a conversation without stepping outside.

Given the current activity and environment as described below, what are the availability of C’s vision/eye, hearing, vision, and hands/fingers channels? For each channel provide reasons first and then answer using the scale defined above: available, slightly affected, affected  or unavailable. 
Separate each channel prediction with a semicolon (;).

Q: C is washing dishes in a kitchen sink. C is in a kitchen. C’s hand is washing dishes. The environmental volume is around 40 dB. 
A: Let’s think step by step. 
Eye Reasoning: While C is washing dishes, their eyes are partially occupied with the task at hand, which involves looking at the dishes to ensure they are clean. However, they can still glance away or multitask to some extent, so their vision is slightly affected but severely impacted.
Eye: Slightly Affected;
Hearing Reasoning: Washing dishes in the kitchen sink does not affect C's hearing. They can still hear other things happening around them.
Hearing: Available;
Vocal Reasoning: C's speech and voice are not impaired by washing dishes. They can still talk or communicate with others while performing the task.
Vocal: Available;
Hand Reasoning: As C's hand is currently engaged in washing dishes, it is not available for other tasks. If C needs to use their hand for something else, they would need to stop washing dishes and wipe their hands.
Hand: Not Available;
[ANSWER COMPLETED]

Q: C is playing an acoustic guitar in a room. C is in a small, cozy room with minimal furniture and decorations. C’s hand is playing an acoustic guitar. The environmental volume is around 58 dB.
`;
    }
}
