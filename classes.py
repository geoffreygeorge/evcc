class bowlingObj:
    def __init__(self, number, player, team, matches, innings, overs, runs, wickets, average, economy, strikerate, hattrick, fourwickets, fivewickets, wides, noballs, balls):
        self._number = number
        self._player = player
        self._team = team
        self._matches = matches
        self._innings = innings
        self._overs = overs
        self._runs = runs
        self._wickets = wickets
        self._average = average
        self._economy = economy
        self._strikerate = strikerate
        self._hattrick = hattrick
        self._fourwickets = fourwickets
        self._fivewickets = fivewickets
        self._wides = wides
        self._noballs = noballs
        self._balls = balls

    def __repr__(self):
        return "['%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s']\n"  % (self._number, self._player, self._team, self._matches, self._innings, self._overs, self._runs, self._wickets, self._average, self._economy, self._strikerate, self._hattrick, self._fourwickets, self._fivewickets, self._wides, self._noballs)

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s \n" % (self._number, self._player, self._team, self._matches, self._innings, self._overs, self._runs, self._wickets, self._average, self._economy, self._strikerate, self._hattrick, self._fourwickets, self._fivewickets, self._wides, self._noballs)

    # getter method 
    def get_number(self): 
        return self._number 
      
    # setter method 
    def set_number(self, number): 
        self._number = number

    # getter method 
    def get_player(self): 
        return self._player 
      
    # setter method 
    def set_player(self, player): 
        self._player = player 

    # getter method 
    def get_team(self): 
        return self._team 
      
    # setter method 
    def set_team(self, team): 
        self._team = team 

    # getter method 
    def get_matches(self): 
        return self._matches
      
    # setter method 
    def set_matches(self, matches): 
        self._matches =  matches

    # getter method 
    def get_innings(self): 
        return self._innings 
      
    # setter method 
    def set_innings(self, innings): 
        self._innings = innings 

    # getter method 
    def get_overs(self): 
        return self._overs
      
    # setter method 
    def set_overs(self, overs): 
        self._overs = overs 

    # getter method 
    def get_runs(self): 
        return self._runs
      
    # setter method 
    def set_runs(self, runs): 
        self._runs = runs

    # getter method 
    def get_wickets(self): 
        return self._wickets
      
    # setter method 
    def set_wickets(self, wickets): 
        self._wickets = wickets 

    # getter method 
    def get_average(self): 
        return self._average
      
    # setter method 
    def set_average(self, average): 
        self._average = average

    # getter method 
    def get_economy(self): 
        return self._economy
      
    # setter method 
    def set_economy(self, economy): 
        self._economy = economy 

    # getter method 
    def get_strikerate(self): 
        return self._strikerate
      
    # setter method 
    def set_strikerate(self, strikerate): 
        self._strikerate = strikerate 

    # getter method 
    def get_hattrick(self): 
        return self._hattrick
      
    # setter method 
    def set_hattrick(self, hattrick): 
        self._hattrick = hattrick

    # getter method 
    def get_fourwickets(self): 
        return self._fourwickets
      
    # setter method 
    def set_fourwickets(self, fourwickets): 
        self._fourwickets = fourwickets 

    # getter method 
    def get_fivewickets(self): 
        return self._fivewickets
      
    # setter method 
    def set_fivewickets(self, fivewickets): 
        self._fivewickets = fivewickets 

    # getter method 
    def get_wides(self): 
        return self._wides
      
    # setter method 
    def set_wides(self, wides): 
        self._wides = wides 

    # getter method 
    def get_noballs(self): 
        return self._noballs
      
    # setter method 
    def set_noballs(self, noballs): 
        self._noballs = noballs

    # getter method 
    def get_balls(self): 
        return self._balls
      
    # setter method 
    def set_balls(self, balls): 
        self._balls = balls


