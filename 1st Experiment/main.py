import re

string = """
<h1>Random Quote Generator</h1>
<h1>Random Quote Generator</h1>
<div class="white-box">
  <div class="quote">
    <i class="fa fa-quote-left fa-3x"></i> 
    <p class="random-quote"> <span id="text"></span></p>
  </div>
  <div class="random-author">- <span id="author"></span>
  </div>
  <div class= "buttons">
    
<a id="tweet" href=""https://twitter.com/intent/tweet"" title="Tweet this!"><button class= "button"><i class= "fa fa-twitter"></i></button></a>
    
    <div class= "new-quote-button" >
    <button class="button" id="new-quote"> New Quote
    </div>
  </div>
</div>
"""

string = re.sub("<.*?>"," ", string)
string = re.sub(" *\n","", string)
print(string)