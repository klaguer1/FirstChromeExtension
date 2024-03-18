chrome.tabs.onUpdated.addListener(function (tabId, changeInfo, tab) {
  // Check if the updated tab has a URL
  if (tab.url) {
    if (tab.url.includes("google.com/search")) {
      // Handle Google searches - You can perform actions specific to Google searches here
      // For example, extract search query or perform some specific logic
      const queryParameters = tab.url.split("?")[1];
      const urlParameters = new URLSearchParams(queryParameters);
      chrome.tabs.sendMessage(tab.id, {
        type: "GOOGLE_SEARCH",
        searchText: urlParameters.get("q"),
      });
    }
  }
});
