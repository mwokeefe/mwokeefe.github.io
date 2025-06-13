title: Monitoring luminosity at the LHC using the Z boson
date: 23/02/2021

# Introduction
When you’re smashing protons together at nearly the speed of light inside the Large Hadron Collider (LHC), keeping track of how often those collisions happen — and under what conditions — is absolutely critical. That’s where the concept of luminosity comes in.

During Run 2 of the LHC, from 2015 to 2018, the ATLAS experiment at CERN reached unprecedented levels of collision activity. But how do we know — with precision — how many collisions actually occurred? Traditionally, this has been the job of specialized detectors like LUCID. But as it turns out, the humble Z boson, a well-understood particle from the Standard Model, can also serve as a powerful tool to monitor luminosity.

Let me walk you through how.

# What Is Luminosity, and Why Does It Matter?
In high-energy physics, luminosity measures the number of potential collisions per area over time — think of it as the brightness of the proton beams. High luminosity means more data and greater chances of spotting rare processes. But high luminosity also brings complications, like increased “pileup” — overlapping events in the detector that can muddy results.

Precise luminosity measurements are essential for calculating cross-sections — the probabilities of various particle interactions. And those calculations, in turn, are the backbone of much of our understanding of particle physics.

# Z Bosons as Luminosity Probes
Enter the Z boson: a particle that decays into a pair of electrons or muons with a signature that’s easy to spot amid the chaos of a proton-proton collision. Because we know so much about how often Z bosons are produced and how they decay, counting them gives us a reliable indicator of how many collisions have taken place.

During Run 2, ATLAS was able to monitor these Z → ℓ⁺ℓ⁻ decays (where ℓ is either an electron or muon) every minute. With high-energy leptons selected by strict criteria (e.g. transverse momentum > 27 GeV and invariant mass between 66 and 116 GeV), the number of Z events turned out to be a surprisingly precise luminosity tool — offering about 2–4% statistical precision when averaged over 20 minutes.

# Correcting for Detector Realities
Of course, this kind of measurement isn’t plug-and-play. You have to account for inefficiencies in triggering and reconstructing particles, dead time in data acquisition, and even subtleties like the impact of overlapping interactions (pileup).

ATLAS handled this using two methods:

Tag-and-Probe Technique — Real data is used to measure how often detectors correctly trigger and reconstruct one of the leptons from a Z decay, by comparing it to the "other" lepton in the same event.
Monte Carlo Simulations — These help correct for anything the tag-and-probe method misses, like correlations between the two leptons or detector-specific quirks.
Together, these methods give a clean, corrected rate of Z boson decays that can be translated into an instantaneous luminosity value.

# Why Use Z Bosons at All?
While not yet competitive with primary methods like LUCID for absolute luminosity, Z boson counting offers something equally valuable: stability and independence. It's a cross-check that doesn’t rely on the same assumptions or calibration methods. It’s especially useful for comparing ATLAS and CMS measurements or for catching shifts in detector performance over time.

What’s more, the results from Z → e⁺e⁻ and Z → μ⁺μ⁻ agree beautifully — within 1% across all of Run 2 — demonstrating the robustness of the method.

# Final Thoughts
Using physics itself to calibrate physics may sound meta, but it’s part of what makes experiments like ATLAS so powerful. The ability to use well-modeled processes like Z boson decays to monitor detector performance in real time adds a new layer of confidence to every analysis that follows.
And as we head into higher luminosities and more complex data in Run 3 and beyond, having multiple, independent ways to validate our measurements isn’t just nice — it’s essential.

If you would like to read more, the full details can be found in [this paper](https://cds.cern.ch/record/2752951/files/ATL-DAPR-PUB-2021-001.pdf).