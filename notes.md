## Worker_sim notes

#### 5/24/26 7:19 am
I'm have an issue figuring out how to create an async task queue, I'd like the option to spawn workers when a task is queued and then then update assigned work. I'm thinking about using a non-blocking while loop to scan for tasks. I Was thinking about a while loop to scan and another to catch incoming task updates but I think gather does more for my goals here. I've reached a level of completity where scope creep is looming hard. I have to keep my feature list tight so I don't blow this project up. 
    * Hmmm maybe a feature list is a pretty good idea moving forward

#### 5/24/26 6:30pm
The major issue I'm running into is the control flow (I don't know if i'm using that word correctly). I need to map out what each step of the function is supposed to achieve. 
    