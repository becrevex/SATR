# AFI-redteam
This interface was written in Python and converted to an executable with pyinstaller.  

Download the EXE and the XLS.  The EXE will read the XLS file and populate the interface.  

There are a few ascii encoding bugs in the UI as it attempts to read the XLS file contents.  
It's actually kind of a pain, but I will work through these as I find them.  

You can also let me know if you come across them.  

-q0m


--|--

A principle of AFI is that tools and attacks come and go, so it’s arbitrary to learn them. The complexity of syntax with regard to advanced commands and attacks is simply not necessary to memorize. What is important is knowing what to do and when to do it. This concept resulted in the redteam AFI; a collection of tactics, techniques, and procedures used in adversarial engagements.

The module’s left ItemBox contains categories based on and organized by a standard penetration testing methodology. Each category has a series of techniques, tactics, and procedures that can be quickly identified and implemented during an adversarial engagement.

While portscanning is completely acceptible in a lab environment, in the wild, targeted scanning works best. Targeted scanning is finding specific targets and target servifes or vulnerabilities you already know how to exploit. AIC Rule: Once you become familiar with exploiting a particular service or executing a specific vulnerability, index it and develop a way to scan just for that weakness.

Delivery methods are ways to initially compromsie a host. Techniques in this realm constantly become obsolete so creatively (and social engineering) is important to successful unauthorized execution. AIC Rule: Understand what works and what doesn't. This step has a higher chance of being successful if adequate recon and enumeration are performed. Always test delivery methods in a lab environment before taking the attack live.

An offensive attack is typically a collection of techniques and tactics to Destroy, Surveil, or Thieve aspects of data or network confidentiality, availability or integrity. AIC Rule: Know and understand offensive attacks. Operationalize a collection of offensive attack tools and source where they can be carried out at a moments notice.

Post-exploitation is the most important aspect of an attack or live engagement. Gaining access is just the tip of the iceberg. It's what you do after you've gained access that will have the most impact. AIC Rule: Plan your post-exploitation attack path prior to exploitation. You don't want to be sitting on a comrpomised asset thinking about what to do next.

Native techniques to get code or tools on a system are critical tactics in any environment. Both upload and download methods should be learned and mastered. AIC Rule: Become more than familiar with numerous NATIVE ways to perform upload and download actions. If one fails or is blocked, various fall backs will be necessary to continue infiltration.

Native techniques to get code or tools on a system are critical tactics in any environment. Both upload and download methods should be learned and mastered. AIC Rule: Become more than familiar with numerous NATIVE ways to perform upload and download actions. If one fails or is blocked, various fall backs will be necessary to continue infiltration.

Once comrpromised, it's often necessary to initiate a persistence technique (or two) to ensure future access to the system. There are a plethora of ways to do this. The most common being adding a local user or createing an autorun shell or reverse shell. AIC Rule: Persistence can get you in trouble. Utilize persistence techniques sparingly. Know what you're targeting and why you're there and you wont need persistence.

Never leave any artifacts behind. This is a critical step that a lot of inexperienced hackers forget. Always cover your tracks and eliminate any evidence that you were there.

Part of post-exploitation, situational awareness techniques are used to understand the network you've just gained access to. It's a must that these techniques are memorized and mastered. Time is of the essence once you've gained access to a machine. Effective attack planning should more or less have most of these steps layed out before compromise occurs. AIC Rule: Ensure postex scripts, enumerated commands, and/or procedures are always internet accessible to you. Having access to them and memorizing their URI's are a must. It is imperative that local and network recon tactics are highly available.

When landing on a machine in the middle of a network envision yourself moving around and laterally compromise neighboring systems. There are numerous techniques to do this. AIC Rule: There is always another place to go and another asset to attack and compromise -- that 's the nature (and beauty) of networking. Where you are is always a jump off or pivot point. Use that location to explore and infiltrate. Scan for services and vulnerabilities, never port scan.

Once a system is compromised, locating sensitive data is usually the initial and primary goal. AIC Rule: Commit to memory the techniques to search for files and sensitive data via the command line; where sensitive data is and how it can be found via the command line (and what are you going to do with it after you've found it). Find unique ways to search for sensitive data that flies under the radar. Some items to always go for: credentials, CCN, SSN, certificates, emails, history, bookmarks, encryption keys, content on removable media.

Exfiltration Techniques are ways to get data from one private network to another -- usually without triggering too many alarms. The goal is to either do it all in one fell swoop or to trickle out the data low and slow on a channel that's not typically monitored for anomalous activity. AIC Rule: All data is important. Think of ways to get data from an asset/network to a place you can analyze or archive it later. Acquire sensitive data whenever possible and utilize exfiltration techniques to stay covert.
