﻿using System.Linq;

public class House
{
    private static string[][] words = new[] {
        new[] {"","horse and the hound and the horn"},
        new[] {"belonged to","farmer sowing his corn"},
        new[] {"kept","rooster that crowed in the morn"},
        new[] {"woke","priest all shaven and shorn"},
        new[] {"married","man all tattered and torn"},
        new[] {"kissed","maiden all forlorn"},
        new[] {"milked","cow with the crumpled horn"},
        new[] {"tossed","dog"},
        new[] {"worried","cat"},
        new[] {"killed","rat"},
        new[] {"ate","malt"},
        new[] {"lay in","house that Jack built."},
    }.Reverse().ToArray();
    public static string Verse(int i) => Verse(i - 1, true);
    private static string Verse(int i, bool start) =>
        $"{(start ? "This is" : $"that {words[i][0]}")} the {words[i][1]}{(i == 0 ? string.Empty : $"\n{Verse(i - 1, false)}")}";
    public static string Verses(int start, int stop) =>
        string.Join("\n\n", Enumerable.Range(start, stop - start + 1).Select(i => Verse(i)));
    public static string Rhyme() => Verses(1, words.Length);
}