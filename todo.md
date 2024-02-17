Chill a bit more
Get all tags
Get peaks
Get non government investors
Get all funding rounds
The alternative is to look up against existing firm data
Can do both, since I can figure out how to use the data while I'm fetching the data in the first place

let listItems = document.querySelectorAll('mat-list-item[data-cy="industry"]') 

let textContents = [];
for (var i = 0; i < listItems.length; i++) {
    textContents.push(listItems[i].textContent.trim());
}

console.log(textContents);

listItems = document.querySelectorAll('mat-list-item[data-cy="industry"]') 
textContents = [];
for (var i = 0; i < listItems.length; i++) {
    textContents.push(listItems[i].textContent.trim());
}

console.log(textContents);

let get_industries = () => {
  let listItems = document.querySelectorAll('mat-list-item[data-cy="industry"]') 
  let textContents = []
  for (let i = 0; i < listItems.length; i++) {
      textContents.push(listItems[i].textContent.trim())
  }

  console.log(textContents)
}