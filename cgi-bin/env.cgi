#!/usr/bin/perl

print "Content-type: text/plain\n\n";

foreach $var (sort keys %ENV) {
   print "$var=\"$ENV{$var}\"\n";
}

