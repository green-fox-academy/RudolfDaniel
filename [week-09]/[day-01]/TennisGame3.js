'use strict';

var TennisGame3 = function(player1Name, player2Name) {
  this.matchScore1 = 0;
  this.matchScore2 = 0;

  this.player1Name = player1Name;
  this.player2Name = player2Name;
};

TennisGame3.prototype.getScore = function() {
  var s;
  if ((this.matchScore1 < 4 && this.matchScore2 < 4) && (this.matchScore1 + this.matchScore2 < 6)) {
      var p = ['Love', 'Fifteen', 'Thirty', 'Forty'];
      s = p[this.matchScore1];
      return (this.matchScore1 == this.matchScore2) ? s + '-All' : s + '-' + p[this.matchScore2];
  } else {
      if (this.matchScore1 == this.matchScore2)
          return 'Deuce';
      s = this.matchScore1 > this.matchScore2 ? this.player1Name : this.player2Name;
      return ((this.matchScore1 - this.matchScore2) * (this.matchScore1 - this.matchScore2) == 1) ? 'Advantage ' + s : 'Win for ' + s;
  }
};

TennisGame3.prototype.wonPoint = function(playerName) {
  if (playerName == 'player1')
      this.matchScore1 += 1;
  else
      this.matchScore2 += 1;

};

if (typeof window === 'undefined') {
  module.exports = TennisGame3;
}