class battingObj:
 
    def __init__(self, number, player, team, matches, innings, notout, runs, balls, average, strikerate, highscore, hundreds, seventyfive, fifties, twentyfive, zeros, fours, sixes):
        self._number = number
        self._player = player
        self._team = team
        self._matches = matches
        self._innings = innings
        self._notout = notout
        self._runs = runs
        self._balls = balls
        self._average = average
        self._strikerate = strikerate
        self._highscore = highscore
        self._hundreds = hundreds
        self._seventyfive = seventyfive
        self._fifties = fifties
        self._twentyfive = twentyfive
        self._zeros = zeros
        self._fours = fours
        self._sixes = sixes

    def __repr__(self):
        return "['%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s']\n"  % (self._number, self._player, self._team, self._matches, self._innings, self._notout, self._runs, self._balls, self._average, self._strikerate, self._highscore, self._hundreds, self._seventyfive, self._fifties, self._twentyfive, self._zeros, self._fours, self._sixes)

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s \n" % (self._number, self._player, self._team, self._matches, self._innings, self._notout, self._runs, self._balls, self._average, self._strikerate, self._highscore, self._hundreds, self._seventyfive, self._fifties, self._twentyfive, self._zeros, self._fours, self._sixes)

    # getter method 
    def get_number(self): 
        return self._number 
      
    # setter method 
    def set_number(self, number): 
        self._number = number 

    # getter method 
    def get_player(self): 
        return self._player 
      
    # setter method 
    def set_player(self, player): 
        self._player = player 

    # getter method 
    def get_team(self): 
        return self._team 
      
    # setter method 
    def set_team(self, team): 
        self._team = team 

    # getter method 
    def get_matches(self): 
        return self._matches
      
    # setter method 
    def set_matches(self, matches): 
        self._matches =  matches

    # getter method 
    def get_innings(self): 
        return self._innings 
      
    # setter method 
    def set_innings(self, innings): 
        self._innings = innings 

    # getter method 
    def get_notout(self): 
        return self._notout 
      
    # setter method 
    def set_notout(self, notout): 
        self._notout =  notout

    # getter method 
    def get_runs(self): 
        return self._runs 
      
    # setter method 
    def set_runs(self, runs): 
        self._runs = runs

    # getter method 
    def get_balls(self): 
        return self._balls 
      
    # setter method 
    def set_balls(self, balls): 
        self._balls = balls 

    # getter method 
    def get_average(self): 
        return self._average 
      
    # setter method 
    def set_average(self, average): 
        self._average = average 

    # getter method 
    def get_strikerate(self): 
        return self._strikerate 
      
    # setter method 
    def set_strikerate(self, strikerate): 
        self._strikerate = strikerate 

    # getter method 
    def get_highscore(self): 
        return self._highscore 
      
    # setter method 
    def set_highscore(self, highscore): 
        self._highscore = highscore 

    # getter method 
    def get_hundreds(self): 
        return self._hundreds 
      
    # setter method 
    def set_hundreds(self, hundreds): 
        self._hundreds = hundreds 

    # getter method 
    def get_seventyfive(self): 
        return self._seventyfive 
      
    # setter method 
    def set_seventyfive(self, seventyfive): 
        self._seventyfive = seventyfive 

    # getter method 
    def get_fifties(self): 
        return self._fifties 
      
    # setter method 
    def set_fifties(self, fifties): 
        self._fifties = fifties 

    # getter method 
    def get_twentyfive(self): 
        return self._twentyfive 
      
    # setter method 
    def set_twentyfive(self, twentyfive): 
        self._twentyfive = twentyfive 

    # getter method 
    def get_zeros(self): 
        return self._zeros 
      
    # setter method 
    def set_zeros(self, zeros): 
        self._zeros = zeros 

    # getter method 
    def get_fours(self): 
        return self._fours 
      
    # setter method 
    def set_fours(self, fours): 
        self._fours = fours 

    # getter method 
    def get_sixes(self): 
        return self._sixes 
      
    # setter method 
    def set_sixes(self, sixes): 
        self._sixes = sixes 

class fieldingObj:
 
    def __init__(self, number, player, team, catches, wkcatches, directro, indirectro, stumpings, total):

        self._number = number
        self._player = player
        self._team = team
        self._catches = catches
        self._wkcatches = wkcatches
        self._directro = directro
        self._indirectro = indirectro
        self._stumpings = stumpings
        self._total = total

    def __repr__(self):
        return "['%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s']\n"  % (self._number, self._player, self._team, self._catches, self._wkcatches, self._directro, self._indirectro, self._stumpings, self._total)

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s \n" % (self._number, self._player, self._team, self._catches, self._wkcatches, self._directro, self._indirectro, self._stumpings, self._total)


    # getter method 
    def get_number(self): 
        return self._number 
      
    # setter method 
    def set_number(self, number): 
        self._number = number 

    # getter method 
    def get_player(self): 
        return self._player 
      
    # setter method 
    def set_player(self, player): 
        self._player = player 

    # getter method 
    def get_team(self): 
        return self._team 
      
    # setter method 
    def set_team(self, team): 
        self._team = team 

    # getter method 
    def get_catches(self): 
        return self._catches 
      
    # setter method 
    def set_catches(self, catches): 
        self._catches = catches 

    # getter method 
    def get_wkcatches(self): 
        return self._wkcatches 
      
    # setter method 
    def set_wkcatches(self, wkcatches): 
        self._wkcatches = wkcatches 

    # getter method 
    def get_directro(self): 
        return self._directro 
      
    # setter method 
    def set_directro(self, directro): 
        self._directro = directro 

    # getter method 
    def get_indirectro(self): 
        return self._indirectro
      
    # setter method 
    def set_indirectro(self, indirectro): 
        self._indirectro = indirectro 

    # getter method 
    def get_stumpings(self): 
        return self._stumpings 
      
    # setter method 
    def set_stumpings(self, stumpings): 
        self._stumpings = stumpings 

    # getter method 
    def get_total(self): 
        return self._total 
      
    # setter method 
    def set_total(self, total): 
        self._total = total 
