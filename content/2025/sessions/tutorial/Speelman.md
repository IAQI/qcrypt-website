---
title: "Tutorial Talk: Quantum position verification: where are we now?"
format: tutorial
type: sessions
year: 2025
speakers:
    - Speelman
chair: Ian George
presentation: null
draft: false
videoId: null
---

## Biography

Florian Speelman is assistant professor at the Theoretical Computer Science group of the University of Amsterdam and affiliated with the QuSoft research center for quantum computing. His research interests include cryptographic protocols for quantum networks, quantum complexity theory, and theoretical questions in quantum communication.

## Abstract

Location can be strongly correlated to trust and identity: For example, when visiting a bank, you might trust the teller just by virtue of her position behind the counter. We would like to be able to use position as a cryptographic credential, being able to encrypt messages that can only be read at a certain location, or signing messages so that we are sure that they are sent from a promised spot.

In this tutorial, we will study the task of quantum position verification (QPV) - where an untrusted party uses quantum information to prove their location, which enables more advanced tasks such as encrypting messages to be only read at a certain location. This is impossible to achieve if all communication and computation is classical, even under computational assumptions, and is an exciting possible use of quantum communication.

In the session, we will start with an overview of basic protocols, inspired by BB84 quantum key distribution, and their security proofs. We will then go over some experimental obstacles on implementing such protocols in practice, and how to modify the protocols to overcome them. On the theoretical side, the QPV task turns out to be connected to the AdS/CFT correspondence, and to various topics in quantum communication and cryptography, because attacks require a form of non-local quantum computation (NLQC). We will go over these connections, and survey open questions on this topic.
