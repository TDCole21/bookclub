-- Deletes from two tables
DELETE Actors, Film_Actor
FROM Actors
INNER JOIN Film_Actor ON Actors.Actor_ID = Film_Actor.ActorID
WHERE Actors.Actor_Name='Harrison Ford';

-- Deletes from two independent tables
DELETE Actors, Film_Actor, Films
FROM Actors
INNER JOIN Films ON Films.Film_ID = Film_Actor.FilmID
WHERE Film_Actor.ActorID = (SELECT Actor_ID from Actors WHERE Actor_Name='Harrison Ford');

-- Dissociate a film from an actor
DELETE Actors, Film_Actor FROM Actors INNER JOIN Film_Actor ON Actors.Actor_ID = Film_Actor.ActorID WHERE Actors.Actor_Name="Will Smith"


-- Select from two independent tables
SELECT *
FROM Actors
INNER JOIN Film_Actor ON Actors.Actor_ID = Film_Actor.ActorID
WHERE Actors.Actor_Name='Harrison Ford';


select * from Films where Film_ID in (select FilmID from Film_Actor)
select Film_Name from Films where Film_ID in (select FilmID from Film_Actor where ActorID=(SELECT Actor_ID from Actors WHERE Actor_Name='Harrison Ford'));

-- Update two independent tables
cur.execute("UPDATE Actors SET Actor_Name=(%s) WHERE Actor_Name=(%s)", [toname, fromname])
cur.execute("INSERT INTO Film_Actor VALUES((SELECT Film_ID from Films WHERE Film_Name=(%s), (SELECT Actor_ID from Actors WHERE Actor_Name=(%s))))", [actorname, filmname])

INSERT INTO Film_Actor VALUES ((SELECT Film_ID from Films WHERE Film_Name='Star Wars: The Force Awakens'), (SELECT Actor_ID from Actors WHERE Actor_Name='Harrison Ford'));
INSERT INTO Film_Actor VALUES ((SELECT Film_ID from Films WHERE Film_Name="Shrek 2"), (SELECT Actor_ID from Actors WHERE Actor_Name="Eddie Murphy"));
INSERT INTO Film_Actor VALUES ((SELECT Film_ID from Films WHERE Film_Name=(%s)), (SELECT Actor_ID from Actors WHERE Actor_Name=(%s)));



SELECT Films.Films_Name, Users.Users_Name, Streaming_Platforms.Streaming_Platforms_Name
FROM ((Films
INNER JOIN Users ON Films.Users_ID=Users.Users_ID)
INNER JOIN Streaming_Platforms ON Films.Streaming_Platforms_ID=Streaming_Platforms.Streaming_Platforms_ID);