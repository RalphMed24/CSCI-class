window.addEventListener("load", function ()
{
    // Get click element references.
    let clickCounterElement = document.getElementById("click-counter");
    let clickButtonElement = document.getElementById("click-button");

    // Counter value.
    let counter = 0;

    // Click button function.
    let clickButtonFunction = function ()
    {
        // Incrementcounter.
        counter++;

        // update counter value.
        clickCounterElement.innerHTML = counter;
    };
    
    // Attach button function.
    clickButtonElement.addEventListener("click, clickButtonFunction");
});