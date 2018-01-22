'use strict';

var TennisGame3 = function(player1Name, player2Name) {
  this.matchScore1 = 0;
  this.matchScore2 = 0;
  this.player1Name = player1Name;
  this.player2Name = player2Name;
};

TennisGame3.prototype.getScore = function() {
  let score;
  if ((this.matchScore1 < 4 && this.matchScore2 < 4) && (this.matchScore1 + this.matchScore2 < 6)) {
      var point = ['Love', 'Fifteen', 'Thirty', 'Forty'];
      score = point[this.matchScore1];
      return (this.matchScore1 == this.matchScore2) ? score + '-All' : score + '-' + point[this.matchScore2];
  } else {
      if (this.matchScore1 == this.matchScore2)
          return 'Deuce';
      score = this.matchScore1 > this.matchScore2 ? this.player1Name : this.player2Name;
      return ((this.matchScore1 - this.matchScore2) * (this.matchScore1 - this.matchScore2) == 1) ? 'Advantage ' + score : 'Win for ' + score;
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