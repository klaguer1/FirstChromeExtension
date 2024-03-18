const USER_SEARCH = " ";
const styleSheet = document.createElement("link");
styleSheet.rel = "stylesheet";
styleSheet.type = "text/css";
styleSheet.href = chrome.runtime.getURL("popup.css");

document.head.appendChild(styleSheet);

chrome.runtime.onMessage.addListener((obj, sender, response) => {
  const { type, value, searchText } = obj;

  if (type === "GOOGLE_SEARCH") {
    // Assuming the first h3 tag in the search results is the result title
    const firstResultTitle = document.querySelector("h3");
    if (
      firstResultTitle &&
      firstResultTitle.textContent.includes("Frankensons Pizzeria")
    ) {
      // Create a div container to hold the image and text link
      const imageContainer = document.createElement("div");
      imageContainer.className = "image-container";

      // Create an image element
      const imageElement = document.createElement("img");
      imageElement.src = chrome.runtime.getURL("assets/keith-lee.png"); // Replace with the actual path
      imageElement.alt = "Keith Lee";
      imageElement.className = "keithLeeImage";

      // Create a text link element
      const textLink = document.createElement("a");
      textLink.href = "#"; // Replace with the actual link
      textLink.target = "_blank";
      textLink.textContent = "Keith Lee reviewed";

      // Append the image and text link to the image container
      imageContainer.appendChild(imageElement);
      imageContainer.appendChild(textLink);

      // Append the image container to the search result title
      firstResultTitle.appendChild(imageContainer);
    }
  }
});

() => {
  const testCall = () => {
    console.log("you see me ");
  };

  const getTime = (t) => {
    var date = new Date(0);
    date.setSeconds(t);

    return date.toISOString().substring(11, 19);
  };
};
