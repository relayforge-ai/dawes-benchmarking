# IUK Bank — T3 Specialist/PhD
**Total questions:** 425
**Default weight:** 3.5×
**Pass gate:** ≥65%

## Sources
- `IUK_v3_IUK_v3_T3_diagnostic`: 296Q
- `IUK_upgrade_IUK_T3_specialist_560_upgrade`: 125Q
- `IUK_mastery_textualized_IUK_MASTERY_INST200_x1_mastery_v01_textualized`: 3Q
- `IUK_mastery_textualized_IUK_MASTERY_INST251_x2_mastery_textualized`: 1Q

## Format breakdown
- `full_iuk`: 296Q
- `iuk_upgrade_filled`: 125Q
- `iuk_mastery_textualized`: 4Q

## Block coverage
- Block 10 - Safety & Leadership: 60Q
- Block 9 - Advanced Diagnostic: 40Q
- Block 11 - ICS Cybersecurity: 25Q
- Mastery Exam (Kuphaldt): 4Q

---

## IUK-T3-560-CYBER-001
**Block:** Block 11 - ICS Cybersecurity  
**Tier:** T3 · Specialist/PhD  
**Type:** COMPARE  
**Weight:** 3.5×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
What does ISA/IEC 62443 define as a Security Level (SL), and what is the difference between SL-T (target) and SL-C (capability)?

**Correct Answer:**  
SL-T is the desired security level for a zone or conduit; SL-C is what a product or system can actually achieve. The design must ensure SL-C meets or exceeds SL-T.

**Required Elements:**
- SL-T is the desired security level for a zone or conduit
- SL-C is what a product or system can actually achieve
- The design must ensure SL-C meets or exceeds SL-T

**Common Wrong Answers:**
- SL-T and SL-C are the same number; one is used by IT and one by OT.
- SL-C may be lower than SL-T as long as the firewall is modern.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — all 3 required elements present and accurate |  
| Partial (high) | 7/10 — 2 of 3 elements correct |  
| Partial (low) | 4/10 — partial answer, key element missing |  
| Zero | 0/10 — incorrect or missing core concept |

**Confidence Penalty Trigger:** model conflates the two systems or misattributes a property to the wrong standard

**Reference:** ISA/IEC 62443; NIST SP 800-82; NERC CIP

**Difficulty Rationale:** T3 Specialist (3.5×) because ICS Cybersecurity requires understanding of two distinct systems and their domain-specific tradeoffs

---

## IUK-T3-560-CYBER-002
**Block:** Block 11 - ICS Cybersecurity  
**Tier:** T3 · Specialist/PhD  
**Type:** IDENTIFY  
**Weight:** 3.5×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
In the Purdue Model applied to OT security, what are the five functional levels (0 through 4)?

**Correct Answer:**  
Level 0: Field devices (sensors, actuators). Level 1: Basic control (PLCs, DCS controllers). Level 2: Supervisory/SCADA/HMI. Level 3: Operations management/MES/historians. Level 4: Business/ERP networks.

**Required Elements:**
- Level 0: Field devices (sensors, actuators)
- Level 1: Basic control (PLCs, DCS controllers)
- Level 2: Supervisory/SCADA/HMI
- Level 3: Operations management/MES/historians
- Level 4: Business/ERP networks

**Common Wrong Answers:**
- Level 0 is the business network and Level 4 is the field devices.
- The Purdue Model has only three levels: enterprise, control room, and field.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — all 5 required elements present and accurate |  
| Partial (high) | 7/10 — 4 of 5 elements correct |  
| Partial (low) | 4/10 — partial answer, key element missing |  
| Zero | 0/10 — incorrect or missing core concept |

**Confidence Penalty Trigger:** model states a definition without citing the applicable standard or first principle

**Reference:** ISA/IEC 62443; NIST SP 800-82; NERC CIP

**Difficulty Rationale:** T3 Specialist (3.5×) because ICS Cybersecurity requires precise recall of a standard or principle with correct scope

---

## IUK-T3-560-CYBER-003
**Block:** Block 11 - ICS Cybersecurity  
**Tier:** T3 · Specialist/PhD  
**Type:** DIAGNOSE  
**Weight:** 3.5×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
In OT security architecture, what is an Industrial DMZ (IDMZ), and why is it critical?

**Correct Answer:**  
An IDMZ is a neutral network segment between the OT network (Levels 0-3) and enterprise IT (Levels 4+). It hosts shared services such as historians and patch servers, preventing direct connections between IT and OT.

**Required Elements:**
- An IDMZ is a neutral network segment between the OT network (Levels 0-3) and enterprise IT (Levels 4+)
- It hosts shared services such as historians and patch servers, preventing direct connections between IT and OT

**Common Wrong Answers:**
- An IDMZ is just a firewall rule allowing IT to reach PLCs directly.
- The historian should be placed directly on the DCS control LAN so ERP can poll it faster.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — correct root cause + physical mechanism + correct fix |  
| Partial (high) | 7/10 — correct root cause, mechanism incomplete |  
| Partial (low) | 4/10 — plausible diagnosis but wrong mechanism |  
| Zero | 0/10 — wrong root cause or dangerous recommendation |

**Confidence Penalty Trigger:** model gives a root cause without citing the physical mechanism or reasoning chain

**Reference:** ISA/IEC 62443; NIST SP 800-82; NERC CIP

**Difficulty Rationale:** T3 Specialist (3.5×) because ICS Cybersecurity requires multi-step reasoning from symptoms to root cause — a field-level skill

---

## IUK-T3-560-CYBER-004
**Block:** Block 11 - ICS Cybersecurity  
**Tier:** T3 · Specialist/PhD  
**Type:** COMPARE  
**Weight:** 3.5×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
What is the fundamental difference between IT and OT security priorities?

**Correct Answer:**  
IT prioritizes Confidentiality, Integrity, Availability (CIA) in that order. OT inverts this: Safety and Availability first, then Integrity, then Confidentiality.

**Required Elements:**
- IT prioritizes Confidentiality, Integrity, Availability (CIA) in that order
- OT inverts this: Safety and Availability first, then Integrity, then Confidentiality

**Common Wrong Answers:**
- OT should prioritize confidentiality first because production data is proprietary.
- IT and OT priorities are identical; the same policies can be copied into the plant unchanged.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — all 2 required elements present and accurate |  
| Partial (high) | 7/10 — 1 of 2 elements correct |  
| Partial (low) | 4/10 — partial answer, key element missing |  
| Zero | 0/10 — incorrect or missing core concept |

**Confidence Penalty Trigger:** model conflates the two systems or misattributes a property to the wrong standard

**Reference:** ISA/IEC 62443; NIST SP 800-82; NERC CIP

**Difficulty Rationale:** T3 Specialist (3.5×) because ICS Cybersecurity requires understanding of two distinct systems and their domain-specific tradeoffs

---

## IUK-T3-560-CYBER-005
**Block:** Block 11 - ICS Cybersecurity  
**Tier:** T3 · Specialist/PhD  
**Type:** APPLY  
**Weight:** 3.5×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
A SCADA historian needs to share process data with the business ERP system. What is the recommended secure architecture?

**Correct Answer:**  
Place the historian in the IDMZ with one-way data flow (unidirectional gateway or data diode) from OT to IDMZ, then replicate from IDMZ to the business network. Never allow ERP direct access to the OT network.

**Required Elements:**
- Place the historian in the IDMZ with one-way data flow (unidirectional gateway or data diode) from OT to IDMZ, then replicate from IDMZ to the business network
- Never allow ERP direct access to the OT network

**Common Wrong Answers:**
- Allow the ERP server read-only access directly to the DCS historian on the control network.
- Put the historian on the business network and open inbound firewall ports from DCS controllers.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — all 2 required elements present and accurate |  
| Partial (high) | 7/10 — 1 of 2 elements correct |  
| Partial (low) | 4/10 — partial answer, key element missing |  
| Zero | 0/10 — incorrect or missing core concept |

**Confidence Penalty Trigger:** model asserts without citing supporting reasoning

**Reference:** ISA/IEC 62443; NIST SP 800-82; NERC CIP

**Difficulty Rationale:** T3 Specialist (3.5×) because ICS Cybersecurity requires sequencing a correct procedure, not just identifying one step

---

## IUK-T3-560-CYBER-006
**Block:** Block 11 - ICS Cybersecurity  
**Tier:** T3 · Specialist/PhD  
**Type:** DESIGN  
**Weight:** 3.5×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
What is a unidirectional gateway (data diode), and when would you specify one for a DCS network?

**Correct Answer:**  
A hardware-enforced one-way data transfer device that physically allows data to flow in only one direction. Specified when data must leave the OT network but no commands should ever enter from IT, and software-only firewall rules are not considered sufficient assurance.

**Required Elements:**
- A hardware-enforced one-way data transfer device that physically allows data to flow in only one direction
- Specified when data must leave the OT network but no commands should ever enter from IT, and software-only firewall rules are not considered sufficient assurance

**Common Wrong Answers:**
- A data diode is a firewall configured to block most inbound ports.
- Specify one whenever a normal managed switch is out of ports.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — all 2 required elements present and accurate |  
| Partial (high) | 7/10 — 1 of 2 elements correct |  
| Partial (low) | 4/10 — partial answer, key element missing |  
| Zero | 0/10 — incorrect or missing core concept |

**Confidence Penalty Trigger:** model makes a selection without stating the selection criteria or design constraint

**Reference:** ISA/IEC 62443; NIST SP 800-82; NERC CIP

**Difficulty Rationale:** T3 Specialist (3.5×) because ICS Cybersecurity requires applying selection criteria under real engineering constraints

---

## IUK-T3-560-CYBER-007
**Block:** Block 11 - ICS Cybersecurity  
**Tier:** T3 · Specialist/PhD  
**Type:** IDENTIFY  
**Weight:** 3.5×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
A DCS operator workstation runs Windows XP because the DCS vendor has not certified a newer OS. What compensating controls reduce risk?

**Correct Answer:**  
Application whitelisting, VLAN network isolation, USB port physical disabling, compensating network IDS/monitoring, documented risk acceptance, and regular review of compensating controls.

**Required Elements:**
- Application whitelisting
- VLAN network isolation
- USB port physical disabling, compensating network IDS/monitoring, documented risk acceptance, and regular review of compensating controls

**Common Wrong Answers:**
- Connect it to the corporate patch server and apply all Microsoft updates automatically.
- Risk is acceptable if operators promise not to browse the internet from the HMI.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — all 3 required elements present and accurate |  
| Partial (high) | 7/10 — 2 of 3 elements correct |  
| Partial (low) | 4/10 — partial answer, key element missing |  
| Zero | 0/10 — incorrect or missing core concept |

**Confidence Penalty Trigger:** model states a definition without citing the applicable standard or first principle

**Reference:** ISA/IEC 62443; NIST SP 800-82; NERC CIP

**Difficulty Rationale:** T3 Specialist (3.5×) because ICS Cybersecurity requires precise recall of a standard or principle with correct scope

---

## IUK-T3-560-CYBER-008
**Block:** Block 11 - ICS Cybersecurity  
**Tier:** T3 · Specialist/PhD  
**Type:** IDENTIFY  
**Weight:** 3.5×  
**Safety Gate:** YES  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
What is the principle of least privilege in an ICS context?

**Correct Answer:**  
Each user, process, or device should have only the minimum access rights required to perform its function — nothing more.

**Required Elements:**
- Each user, process, or device should have only the minimum access rights required to perform its function — nothing more

**Common Wrong Answers:**
- Least privilege means giving every operator admin rights so they can fix problems quickly.
- It means using one shared low-privilege account for the whole shift.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — all 1 required elements present and accurate |  
| Partial (high) | 7/10 — 1 of 1 elements correct |  
| Partial (low) | 4/10 — partial answer, key element missing |  
| Zero | 0/10 — incorrect or missing core concept |

**Confidence Penalty Trigger:** model states a definition without citing the applicable standard or first principle; model omits or minimizes the safety implication of an incorrect answer

**Reference:** ISA/IEC 62443; NIST SP 800-82; NERC CIP

**Difficulty Rationale:** T3 Specialist (3.5×) because ICS Cybersecurity requires precise recall of a standard or principle with correct scope

---

## IUK-T3-560-CYBER-009
**Block:** Block 11 - ICS Cybersecurity  
**Tier:** T3 · Specialist/PhD  
**Type:** IDENTIFY  
**Weight:** 3.5×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
In ISA 62443 terminology, what is a Security Zone and what is a Conduit?

**Correct Answer:**  
A Security Zone is a grouping of logical or physical assets sharing the same security requirements, protected as a unit. A Conduit is the communication path and its security controls between two zones.

**Required Elements:**
- A Security Zone is a grouping of logical or physical assets sharing the same security requirements, protected as a unit
- A Conduit is the communication path and its security controls between two zones

**Common Wrong Answers:**
- A zone is a physical room, and a conduit is only a piece of cable tray.
- A conduit is another name for a firewall, while zones are individual IP addresses.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — all 2 required elements present and accurate |  
| Partial (high) | 7/10 — 1 of 2 elements correct |  
| Partial (low) | 4/10 — partial answer, key element missing |  
| Zero | 0/10 — incorrect or missing core concept |

**Confidence Penalty Trigger:** model states a definition without citing the applicable standard or first principle

**Reference:** ISA/IEC 62443; NIST SP 800-82; NERC CIP

**Difficulty Rationale:** T3 Specialist (3.5×) because ICS Cybersecurity requires precise recall of a standard or principle with correct scope

---

## IUK-T3-560-CYBER-010
**Block:** Block 11 - ICS Cybersecurity  
**Tier:** T3 · Specialist/PhD  
**Type:** DIAGNOSE  
**Weight:** 3.5×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
Why is remote VPN access to an ICS a higher security risk than enterprise VPN, and what additional controls are needed?

**Correct Answer:**  
ICS VPN bypasses all physical perimeter controls; a compromised VPN session gives direct access to safety-critical systems. Additional controls: multi-factor authentication, dedicated jump server/bastion host, session recording, time-limited access windows, and role-based access management.

**Required Elements:**
- ICS VPN bypasses all physical perimeter controls
- a compromised VPN session gives direct access to safety-critical systems
- Additional controls: multi-factor authentication, dedicated jump server/bastion host, session recording, time-limited access windows, and role-based access management

**Common Wrong Answers:**
- ICS VPN is safe if the password is long; no jump server or session controls are needed.
- Remote vendors should connect directly to PLCs to avoid delays during support calls.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — correct root cause + physical mechanism + correct fix |  
| Partial (high) | 7/10 — correct root cause, mechanism incomplete |  
| Partial (low) | 4/10 — plausible diagnosis but wrong mechanism |  
| Zero | 0/10 — wrong root cause or dangerous recommendation |

**Confidence Penalty Trigger:** model gives a root cause without citing the physical mechanism or reasoning chain

**Reference:** ISA/IEC 62443; NIST SP 800-82; NERC CIP

**Difficulty Rationale:** T3 Specialist (3.5×) because ICS Cybersecurity requires multi-step reasoning from symptoms to root cause — a field-level skill

---

## IUK-T3-560-CYBER-011
**Block:** Block 11 - ICS Cybersecurity  
**Tier:** T3 · Specialist/PhD  
**Type:** COMPARE  
**Weight:** 3.5×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
What is the difference between a vulnerability and an exploit in OT cybersecurity?

**Correct Answer:**  
A vulnerability is a weakness (software bug, misconfiguration, weak password). An exploit is the mechanism by which an attacker takes advantage of a vulnerability to compromise a system.

**Required Elements:**
- A vulnerability is a weakness (software bug, misconfiguration, weak password)
- An exploit is the mechanism by which an attacker takes advantage of a vulnerability to compromise a system

**Common Wrong Answers:**
- A vulnerability is the attack tool, and an exploit is the missing patch.
- They mean the same thing: any cybersecurity problem on the network.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — all 2 required elements present and accurate |  
| Partial (high) | 7/10 — 1 of 2 elements correct |  
| Partial (low) | 4/10 — partial answer, key element missing |  
| Zero | 0/10 — incorrect or missing core concept |

**Confidence Penalty Trigger:** model conflates the two systems or misattributes a property to the wrong standard

**Reference:** ISA/IEC 62443; NIST SP 800-82; NERC CIP

**Difficulty Rationale:** T3 Specialist (3.5×) because ICS Cybersecurity requires understanding of two distinct systems and their domain-specific tradeoffs

---

## IUK-T3-560-CYBER-012
**Block:** Block 11 - ICS Cybersecurity  
**Tier:** T3 · Specialist/PhD  
**Type:** IDENTIFY  
**Weight:** 3.5×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
A WirelessHART gateway is connected directly to the DCS control network without network segmentation. What is the security concern?

**Correct Answer:**  
WirelessHART networks can be attacked at the wireless layer (e.g., rogue gateway, replay attacks). A compromised gateway connected directly to a flat control network provides a pivot point to attack DCS controllers or other field devices.

**Required Elements:**
- WirelessHART networks can be attacked at the wireless layer (e.g., rogue gateway, replay attacks)
- A compromised gateway connected directly to a flat control network provides a pivot point to attack DCS controllers or other field devices

**Common Wrong Answers:**
- WirelessHART is encrypted, so segmentation is unnecessary.
- The gateway is only a sensor network device and cannot be used as a pivot into the DCS.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — all 2 required elements present and accurate |  
| Partial (high) | 7/10 — 1 of 2 elements correct |  
| Partial (low) | 4/10 — partial answer, key element missing |  
| Zero | 0/10 — incorrect or missing core concept |

**Confidence Penalty Trigger:** model states a definition without citing the applicable standard or first principle

**Reference:** ISA/IEC 62443; NIST SP 800-82; NERC CIP

**Difficulty Rationale:** T3 Specialist (3.5×) because ICS Cybersecurity requires precise recall of a standard or principle with correct scope

---

## IUK-T3-560-CYBER-013
**Block:** Block 11 - ICS Cybersecurity  
**Tier:** T3 · Specialist/PhD  
**Type:** DIAGNOSE  
**Weight:** 3.5×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
What does "air-gap" mean in ICS security, and why is a true air-gap increasingly difficult to maintain in modern industrial plants?

**Correct Answer:**  
An air-gap means no electronic network connection exists between the OT system and any external network. Modern plants increasingly require remote monitoring, vendor support, software updates, and historian data sharing — all of which introduce connections that break a true air-gap.

**Required Elements:**
- An air-gap means no electronic network connection exists between the OT system and any external network
- Modern plants increasingly require remote monitoring, vendor support, software updates, and historian data sharing — all of which introduce connections that break a true air-gap

**Common Wrong Answers:**
- Air-gap means the OT network has a firewall between it and IT.
- A plant remains air-gapped even with vendor remote access if the VPN uses MFA.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — correct root cause + physical mechanism + correct fix |  
| Partial (high) | 7/10 — correct root cause, mechanism incomplete |  
| Partial (low) | 4/10 — plausible diagnosis but wrong mechanism |  
| Zero | 0/10 — wrong root cause or dangerous recommendation |

**Confidence Penalty Trigger:** model gives a root cause without citing the physical mechanism or reasoning chain

**Reference:** ISA/IEC 62443; NIST SP 800-82; NERC CIP

**Difficulty Rationale:** T3 Specialist (3.5×) because ICS Cybersecurity requires multi-step reasoning from symptoms to root cause — a field-level skill

---

## IUK-T3-560-CYBER-014
**Block:** Block 11 - ICS Cybersecurity  
**Tier:** T3 · Specialist/PhD  
**Type:** DIAGNOSE  
**Weight:** 3.5×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
What is application whitelisting in ICS, and why is it preferred over traditional antivirus software on HMI/SCADA stations?

**Correct Answer:**  
Whitelisting allows only pre-approved executables to run. Preferred over traditional AV because: HMI/SCADA stations run a fixed and well-known software set; AV signature updates can interfere with DCS operations; and zero-day threats bypass AV signature detection entirely.

**Required Elements:**
- Whitelisting allows only pre-approved executables to run
- Preferred over traditional AV because: HMI/SCADA stations run a fixed and well-known software set
- AV signature updates can interfere with DCS operations
- and zero-day threats bypass AV signature detection entirely

**Common Wrong Answers:**
- Whitelisting is a list of allowed websites for HMI operators.
- Traditional antivirus is preferred because frequent signature updates are harmless on DCS stations.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — correct root cause + physical mechanism + correct fix |  
| Partial (high) | 7/10 — correct root cause, mechanism incomplete |  
| Partial (low) | 4/10 — plausible diagnosis but wrong mechanism |  
| Zero | 0/10 — wrong root cause or dangerous recommendation |

**Confidence Penalty Trigger:** model gives a root cause without citing the physical mechanism or reasoning chain

**Reference:** ISA/IEC 62443; NIST SP 800-82; NERC CIP

**Difficulty Rationale:** T3 Specialist (3.5×) because ICS Cybersecurity requires multi-step reasoning from symptoms to root cause — a field-level skill

---

## IUK-T3-560-CYBER-015
**Block:** Block 11 - ICS Cybersecurity  
**Tier:** T3 · Specialist/PhD  
**Type:** IDENTIFY  
**Weight:** 3.5×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
An unauthorized USB drive is found plugged into an HMI workstation in the control room. What is the immediate correct response?

**Correct Answer:**  
Do not remove without documentation. Isolate the workstation from the network if safe to do so. Photograph, document, and preserve the scene. Engage the facility cybersecurity incident response team. Check for malware indicators. Report per the facility incident response plan.

**Required Elements:**
- Do not remove without documentation
- Isolate the workstation from the network if safe to do so
- Photograph, document, and preserve the scene
- Engage the facility cybersecurity incident response team
- Check for malware indicators

**Common Wrong Answers:**
- Pull the USB drive immediately and plug it into an office PC to see what is on it.
- Reboot the HMI and keep operating if no alarm appears.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — all 5 required elements present and accurate |  
| Partial (high) | 7/10 — 4 of 5 elements correct |  
| Partial (low) | 4/10 — partial answer, key element missing |  
| Zero | 0/10 — incorrect or missing core concept |

**Confidence Penalty Trigger:** model states a definition without citing the applicable standard or first principle

**Reference:** ISA/IEC 62443; NIST SP 800-82; NERC CIP

**Difficulty Rationale:** T3 Specialist (3.5×) because ICS Cybersecurity requires precise recall of a standard or principle with correct scope

---

## IUK-T3-560-CYBER-016
**Block:** Block 11 - ICS Cybersecurity  
**Tier:** T3 · Specialist/PhD  
**Type:** COMPARE  
**Weight:** 3.5×  
**Safety Gate:** YES  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
What is cyber-physical risk, and how does it differ from a conventional data breach in an OT context?

**Correct Answer:**  
Cyber-physical risk is the potential for a cyber attack to cause physical consequences: equipment damage, process upsets, environmental release, injury, or death. A data breach loses information; a cyber-physical attack can destroy equipment, injure personnel, or kill people.

**Required Elements:**
- Cyber-physical risk is the potential for a cyber attack to cause physical consequences: equipment damage, process upsets, environmental release, injury, or death
- A data breach loses information
- a cyber-physical attack can destroy equipment, injure personnel, or kill people

**Common Wrong Answers:**
- Cyber-physical risk is just loss of production reports or historian data.
- A data breach and a cyber-physical event are equivalent because both are IT incidents.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — all 3 required elements present and accurate |  
| Partial (high) | 7/10 — 2 of 3 elements correct |  
| Partial (low) | 4/10 — partial answer, key element missing |  
| Zero | 0/10 — incorrect or missing core concept |

**Confidence Penalty Trigger:** model conflates the two systems or misattributes a property to the wrong standard; model omits or minimizes the safety implication of an incorrect answer

**Reference:** ISA/IEC 62443; NIST SP 800-82; NERC CIP

**Difficulty Rationale:** T3 Specialist (3.5×) because ICS Cybersecurity requires understanding of two distinct systems and their domain-specific tradeoffs

---

## IUK-T3-560-CYBER-017
**Block:** Block 11 - ICS Cybersecurity  
**Tier:** T3 · Specialist/PhD  
**Type:** DIAGNOSE  
**Weight:** 3.5×  
**Safety Gate:** YES  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
What is patch management in ICS, and why is it more complex than patch management in enterprise IT?

**Correct Answer:**  
ICS patch management involves updating firmware, OS, and applications on field devices, controllers, HMIs, and servers. Complexity arises because: systems may not tolerate downtime; vendor certification is required before patching; patches must be tested in a staging environment; and some legacy systems cannot be patched at all.

**Required Elements:**
- ICS patch management involves updating firmware, OS, and applications on field devices, controllers, HMIs, and servers
- Complexity arises because: systems may not tolerate downtime
- vendor certification is required before patching
- patches must be tested in a staging environment
- and some legacy systems cannot be patched at all

**Common Wrong Answers:**
- ICS patching should follow enterprise IT timelines with automatic overnight updates.
- If a system cannot be patched, it must be ignored until the next vendor upgrade.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — correct root cause + physical mechanism + correct fix |  
| Partial (high) | 7/10 — correct root cause, mechanism incomplete |  
| Partial (low) | 4/10 — plausible diagnosis but wrong mechanism |  
| Zero | 0/10 — wrong root cause or dangerous recommendation |

**Confidence Penalty Trigger:** model gives a root cause without citing the physical mechanism or reasoning chain; model omits or minimizes the safety implication of an incorrect answer

**Reference:** ISA/IEC 62443; NIST SP 800-82; NERC CIP

**Difficulty Rationale:** T3 Specialist (3.5×) because ICS Cybersecurity requires multi-step reasoning from symptoms to root cause — a field-level skill

---

## IUK-T3-560-CYBER-018
**Block:** Block 11 - ICS Cybersecurity  
**Tier:** T3 · Specialist/PhD  
**Type:** IDENTIFY  
**Weight:** 3.5×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
What are the key differences between NERC CIP (electric utilities) and ISA/IEC 62443 (general industry)?

**Correct Answer:**  
NERC CIP is a mandatory compliance framework for the North American bulk electric system with specific controls, audit requirements, and financial penalties for non-compliance. ISA/IEC 62443 is a voluntary, risk-based international standard applicable to all industrial sectors. NERC CIP focuses on grid reliability; ISA 62443 focuses on defense-in-depth for general industrial control systems.

**Required Elements:**
- NERC CIP is a mandatory compliance framework for the North American bulk electric system with specific controls, audit requirements, and financial penalties for non-compliance
- ISA/IEC 62443 is a voluntary, risk-based international standard applicable to all industrial sectors
- NERC CIP focuses on grid reliability
- ISA 62443 focuses on defense-in-depth for general industrial control systems

**Common Wrong Answers:**
- NERC CIP is a voluntary best-practice guide for all plants, while ISA 62443 is mandatory for electric utilities.
- Both frameworks are the same; only the document names differ.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — all 4 required elements present and accurate |  
| Partial (high) | 7/10 — 3 of 4 elements correct |  
| Partial (low) | 4/10 — partial answer, key element missing |  
| Zero | 0/10 — incorrect or missing core concept |

**Confidence Penalty Trigger:** model states a definition without citing the applicable standard or first principle

**Reference:** ISA/IEC 62443; NIST SP 800-82; NERC CIP

**Difficulty Rationale:** T3 Specialist (3.5×) because ICS Cybersecurity requires precise recall of a standard or principle with correct scope

---

## IUK-T3-560-CYBER-019
**Block:** Block 11 - ICS Cybersecurity  
**Tier:** T3 · Specialist/PhD  
**Type:** IDENTIFY  
**Weight:** 3.5×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
In a defense-in-depth model for an industrial facility, what are the four common security layers?

**Correct Answer:**  
(1) Physical security: fences, locks, card access, CCTV. (2) Network segmentation: security zones, firewalls, IDMZ, conduits. (3) Endpoint hardening: application whitelisting, patch management, USB disabling. (4) Monitoring and response: passive OT IDS, anomaly detection, incident response procedures.

**Required Elements:**
- (1) Physical security: fences, locks, card access
- CCTV. (2) Network segmentation: security zones, firewalls
- IDMZ, conduits. (3) Endpoint hardening: application whitelisting, patch management
- USB disabling. (4) Monitoring and response: passive OT IDS, anomaly detection, incident response procedures

**Common Wrong Answers:**
- Defense in depth means installing two firewalls in series and nothing else.
- Physical security does not count as cybersecurity because it is not digital.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — all 4 required elements present and accurate |  
| Partial (high) | 7/10 — 3 of 4 elements correct |  
| Partial (low) | 4/10 — partial answer, key element missing |  
| Zero | 0/10 — incorrect or missing core concept |

**Confidence Penalty Trigger:** model states a definition without citing the applicable standard or first principle

**Reference:** ISA/IEC 62443; NIST SP 800-82; NERC CIP

**Difficulty Rationale:** T3 Specialist (3.5×) because ICS Cybersecurity requires precise recall of a standard or principle with correct scope

---

## IUK-T3-560-CYBER-020
**Block:** Block 11 - ICS Cybersecurity  
**Tier:** T3 · Specialist/PhD  
**Type:** IDENTIFY  
**Weight:** 3.5×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
What is a cybersecurity risk assessment as defined by ISA 62443-3-2, and who typically conducts it?

**Correct Answer:**  
A systematic process to identify assets, threats, vulnerabilities, and consequences; estimate risk levels; and prioritize countermeasures. Conducted by a multi-disciplinary team including process engineers, I\&C engineers, IT/OT security professionals, and operations — not IT alone.

**Required Elements:**
- A systematic process to identify assets, threats, vulnerabilities, and consequences
- estimate risk levels
- and prioritize countermeasures
- Conducted by a multi-disciplinary team including process engineers, I\&C engineers, IT/OT security professionals, and operations — not IT alone

**Common Wrong Answers:**
- An ISA 62443 risk assessment is an IT-only vulnerability scan of Windows servers.
- It only lists assets and does not evaluate consequences or countermeasures.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — all 4 required elements present and accurate |  
| Partial (high) | 7/10 — 3 of 4 elements correct |  
| Partial (low) | 4/10 — partial answer, key element missing |  
| Zero | 0/10 — incorrect or missing core concept |

**Confidence Penalty Trigger:** model states a definition without citing the applicable standard or first principle

**Reference:** ISA/IEC 62443; NIST SP 800-82; NERC CIP

**Difficulty Rationale:** T3 Specialist (3.5×) because ICS Cybersecurity requires precise recall of a standard or principle with correct scope

---

## IUK-T3-560-CYBER-021
**Block:** Block 11 - ICS Cybersecurity  
**Tier:** T3 · Specialist/PhD  
**Type:** DIAGNOSE  
**Weight:** 3.5×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
Why is default password management a critical vulnerability in ICS field devices?

**Correct Answer:**  
Many PLCs, RTUs, HMIs, and smart instruments ship with default, publicly documented credentials. If unchanged, an attacker with any network access can gain full control using credentials freely available online or in vendor manuals.

**Required Elements:**
- Many PLCs, RTUs, HMIs, and smart instruments ship with default, publicly documented credentials
- If unchanged, an attacker with any network access can gain full control using credentials freely available online or in vendor manuals

**Common Wrong Answers:**
- Default passwords are acceptable on isolated PLC networks.
- Changing default passwords is unnecessary if the device cabinet is locked.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — correct root cause + physical mechanism + correct fix |  
| Partial (high) | 7/10 — correct root cause, mechanism incomplete |  
| Partial (low) | 4/10 — plausible diagnosis but wrong mechanism |  
| Zero | 0/10 — wrong root cause or dangerous recommendation |

**Confidence Penalty Trigger:** model gives a root cause without citing the physical mechanism or reasoning chain

**Reference:** ISA/IEC 62443; NIST SP 800-82; NERC CIP

**Difficulty Rationale:** T3 Specialist (3.5×) because ICS Cybersecurity requires multi-step reasoning from symptoms to root cause — a field-level skill

---

## IUK-T3-560-CYBER-022
**Block:** Block 11 - ICS Cybersecurity  
**Tier:** T3 · Specialist/PhD  
**Type:** DIAGNOSE  
**Weight:** 3.5×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
Scenario: A SCADA historian is sending data to an unknown external IP address every 15 minutes. What ICS security control should have detected this?

**Correct Answer:**  
Network monitoring or anomaly detection using OT-specific passive monitoring tools (e.g., Claroty, Dragos, Nozomi Networks) configured with baseline traffic profiles and alerting on unauthorized outbound connections or anomalous communication patterns.

**Required Elements:**
- Network monitoring or anomaly detection using OT-specific passive monitoring tools (e.g.
- Nozomi Networks) configured with baseline traffic profiles and alerting on unauthorized outbound connections or anomalous communication patterns

**Common Wrong Answers:**
- Antivirus on the historian alone should detect all unauthorized outbound traffic.
- A monthly spreadsheet review of IP addresses is sufficient monitoring.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — correct root cause + physical mechanism + correct fix |  
| Partial (high) | 7/10 — correct root cause, mechanism incomplete |  
| Partial (low) | 4/10 — plausible diagnosis but wrong mechanism |  
| Zero | 0/10 — wrong root cause or dangerous recommendation |

**Confidence Penalty Trigger:** model gives a root cause without citing the physical mechanism or reasoning chain

**Reference:** ISA/IEC 62443; NIST SP 800-82; NERC CIP

**Difficulty Rationale:** T3 Specialist (3.5×) because ICS Cybersecurity requires multi-step reasoning from symptoms to root cause — a field-level skill

---

## IUK-T3-560-CYBER-023
**Block:** Block 11 - ICS Cybersecurity  
**Tier:** T3 · Specialist/PhD  
**Type:** COMPARE  
**Weight:** 3.5×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
What is the difference between a Cybersecurity Incident Response Plan (CSIRP) and a process safety plan, and why does an I\&C engineer need to understand both?

**Correct Answer:**  
A CSIRP defines processes for detecting, containing, investigating, and recovering from a cyber incident. A process safety plan addresses safe shutdown and emergency procedures for hazardous process upsets. I\&C engineers bridge both because a cyber incident can trigger a process safety emergency.

**Required Elements:**
- A CSIRP defines processes for detecting, containing, investigating, and recovering from a cyber incident
- A process safety plan addresses safe shutdown and emergency procedures for hazardous process upsets
- I\&C engineers bridge both because a cyber incident can trigger a process safety emergency

**Common Wrong Answers:**
- A CSIRP and a process safety plan are the same document because both cover emergencies.
- I\&C engineers only need the process safety plan; cyber response belongs entirely to IT.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — all 3 required elements present and accurate |  
| Partial (high) | 7/10 — 2 of 3 elements correct |  
| Partial (low) | 4/10 — partial answer, key element missing |  
| Zero | 0/10 — incorrect or missing core concept |

**Confidence Penalty Trigger:** model conflates the two systems or misattributes a property to the wrong standard

**Reference:** ISA/IEC 62443; NIST SP 800-82; NERC CIP

**Difficulty Rationale:** T3 Specialist (3.5×) because ICS Cybersecurity requires understanding of two distinct systems and their domain-specific tradeoffs

---

## IUK-T3-560-CYBER-024
**Block:** Block 11 - ICS Cybersecurity  
**Tier:** T3 · Specialist/PhD  
**Type:** IDENTIFY  
**Weight:** 3.5×  
**Safety Gate:** YES  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
Why should instrument and controls engineers understand cybersecurity even if they are not IT professionals?

**Correct Answer:**  
I\&C engineers specify, configure, and maintain the exact devices that would be targeted in an OT attack. They understand the process consequences of control system failure better than IT teams and are key participants in OT risk assessments and safety function validation.

**Required Elements:**
- I\&C engineers specify, configure, and maintain the exact devices that would be targeted in an OT attack
- They understand the process consequences of control system failure better than IT teams and are key participants in OT risk assessments and safety function validation

**Common Wrong Answers:**
- I\&C engineers do not need cybersecurity knowledge because firewalls are IT equipment.
- Cybersecurity only affects data privacy, not transmitters, PLCs, valves, or trips.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — all 2 required elements present and accurate |  
| Partial (high) | 7/10 — 1 of 2 elements correct |  
| Partial (low) | 4/10 — partial answer, key element missing |  
| Zero | 0/10 — incorrect or missing core concept |

**Confidence Penalty Trigger:** model states a definition without citing the applicable standard or first principle; model omits or minimizes the safety implication of an incorrect answer

**Reference:** ISA/IEC 62443; NIST SP 800-82; NERC CIP

**Difficulty Rationale:** T3 Specialist (3.5×) because ICS Cybersecurity requires precise recall of a standard or principle with correct scope

---

## IUK-T3-560-CYBER-025
**Block:** Block 11 - ICS Cybersecurity  
**Tier:** T3 · Specialist/PhD  
**Type:** DIAGNOSE  
**Weight:** 3.5×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
Scenario: A control engineer wants to run an nmap network scan on the DCS subnet to identify all connected devices. Why could this be dangerous on an OT network even though it is routine on enterprise networks?

**Correct Answer:**  
Many PLC and DCS components, especially legacy devices, have fragile TCP/IP stacks that can crash, lock up, or reboot when hit with network scan probe packets. An nmap scan on a live OT network can cause unplanned controller reboots, loss of I/O communication, or process trips. Passive OT discovery tools must be used instead.

**Required Elements:**
- Many PLC and DCS components, especially legacy devices, have fragile TCP/IP stacks that can crash, lock up, or reboot when hit with network scan probe packets
- An nmap scan on a live OT network can cause unplanned controller reboots, loss of I/O communication, or process trips
- Passive OT discovery tools must be used instead

**Common Wrong Answers:**
- Run nmap during lunch because less operator activity means lower risk.
- Use aggressive scans to identify every device quickly, then notify operations afterward.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — correct root cause + physical mechanism + correct fix |  
| Partial (high) | 7/10 — correct root cause, mechanism incomplete |  
| Partial (low) | 4/10 — plausible diagnosis but wrong mechanism |  
| Zero | 0/10 — wrong root cause or dangerous recommendation |

**Confidence Penalty Trigger:** model gives a root cause without citing the physical mechanism or reasoning chain

**Reference:** ISA/IEC 62443; NIST SP 800-82; NERC CIP

**Difficulty Rationale:** T3 Specialist (3.5×) because ICS Cybersecurity requires multi-step reasoning from symptoms to root cause — a field-level skill  
  
---  
# Block 9 - Advanced Diagnostic

---

## IUK-T3-560-DIAG-001
**Block:** Block 9 - Advanced Diagnostic  
**Tier:** T3 · Specialist/PhD  
**Type:** DIAGNOSE  
**Weight:** 3.5×  
**Safety Gate:** YES  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
Scenario: A reactor temperature loop became sluggish after a heavy-wall thermowell was installed and no heat-conductive paste was applied. The 4-20 mA signal to the valve responds immediately. Why is the loop sluggish, and what is the physical cause?

**Correct Answer:**  
The loop is sluggish because the new thermowell increased sensor thermal lag / time constant. The heavy wall and poor thermal contact add thermal resistance and mass, so the sensing element responds much more slowly to process temperature changes.

**Required Elements:**
- The loop is sluggish because the new thermowell increased sensor thermal lag / time constant
- The heavy wall and poor thermal contact add thermal resistance and mass, so the sensing element responds much more slowly to process temperature changes

**Common Wrong Answers:**
- The loop is sluggish because the valve I/P signal has too much damping.
- Reduce PID integral time before checking the thermowell installation.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — correct root cause + physical mechanism + correct fix |  
| Partial (high) | 7/10 — correct root cause, mechanism incomplete |  
| Partial (low) | 4/10 — plausible diagnosis but wrong mechanism |  
| Zero | 0/10 — wrong root cause or dangerous recommendation |

**Confidence Penalty Trigger:** model gives a root cause without citing the physical mechanism or reasoning chain; model omits or minimizes the safety implication of an incorrect answer

**Reference:** ISA-5.1; ISA-18.2; first principles

**Difficulty Rationale:** T3 Specialist (3.5×) because Advanced Diagnostic requires multi-step reasoning from symptoms to root cause — a field-level skill

---

## IUK-T3-560-DIAG-002
**Block:** Block 9 - Advanced Diagnostic  
**Tier:** T3 · Specialist/PhD  
**Type:** DIAGNOSE  
**Weight:** 3.5×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
Scenario: A pressure controller keeps oscillating even after the tech reduces controller gain. The valve has high stiction from over-tightened graphite packing. Why did reducing gain fail, and what trend shape should appear on valve position?

**Correct Answer:**  
Reducing gain failed because the root cause is mechanical stiction, not excessive controller aggressiveness alone. The output ramps until friction breaks free, then the valve jumps, producing a stick-slip sawtooth pattern.

**Required Elements:**
- Reducing gain failed because the root cause is mechanical stiction, not excessive controller aggressiveness alone
- The output ramps until friction breaks free, then the valve jumps, producing a stick-slip sawtooth pattern

**Common Wrong Answers:**
- Reducing gain failed because the controller is still too aggressive; keep lowering gain until the oscillation stops.
- The valve position trend should be a smooth sine wave if packing is the problem.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — correct root cause + physical mechanism + correct fix |  
| Partial (high) | 7/10 — correct root cause, mechanism incomplete |  
| Partial (low) | 4/10 — plausible diagnosis but wrong mechanism |  
| Zero | 0/10 — wrong root cause or dangerous recommendation |

**Confidence Penalty Trigger:** model gives a root cause without citing the physical mechanism or reasoning chain

**Reference:** ISA-5.1; ISA-18.2; first principles

**Difficulty Rationale:** T3 Specialist (3.5×) because Advanced Diagnostic requires multi-step reasoning from symptoms to root cause — a field-level skill

---

## IUK-T3-560-DIAG-003
**Block:** Block 9 - Advanced Diagnostic  
**Tier:** T3 · Specialist/PhD  
**Type:** DIAGNOSE  
**Weight:** 3.5×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
Scenario: A magmeter shows 25 GPM at zero flow. A nearby VFD-driven motor has a failed shield ground. What is the likely cause, and what check should the tech perform?

**Correct Answer:**  
The likely cause is stray 50/60 Hz interference or poor process/reference grounding affecting the electrode circuit. The tech should verify grounding/reference integrity, shield termination, and check for AC/noise voltage associated with the electrode circuit.

**Required Elements:**
- The likely cause is stray 50/60 Hz interference or poor process/reference grounding affecting the electrode circuit
- The tech should verify grounding/reference integrity, shield termination, and check for AC/noise voltage associated with the electrode circuit

**Common Wrong Answers:**
- The magmeter is reading 25 GPM because the pipe is partially full.
- Replace the flowtube before checking shields, grounds, or electrode noise.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — correct root cause + physical mechanism + correct fix |  
| Partial (high) | 7/10 — correct root cause, mechanism incomplete |  
| Partial (low) | 4/10 — plausible diagnosis but wrong mechanism |  
| Zero | 0/10 — wrong root cause or dangerous recommendation |

**Confidence Penalty Trigger:** model gives a root cause without citing the physical mechanism or reasoning chain

**Reference:** ISA-5.1; ISA-18.2; first principles

**Difficulty Rationale:** T3 Specialist (3.5×) because Advanced Diagnostic requires multi-step reasoning from symptoms to root cause — a field-level skill

---

## IUK-T3-560-DIAG-004
**Block:** Block 9 - Advanced Diagnostic  
**Tier:** T3 · Specialist/PhD  
**Type:** DIAGNOSE  
**Weight:** 3.5×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
Scenario: A DP flow transmitter and the DCS are both configured for square-root extraction. If actual flow is 50 percent, what will the HMI display?

**Correct Answer:**  
About 70.7 percent

**Required Elements:**
- About 70.7 percent

**Common Wrong Answers:**
- The HMI will display 50 percent because two square roots cancel out.
- The HMI will display 25 percent because the signal is square-rooted twice.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — correct root cause + physical mechanism + correct fix |  
| Partial (high) | 7/10 — correct root cause, mechanism incomplete |  
| Partial (low) | 4/10 — plausible diagnosis but wrong mechanism |  
| Zero | 0/10 — wrong root cause or dangerous recommendation |

**Confidence Penalty Trigger:** model gives a root cause without citing the physical mechanism or reasoning chain

**Reference:** ISA-5.1; ISA-18.2; first principles

**Difficulty Rationale:** T3 Specialist (3.5×) because Advanced Diagnostic requires multi-step reasoning from symptoms to root cause — a field-level skill

---

## IUK-T3-560-DIAG-005
**Block:** Block 9 - Advanced Diagnostic  
**Tier:** T3 · Specialist/PhD  
**Type:** DIAGNOSE  
**Weight:** 3.5×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
Scenario: Boiler drum level suddenly spikes high after a rapid pressure drop even though no water was added. Explain swell and why the indicated level rises.

**Correct Answer:**  
A rapid pressure drop lets steam bubbles in the drum water expand and causes some water to flash, increasing the apparent water volume. That temporary expansion makes the drum level indication rise even without added water.

**Required Elements:**
- A rapid pressure drop lets steam bubbles in the drum water expand and causes some water to flash, increasing the apparent water volume
- That temporary expansion makes the drum level indication rise even without added water

**Common Wrong Answers:**
- The level rose because more feedwater must have entered the drum.
- A pressure drop should collapse bubbles, so the indicated level should fall.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — correct root cause + physical mechanism + correct fix |  
| Partial (high) | 7/10 — correct root cause, mechanism incomplete |  
| Partial (low) | 4/10 — plausible diagnosis but wrong mechanism |  
| Zero | 0/10 — wrong root cause or dangerous recommendation |

**Confidence Penalty Trigger:** model gives a root cause without citing the physical mechanism or reasoning chain

**Reference:** ISA-5.1; ISA-18.2; first principles

**Difficulty Rationale:** T3 Specialist (3.5×) because Advanced Diagnostic requires multi-step reasoning from symptoms to root cause — a field-level skill

---

## IUK-T3-560-DIAG-006
**Block:** Block 9 - Advanced Diagnostic  
**Tier:** T3 · Specialist/PhD  
**Type:** DIAGNOSE  
**Weight:** 3.5×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
Scenario: Four loop readings are erratic, and a temporary reference jumper stabilizes them. The 24 VDC common is floating and the cable shield is grounded only at the field end. What is the permanent fix?

**Correct Answer:**  
Provide the loop/common with the proper cabinet-side instrument reference/grounding arrangement and terminate shields per site practice, usually at the control-system end.

**Required Elements:**
- Provide the loop/common with the proper cabinet-side instrument reference/grounding arrangement and terminate shields per site practice, usually at the control-system end

**Common Wrong Answers:**
- Leave the temporary jumper installed permanently because it fixed the readings.
- Ground the cable shield at both field and cabinet ends everywhere to force a reference.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — correct root cause + physical mechanism + correct fix |  
| Partial (high) | 7/10 — correct root cause, mechanism incomplete |  
| Partial (low) | 4/10 — plausible diagnosis but wrong mechanism |  
| Zero | 0/10 — wrong root cause or dangerous recommendation |

**Confidence Penalty Trigger:** model gives a root cause without citing the physical mechanism or reasoning chain

**Reference:** ISA-5.1; ISA-18.2; first principles

**Difficulty Rationale:** T3 Specialist (3.5×) because Advanced Diagnostic requires multi-step reasoning from symptoms to root cause — a field-level skill

---

## IUK-T3-560-DIAG-007
**Block:** Block 9 - Advanced Diagnostic  
**Tier:** T3 · Specialist/PhD  
**Type:** DIAGNOSE  
**Weight:** 3.5×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
Scenario: A frozen high-side impulse line leaves a DP flow transmitter stuck at 12.5 mA. If process flow increases, what will the transmitter do?

**Correct Answer:**  
It will stay near 12.5 mA

**Required Elements:**
- It will stay near 12.5 mA

**Common Wrong Answers:**
- It will rise normally because the low-side pressure still changes with flow.
- It will fail low to 4 mA as soon as the process flow increases.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — correct root cause + physical mechanism + correct fix |  
| Partial (high) | 7/10 — correct root cause, mechanism incomplete |  
| Partial (low) | 4/10 — plausible diagnosis but wrong mechanism |  
| Zero | 0/10 — wrong root cause or dangerous recommendation |

**Confidence Penalty Trigger:** model gives a root cause without citing the physical mechanism or reasoning chain

**Reference:** ISA-5.1; ISA-18.2; first principles

**Difficulty Rationale:** T3 Specialist (3.5×) because Advanced Diagnostic requires multi-step reasoning from symptoms to root cause — a field-level skill

---

## IUK-T3-560-DIAG-008
**Block:** Block 9 - Advanced Diagnostic  
**Tier:** T3 · Specialist/PhD  
**Type:** DIAGNOSE  
**Weight:** 3.5×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
Scenario: A pump shows high amps, a downstream vortex meter reads zero, and a rebuilt discharge check valve was installed backward. How can the nearby pressure gauge help prove the blockage is downstream of the pump but upstream of the meter?

**Correct Answer:**  
If pump-discharge pressure rises toward shutoff head while the flowmeter still reads zero, the pump is building pressure against a blockage located downstream of the pump and upstream of the meter.

**Required Elements:**
- If pump-discharge pressure rises toward shutoff head while the flowmeter still reads zero, the pump is building pressure against a blockage located downstream of the pump and upstream of the meter

**Common Wrong Answers:**
- A low discharge pressure with zero flow proves the blockage is downstream of the meter.
- The pressure gauge is useless because only the vortex meter can prove blockage location.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — correct root cause + physical mechanism + correct fix |  
| Partial (high) | 7/10 — correct root cause, mechanism incomplete |  
| Partial (low) | 4/10 — plausible diagnosis but wrong mechanism |  
| Zero | 0/10 — wrong root cause or dangerous recommendation |

**Confidence Penalty Trigger:** model gives a root cause without citing the physical mechanism or reasoning chain

**Reference:** ISA-5.1; ISA-18.2; first principles

**Difficulty Rationale:** T3 Specialist (3.5×) because Advanced Diagnostic requires multi-step reasoning from symptoms to root cause — a field-level skill

---

## IUK-T3-560-DIAG-009
**Block:** Block 9 - Advanced Diagnostic  
**Tier:** T3 · Specialist/PhD  
**Type:** DIAGNOSE  
**Weight:** 3.5×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
Scenario: A cracked pH glass electrode makes the reading stick near 7.0. Why?

**Correct Answer:**  
A cracked glass electrode can collapse the membrane potential toward the probes zero point, which is around 0 mV / pH 7, so the indicated value often drifts toward neutral.

**Required Elements:**
- A cracked glass electrode can collapse the membrane potential toward the probes zero point, which is around 0 mV / pH 7, so the indicated value often drifts toward neutral

**Common Wrong Answers:**
- A cracked pH electrode will always drive full-scale acid or full-scale caustic.
- It sticks near 7 because the transmitter automatically defaults to neutral on any fault.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — correct root cause + physical mechanism + correct fix |  
| Partial (high) | 7/10 — correct root cause, mechanism incomplete |  
| Partial (low) | 4/10 — plausible diagnosis but wrong mechanism |  
| Zero | 0/10 — wrong root cause or dangerous recommendation |

**Confidence Penalty Trigger:** model gives a root cause without citing the physical mechanism or reasoning chain

**Reference:** ISA-5.1; ISA-18.2; first principles

**Difficulty Rationale:** T3 Specialist (3.5×) because Advanced Diagnostic requires multi-step reasoning from symptoms to root cause — a field-level skill

---

## IUK-T3-560-DIAG-010
**Block:** Block 9 - Advanced Diagnostic  
**Tier:** T3 · Specialist/PhD  
**Type:** DIAGNOSE  
**Weight:** 3.5×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
Scenario: A catalytic bead LEL detector false-alarms when a contractor uses a handheld radio next to it. What is the phenomenon, and how should wiring be modified?

**Correct Answer:**  
This is RFI/EMI. Use properly grounded shielded twisted pair, maintain correct bonding, and route/install wiring and housing grounding to reduce radio-frequency pickup.

**Required Elements:**
- This is RFI/EMI
- Use properly grounded shielded twisted pair, maintain correct bonding, and route/install wiring and housing grounding to reduce radio-frequency pickup

**Common Wrong Answers:**
- The radio is changing gas concentration around the sensor.
- Fix it by increasing the LEL alarm setpoint rather than correcting shielding and grounding.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — correct root cause + physical mechanism + correct fix |  
| Partial (high) | 7/10 — correct root cause, mechanism incomplete |  
| Partial (low) | 4/10 — plausible diagnosis but wrong mechanism |  
| Zero | 0/10 — wrong root cause or dangerous recommendation |

**Confidence Penalty Trigger:** model gives a root cause without citing the physical mechanism or reasoning chain

**Reference:** ISA-5.1; ISA-18.2; first principles

**Difficulty Rationale:** T3 Specialist (3.5×) because Advanced Diagnostic requires multi-step reasoning from symptoms to root cause — a field-level skill

---

## IUK-T3-560-DIAG-011
**Block:** Block 9 - Advanced Diagnostic  
**Tier:** T3 · Specialist/PhD  
**Type:** APPLY  
**Weight:** 3.5×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
In ISA-88 batch control, what does a "phase" represent within a unit procedure?

**Correct Answer:**  
A distinct processing step or operation performing a specific function, e.g., charge, heat, react, or discharge.

**Required Elements:**
- A distinct processing step or operation performing a specific function, e.g., charge, heat, react, or discharge

**Common Wrong Answers:**
- A phase is the entire batch recipe from start to finish.
- A phase is a physical equipment item such as a pump or valve.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — all 1 required elements present and accurate |  
| Partial (high) | 7/10 — 1 of 1 elements correct |  
| Partial (low) | 4/10 — partial answer, key element missing |  
| Zero | 0/10 — incorrect or missing core concept |

**Confidence Penalty Trigger:** model asserts without citing supporting reasoning

**Reference:** ISA-5.1; ISA-18.2; first principles

**Difficulty Rationale:** T3 Specialist (3.5×) because Advanced Diagnostic requires sequencing a correct procedure, not just identifying one step

---

## IUK-T3-560-DIAG-012
**Block:** Block 9 - Advanced Diagnostic  
**Tier:** T3 · Specialist/PhD  
**Type:** IDENTIFY  
**Weight:** 3.5×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
A continuous PID loop exhibits integral windup during a prolonged MV saturation. What is the typical symptom when the error reverses direction?

**Correct Answer:**  
Overshoot or delayed recovery caused by the accumulated integral term.

**Required Elements:**
- Overshoot or delayed recovery caused by the accumulated integral term

**Common Wrong Answers:**
- The typical symptom is instant recovery with no overshoot once the error changes sign.
- Windup only affects manual mode and cannot affect automatic PID loops.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — all 1 required elements present and accurate |  
| Partial (high) | 7/10 — 1 of 1 elements correct |  
| Partial (low) | 4/10 — partial answer, key element missing |  
| Zero | 0/10 — incorrect or missing core concept |

**Confidence Penalty Trigger:** model states a definition without citing the applicable standard or first principle

**Reference:** ISA-5.1; ISA-18.2; first principles

**Difficulty Rationale:** T3 Specialist (3.5×) because Advanced Diagnostic requires precise recall of a standard or principle with correct scope

---

## IUK-T3-560-DIAG-013
**Block:** Block 9 - Advanced Diagnostic  
**Tier:** T3 · Specialist/PhD  
**Type:** DIAGNOSE  
**Weight:** 3.5×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
In a cascade control strategy, why is the inner (slave) loop typically tuned more aggressively than the outer (master) loop?

**Correct Answer:**  
To make the slave respond quickly to disturbances so the master sees a well-behaved secondary process.

**Required Elements:**
- To make the slave respond quickly to disturbances so the master sees a well-behaved secondary process

**Common Wrong Answers:**
- The outer loop should always be tuned faster than the inner loop.
- Both master and slave loops should have identical tuning constants.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — correct root cause + physical mechanism + correct fix |  
| Partial (high) | 7/10 — correct root cause, mechanism incomplete |  
| Partial (low) | 4/10 — plausible diagnosis but wrong mechanism |  
| Zero | 0/10 — wrong root cause or dangerous recommendation |

**Confidence Penalty Trigger:** model gives a root cause without citing the physical mechanism or reasoning chain

**Reference:** ISA-5.1; ISA-18.2; first principles

**Difficulty Rationale:** T3 Specialist (3.5×) because Advanced Diagnostic requires multi-step reasoning from symptoms to root cause — a field-level skill

---

## IUK-T3-560-DIAG-014
**Block:** Block 9 - Advanced Diagnostic  
**Tier:** T3 · Specialist/PhD  
**Type:** IDENTIFY  
**Weight:** 3.5×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
A model predictive controller (MPC) is controlling a multivariable distillation column. What is a primary advantage over single-loop PID in this application?

**Correct Answer:**  
Explicit handling of multi-variable interactions, constraints, and economic objectives simultaneously.

**Required Elements:**
- Explicit handling of multi-variable interactions, constraints, and economic objectives simultaneously

**Common Wrong Answers:**
- MPC is mainly useful because it eliminates the need for process measurements.
- Single-loop PID handles interactions and constraints just as well if gain is high enough.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — all 1 required elements present and accurate |  
| Partial (high) | 7/10 — 1 of 1 elements correct |  
| Partial (low) | 4/10 — partial answer, key element missing |  
| Zero | 0/10 — incorrect or missing core concept |

**Confidence Penalty Trigger:** model states a definition without citing the applicable standard or first principle

**Reference:** ISA-5.1; ISA-18.2; first principles

**Difficulty Rationale:** T3 Specialist (3.5×) because Advanced Diagnostic requires precise recall of a standard or principle with correct scope

---

## IUK-T3-560-DIAG-015
**Block:** Block 9 - Advanced Diagnostic  
**Tier:** T3 · Specialist/PhD  
**Type:** DESIGN  
**Weight:** 3.5×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
In override control (selector strategy), what happens when two controllers compete for the same manipulated variable?

**Correct Answer:**  
The selector passes the higher or lower output depending on configuration (max/min select).

**Required Elements:**
- The selector passes the higher or lower output depending on configuration (max/min select)

**Common Wrong Answers:**
- Both controllers are averaged together before driving the valve.
- The controller with the newest tuning constants always wins.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — all 1 required elements present and accurate |  
| Partial (high) | 7/10 — 1 of 1 elements correct |  
| Partial (low) | 4/10 — partial answer, key element missing |  
| Zero | 0/10 — incorrect or missing core concept |

**Confidence Penalty Trigger:** model makes a selection without stating the selection criteria or design constraint

**Reference:** ISA-5.1; ISA-18.2; first principles

**Difficulty Rationale:** T3 Specialist (3.5×) because Advanced Diagnostic requires applying selection criteria under real engineering constraints

---

## IUK-T3-560-DIAG-016
**Block:** Block 9 - Advanced Diagnostic  
**Tier:** T3 · Specialist/PhD  
**Type:** IDENTIFY  
**Weight:** 3.5×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
A feedforward control action is added to a level controller on a surge tank. What condition must be met for perfect disturbance rejection?

**Correct Answer:**  
The feedforward model gain and dynamics must exactly match the real process disturbance path.

**Required Elements:**
- The feedforward model gain and dynamics must exactly match the real process disturbance path

**Common Wrong Answers:**
- Perfect rejection only requires the feedforward signal to move in the correct direction.
- The feedback PID will automatically correct any feedforward model error instantly.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — all 1 required elements present and accurate |  
| Partial (high) | 7/10 — 1 of 1 elements correct |  
| Partial (low) | 4/10 — partial answer, key element missing |  
| Zero | 0/10 — incorrect or missing core concept |

**Confidence Penalty Trigger:** model states a definition without citing the applicable standard or first principle

**Reference:** ISA-5.1; ISA-18.2; first principles

**Difficulty Rationale:** T3 Specialist (3.5×) because Advanced Diagnostic requires precise recall of a standard or principle with correct scope

---

## IUK-T3-560-DIAG-017
**Block:** Block 9 - Advanced Diagnostic  
**Tier:** T3 · Specialist/PhD  
**Type:** APPLY  
**Weight:** 3.5×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
What is the primary purpose of gain scheduling in a nonlinear process such as pH control?

**Correct Answer:**  
To adjust PID parameters dynamically based on operating region, e.g., near neutrality vs. pH extremes.

**Required Elements:**
- To adjust PID parameters dynamically based on operating region, e.g., near neutrality vs. pH extremes

**Common Wrong Answers:**
- Gain scheduling is used to keep the controller output at 50 percent.
- It is mainly a way to change engineering units on the HMI.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — all 1 required elements present and accurate |  
| Partial (high) | 7/10 — 1 of 1 elements correct |  
| Partial (low) | 4/10 — partial answer, key element missing |  
| Zero | 0/10 — incorrect or missing core concept |

**Confidence Penalty Trigger:** model asserts without citing supporting reasoning

**Reference:** ISA-5.1; ISA-18.2; first principles

**Difficulty Rationale:** T3 Specialist (3.5×) because Advanced Diagnostic requires sequencing a correct procedure, not just identifying one step

---

## IUK-T3-560-DIAG-018
**Block:** Block 9 - Advanced Diagnostic  
**Tier:** T3 · Specialist/PhD  
**Type:** IDENTIFY  
**Weight:** 3.5×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
In OPC UA, what feature allows secure, platform-independent data modeling and access compared to classic OPC?

**Correct Answer:**  
Information modeling with nodes and references, plus built-in security: encryption, message signing, and user authentication.

**Required Elements:**
- Information modeling with nodes and references, plus built-in security: encryption, message signing, and user authentication

**Common Wrong Answers:**
- OPC UA is secure because it uses DCOM permissions like classic OPC.
- OPC UA only adds faster polling; it does not change modeling or security.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — all 1 required elements present and accurate |  
| Partial (high) | 7/10 — 1 of 1 elements correct |  
| Partial (low) | 4/10 — partial answer, key element missing |  
| Zero | 0/10 — incorrect or missing core concept |

**Confidence Penalty Trigger:** model states a definition without citing the applicable standard or first principle

**Reference:** ISA-5.1; ISA-18.2; first principles

**Difficulty Rationale:** T3 Specialist (3.5×) because Advanced Diagnostic requires precise recall of a standard or principle with correct scope

---

## IUK-T3-560-DIAG-019
**Block:** Block 9 - Advanced Diagnostic  
**Tier:** T3 · Specialist/PhD  
**Type:** IDENTIFY  
**Weight:** 3.5×  
**Safety Gate:** YES  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
A ratio control loop maintains fuel-to-air ratio in a fired heater. If the air flow transmitter fails low, what should a well-designed override do?

**Correct Answer:**  
Drive fuel to minimum or safe low to prevent rich combustion or explosion risk.

**Required Elements:**
- Drive fuel to minimum or safe low to prevent rich combustion or explosion risk

**Common Wrong Answers:**
- The override should increase fuel to maintain heater duty.
- The override should ignore the air transmitter because ratio control is only advisory.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — all 1 required elements present and accurate |  
| Partial (high) | 7/10 — 1 of 1 elements correct |  
| Partial (low) | 4/10 — partial answer, key element missing |  
| Zero | 0/10 — incorrect or missing core concept |

**Confidence Penalty Trigger:** model states a definition without citing the applicable standard or first principle; model omits or minimizes the safety implication of an incorrect answer

**Reference:** ISA-5.1; ISA-18.2; first principles

**Difficulty Rationale:** T3 Specialist (3.5×) because Advanced Diagnostic requires precise recall of a standard or principle with correct scope

---

## IUK-T3-560-DIAG-020
**Block:** Block 9 - Advanced Diagnostic  
**Tier:** T3 · Specialist/PhD  
**Type:** IDENTIFY  
**Weight:** 3.5×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
In a multi-variable control application, what does RGA (Relative Gain Array) help identify?

**Correct Answer:**  
Loop interactions and pairing recommendations — avoid pairings with RGA near 0 or very large/negative values.

**Required Elements:**
- Loop interactions and pairing recommendations — avoid pairings with RGA near 0 or very large/negative values

**Common Wrong Answers:**
- RGA identifies which thermocouple type should be used in each loop.
- RGA simply ranks loops by economic importance and does not address interactions.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — all 1 required elements present and accurate |  
| Partial (high) | 7/10 — 1 of 1 elements correct |  
| Partial (low) | 4/10 — partial answer, key element missing |  
| Zero | 0/10 — incorrect or missing core concept |

**Confidence Penalty Trigger:** model states a definition without citing the applicable standard or first principle

**Reference:** ISA-5.1; ISA-18.2; first principles

**Difficulty Rationale:** T3 Specialist (3.5×) because Advanced Diagnostic requires precise recall of a standard or principle with correct scope

---

## IUK-T3-560-DIAG-021
**Block:** Block 9 - Advanced Diagnostic  
**Tier:** T3 · Specialist/PhD  
**Type:** DIAGNOSE  
**Weight:** 3.5×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
Scenario: A smart positioner and the DCS both have aggressive PID loops enabled and the valve oscillates. Explain “control on control” and why two aggressive loops in series are unstable.

**Correct Answer:**  
The DCS outer loop is trying to control the process while the positioner inner loop is also aggressively controlling valve travel. If both loops are tuned too hard, they interact and fight each other instead of one serving as a fast, well-behaved inner loop.

**Required Elements:**
- The DCS outer loop is trying to control the process while the positioner inner loop is also aggressively controlling valve travel
- If both loops are tuned too hard, they interact and fight each other instead of one serving as a fast, well-behaved inner loop

**Common Wrong Answers:**
- Control on control is always stable because more controllers means tighter control.
- The fix is to make both the DCS PID and positioner PID more aggressive.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — correct root cause + physical mechanism + correct fix |  
| Partial (high) | 7/10 — correct root cause, mechanism incomplete |  
| Partial (low) | 4/10 — plausible diagnosis but wrong mechanism |  
| Zero | 0/10 — wrong root cause or dangerous recommendation |

**Confidence Penalty Trigger:** model gives a root cause without citing the physical mechanism or reasoning chain

**Reference:** ISA-5.1; ISA-18.2; first principles

**Difficulty Rationale:** T3 Specialist (3.5×) because Advanced Diagnostic requires multi-step reasoning from symptoms to root cause — a field-level skill

---

## IUK-T3-560-DIAG-022
**Block:** Block 9 - Advanced Diagnostic  
**Tier:** T3 · Specialist/PhD  
**Type:** DIAGNOSE  
**Weight:** 3.5×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
Scenario: A Coriolis meter sees large spikes and drive gain goes to 100 percent when vapor slugs pass through. Why does entrained air cause loss of lock?

**Correct Answer:**  
Entrained gas creates two-phase damping and rapidly changes the effective density/load in the vibrating tubes. The meter must drive harder to maintain oscillation, and severe slugs can make it lose stable resonance lock.

**Required Elements:**
- Entrained gas creates two-phase damping and rapidly changes the effective density/load in the vibrating tubes
- The meter must drive harder to maintain oscillation, and severe slugs can make it lose stable resonance lock

**Common Wrong Answers:**
- Entrained air improves Coriolis drive stability because gas is lighter than liquid.
- Drive gain at 100 percent proves the transmitter electronics are failed, not the process condition.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — correct root cause + physical mechanism + correct fix |  
| Partial (high) | 7/10 — correct root cause, mechanism incomplete |  
| Partial (low) | 4/10 — plausible diagnosis but wrong mechanism |  
| Zero | 0/10 — wrong root cause or dangerous recommendation |

**Confidence Penalty Trigger:** model gives a root cause without citing the physical mechanism or reasoning chain

**Reference:** ISA-5.1; ISA-18.2; first principles

**Difficulty Rationale:** T3 Specialist (3.5×) because Advanced Diagnostic requires multi-step reasoning from symptoms to root cause — a field-level skill

---

## IUK-T3-560-DIAG-023
**Block:** Block 9 - Advanced Diagnostic  
**Tier:** T3 · Specialist/PhD  
**Type:** DIAGNOSE  
**Weight:** 3.5×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
Scenario: A flare-stack DP transmitter shows a false 1.5 inWC at zero flow, but reads zero when both sides are vented locally. How does the chimney effect create this error?

**Correct Answer:**  
The light flare gas in the tall stack has a different hydrostatic pressure gradient than the outside air column. That density difference creates a real pressure difference between bottom and top taps even when there is no actual process flow.

**Required Elements:**
- The light flare gas in the tall stack has a different hydrostatic pressure gradient than the outside air column
- That density difference creates a real pressure difference between bottom and top taps even when there is no actual process flow

**Common Wrong Answers:**
- The chimney effect is caused by wind blowing across the transmitter manifold.
- If both sides vent to zero locally, the installed measurement must also be zero.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — correct root cause + physical mechanism + correct fix |  
| Partial (high) | 7/10 — correct root cause, mechanism incomplete |  
| Partial (low) | 4/10 — plausible diagnosis but wrong mechanism |  
| Zero | 0/10 — wrong root cause or dangerous recommendation |

**Confidence Penalty Trigger:** model gives a root cause without citing the physical mechanism or reasoning chain

**Reference:** ISA-5.1; ISA-18.2; first principles

**Difficulty Rationale:** T3 Specialist (3.5×) because Advanced Diagnostic requires multi-step reasoning from symptoms to root cause — a field-level skill

---

## IUK-T3-560-DIAG-024
**Block:** Block 9 - Advanced Diagnostic  
**Tier:** T3 · Specialist/PhD  
**Type:** DIAGNOSE  
**Weight:** 3.5×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
Scenario: A 120 VAC solenoid is humming loudly, very hot, and the armature is stuck half-seated. Why does this lead to burnout?

**Correct Answer:**  
With the armature not fully seated, the magnetic circuit stays open, inductance stays low, and current remains near inrush rather than falling to normal holding current. The excess I-squared-R heating overheats the coil.

**Required Elements:**
- With the armature not fully seated, the magnetic circuit stays open, inductance stays low, and current remains near inrush rather than falling to normal holding current
- The excess I-squared-R heating overheats the coil

**Common Wrong Answers:**
- A half-seated AC solenoid draws less current because the armature gap is smaller than normal.
- The humming is only a noise issue; the coil temperature is unrelated to armature position.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — correct root cause + physical mechanism + correct fix |  
| Partial (high) | 7/10 — correct root cause, mechanism incomplete |  
| Partial (low) | 4/10 — plausible diagnosis but wrong mechanism |  
| Zero | 0/10 — wrong root cause or dangerous recommendation |

**Confidence Penalty Trigger:** model gives a root cause without citing the physical mechanism or reasoning chain

**Reference:** ISA-5.1; ISA-18.2; first principles

**Difficulty Rationale:** T3 Specialist (3.5×) because Advanced Diagnostic requires multi-step reasoning from symptoms to root cause — a field-level skill

---

## IUK-T3-560-DIAG-025
**Block:** Block 9 - Advanced Diagnostic  
**Tier:** T3 · Specialist/PhD  
**Type:** DIAGNOSE  
**Weight:** 3.5×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
Scenario: An ultrasonic level transmitter is locked on a false echo from an agitator blade. What software feature should be used?

**Correct Answer:**  
False echo suppression / echo mapping

**Required Elements:**
- False echo suppression / echo mapping

**Common Wrong Answers:**
- Increase the ultrasonic output damping until the false echo disappears.
- Re-range the transmitter span so the agitator blade is outside the measured level range.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — correct root cause + physical mechanism + correct fix |  
| Partial (high) | 7/10 — correct root cause, mechanism incomplete |  
| Partial (low) | 4/10 — plausible diagnosis but wrong mechanism |  
| Zero | 0/10 — wrong root cause or dangerous recommendation |

**Confidence Penalty Trigger:** model gives a root cause without citing the physical mechanism or reasoning chain

**Reference:** ISA-5.1; ISA-18.2; first principles

**Difficulty Rationale:** T3 Specialist (3.5×) because Advanced Diagnostic requires multi-step reasoning from symptoms to root cause — a field-level skill

---

## IUK-T3-560-DIAG-026
**Block:** Block 9 - Advanced Diagnostic  
**Tier:** T3 · Specialist/PhD  
**Type:** DIAGNOSE  
**Weight:** 3.5×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
Scenario: A gas DP flow installation has trapped condensate giving unequal liquid head in the impulse lines. How does this create a false high flow reading?

**Correct Answer:**  
Unequal liquid head adds extra hydrostatic pressure to one side of the DP measurement. If the high side carries more trapped liquid head than the low side, the measured DP rises and the indicated flow reads high.

**Required Elements:**
- Unequal liquid head adds extra hydrostatic pressure to one side of the DP measurement
- If the high side carries more trapped liquid head than the low side, the measured DP rises and the indicated flow reads high

**Common Wrong Answers:**
- Condensate in impulse lines always cancels out because both taps are on the same pipe.
- Unequal liquid head only affects level transmitters, not flow transmitters.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — correct root cause + physical mechanism + correct fix |  
| Partial (high) | 7/10 — correct root cause, mechanism incomplete |  
| Partial (low) | 4/10 — plausible diagnosis but wrong mechanism |  
| Zero | 0/10 — wrong root cause or dangerous recommendation |

**Confidence Penalty Trigger:** model gives a root cause without citing the physical mechanism or reasoning chain

**Reference:** ISA-5.1; ISA-18.2; first principles

**Difficulty Rationale:** T3 Specialist (3.5×) because Advanced Diagnostic requires multi-step reasoning from symptoms to root cause — a field-level skill

---

## IUK-T3-560-DIAG-027
**Block:** Block 9 - Advanced Diagnostic  
**Tier:** T3 · Specialist/PhD  
**Type:** DIAGNOSE  
**Weight:** 3.5×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
Scenario: A pH probe still shows 92 percent slope but takes 10 to 15 minutes to stabilize in buffers. Why can it still be end-of-life?

**Correct Answer:**  
Because endpoint slope and response time are different health indicators. A probe may still calibrate with acceptable slope yet be too sluggish for real process control because its glass/junction chemistry has aged or become poisoned.

**Required Elements:**
- Because endpoint slope and response time are different health indicators
- A probe may still calibrate with acceptable slope yet be too sluggish for real process control because its glass/junction chemistry has aged or become poisoned

**Common Wrong Answers:**
- A 92 percent slope proves the pH probe is healthy regardless of response time.
- Slow buffer response means the transmitter damping is too high, not the electrode.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — correct root cause + physical mechanism + correct fix |  
| Partial (high) | 7/10 — correct root cause, mechanism incomplete |  
| Partial (low) | 4/10 — plausible diagnosis but wrong mechanism |  
| Zero | 0/10 — wrong root cause or dangerous recommendation |

**Confidence Penalty Trigger:** model gives a root cause without citing the physical mechanism or reasoning chain

**Reference:** ISA-5.1; ISA-18.2; first principles

**Difficulty Rationale:** T3 Specialist (3.5×) because Advanced Diagnostic requires multi-step reasoning from symptoms to root cause — a field-level skill

---

## IUK-T3-560-DIAG-028
**Block:** Block 9 - Advanced Diagnostic  
**Tier:** T3 · Specialist/PhD  
**Type:** DIAGNOSE  
**Weight:** 3.5×  
**Safety Gate:** YES  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
Scenario: A 4-20 mA signal jumps whenever a nearby VFD starts, and the analog wire shares conduit with VFD output leads. What is capacitive coupling?

**Correct Answer:**  
The fast dv/dt switching on the VFD leads creates changing electric fields that couple through stray capacitance into the nearby analog conductor, injecting noise on top of the loop signal.

**Required Elements:**
- The fast dv/dt switching on the VFD leads creates changing electric fields that couple through stray capacitance into the nearby analog conductor, injecting noise on top of the loop signal

**Common Wrong Answers:**
- Capacitive coupling is caused by magnetic fields from DC current only.
- Sharing conduit with VFD output leads is acceptable if the analog signal is 4-20 mA.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — correct root cause + physical mechanism + correct fix |  
| Partial (high) | 7/10 — correct root cause, mechanism incomplete |  
| Partial (low) | 4/10 — plausible diagnosis but wrong mechanism |  
| Zero | 0/10 — wrong root cause or dangerous recommendation |

**Confidence Penalty Trigger:** model gives a root cause without citing the physical mechanism or reasoning chain; model omits or minimizes the safety implication of an incorrect answer

**Reference:** ISA-5.1; ISA-18.2; first principles

**Difficulty Rationale:** T3 Specialist (3.5×) because Advanced Diagnostic requires multi-step reasoning from symptoms to root cause — a field-level skill

---

## IUK-T3-560-DIAG-029
**Block:** Block 9 - Advanced Diagnostic  
**Tier:** T3 · Specialist/PhD  
**Type:** DIAGNOSE  
**Weight:** 3.5×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
Scenario: A bubbler dip tube is plugged, air flow goes to zero, and the level reading pegs high. Why?

**Correct Answer:**  
Because the air cannot escape the plugged tube, backpressure builds toward the regulator/supply limit. The transmitter sees that pressure as if it were maximum liquid head.

**Required Elements:**
- Because the air cannot escape the plugged tube, backpressure builds toward the regulator/supply limit
- The transmitter sees that pressure as if it were maximum liquid head

**Common Wrong Answers:**
- A plugged bubbler tube makes the reading peg low because no air reaches the tank.
- The reading is caused by actual level rising above the dip-tube tip.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — correct root cause + physical mechanism + correct fix |  
| Partial (high) | 7/10 — correct root cause, mechanism incomplete |  
| Partial (low) | 4/10 — plausible diagnosis but wrong mechanism |  
| Zero | 0/10 — wrong root cause or dangerous recommendation |

**Confidence Penalty Trigger:** model gives a root cause without citing the physical mechanism or reasoning chain

**Reference:** ISA-5.1; ISA-18.2; first principles

**Difficulty Rationale:** T3 Specialist (3.5×) because Advanced Diagnostic requires multi-step reasoning from symptoms to root cause — a field-level skill

---

## IUK-T3-560-DIAG-030
**Block:** Block 9 - Advanced Diagnostic  
**Tier:** T3 · Specialist/PhD  
**Type:** DIAGNOSE  
**Weight:** 3.5×  
**Safety Gate:** YES  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
Scenario: A thermocouple wire shorts near the furnace wall, creating a new junction outside the hot zone. Which junction does the transmitter effectively measure?

**Correct Answer:**  
It effectively measures the unintended junction that remains in the active circuit - in this case the short near the conduit entry - rather than the original hot junction.

**Required Elements:**
- It effectively measures the unintended junction that remains in the active circuit - in this case the short near the conduit entry - rather than the original hot junction

**Common Wrong Answers:**
- The transmitter still measures the original hot junction because it is physically at the furnace.
- The short only lowers loop resistance and has no temperature-measurement effect.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — correct root cause + physical mechanism + correct fix |  
| Partial (high) | 7/10 — correct root cause, mechanism incomplete |  
| Partial (low) | 4/10 — plausible diagnosis but wrong mechanism |  
| Zero | 0/10 — wrong root cause or dangerous recommendation |

**Confidence Penalty Trigger:** model gives a root cause without citing the physical mechanism or reasoning chain; model omits or minimizes the safety implication of an incorrect answer

**Reference:** ISA-5.1; ISA-18.2; first principles

**Difficulty Rationale:** T3 Specialist (3.5×) because Advanced Diagnostic requires multi-step reasoning from symptoms to root cause — a field-level skill

---

## IUK-T3-560-DIAG-031
**Block:** Block 9 - Advanced Diagnostic  
**Tier:** T3 · Specialist/PhD  
**Type:** APPLY  
**Weight:** 3.5×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
In ISA-88 batch control, what does a "phase" represent within a unit procedure?

**Correct Answer:**  
A distinct processing step or operation performing a specific function, e.g., charge, heat, react, or discharge.

**Required Elements:**
- A distinct processing step or operation performing a specific function, e.g., charge, heat, react, or discharge

**Common Wrong Answers:**
- A phase is the entire batch recipe from start to finish.
- A phase is a physical equipment item such as a pump or valve.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — all 1 required elements present and accurate |  
| Partial (high) | 7/10 — 1 of 1 elements correct |  
| Partial (low) | 4/10 — partial answer, key element missing |  
| Zero | 0/10 — incorrect or missing core concept |

**Confidence Penalty Trigger:** model asserts without citing supporting reasoning

**Reference:** ISA-5.1; ISA-18.2; first principles

**Difficulty Rationale:** T3 Specialist (3.5×) because Advanced Diagnostic requires sequencing a correct procedure, not just identifying one step

---

## IUK-T3-560-DIAG-032
**Block:** Block 9 - Advanced Diagnostic  
**Tier:** T3 · Specialist/PhD  
**Type:** IDENTIFY  
**Weight:** 3.5×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
A continuous PID loop exhibits integral windup during a prolonged MV saturation. What is the typical symptom when the error reverses direction?

**Correct Answer:**  
Overshoot or delayed recovery caused by the accumulated integral term.

**Required Elements:**
- Overshoot or delayed recovery caused by the accumulated integral term

**Common Wrong Answers:**
- The typical symptom is instant recovery with no overshoot once the error changes sign.
- Windup only affects manual mode and cannot affect automatic PID loops.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — all 1 required elements present and accurate |  
| Partial (high) | 7/10 — 1 of 1 elements correct |  
| Partial (low) | 4/10 — partial answer, key element missing |  
| Zero | 0/10 — incorrect or missing core concept |

**Confidence Penalty Trigger:** model states a definition without citing the applicable standard or first principle

**Reference:** ISA-5.1; ISA-18.2; first principles

**Difficulty Rationale:** T3 Specialist (3.5×) because Advanced Diagnostic requires precise recall of a standard or principle with correct scope

---

## IUK-T3-560-DIAG-033
**Block:** Block 9 - Advanced Diagnostic  
**Tier:** T3 · Specialist/PhD  
**Type:** DIAGNOSE  
**Weight:** 3.5×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
In a cascade control strategy, why is the inner (slave) loop typically tuned more aggressively than the outer (master) loop?

**Correct Answer:**  
To make the slave respond quickly to disturbances so the master sees a well-behaved secondary process.

**Required Elements:**
- To make the slave respond quickly to disturbances so the master sees a well-behaved secondary process

**Common Wrong Answers:**
- The outer loop should always be tuned faster than the inner loop.
- Both master and slave loops should have identical tuning constants.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — correct root cause + physical mechanism + correct fix |  
| Partial (high) | 7/10 — correct root cause, mechanism incomplete |  
| Partial (low) | 4/10 — plausible diagnosis but wrong mechanism |  
| Zero | 0/10 — wrong root cause or dangerous recommendation |

**Confidence Penalty Trigger:** model gives a root cause without citing the physical mechanism or reasoning chain

**Reference:** ISA-5.1; ISA-18.2; first principles

**Difficulty Rationale:** T3 Specialist (3.5×) because Advanced Diagnostic requires multi-step reasoning from symptoms to root cause — a field-level skill

---

## IUK-T3-560-DIAG-034
**Block:** Block 9 - Advanced Diagnostic  
**Tier:** T3 · Specialist/PhD  
**Type:** IDENTIFY  
**Weight:** 3.5×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
A model predictive controller (MPC) is controlling a multivariable distillation column. What is a primary advantage over single-loop PID in this application?

**Correct Answer:**  
Explicit handling of multi-variable interactions, constraints, and economic objectives simultaneously.

**Required Elements:**
- Explicit handling of multi-variable interactions, constraints, and economic objectives simultaneously

**Common Wrong Answers:**
- MPC is mainly useful because it eliminates the need for process measurements.
- Single-loop PID handles interactions and constraints just as well if gain is high enough.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — all 1 required elements present and accurate |  
| Partial (high) | 7/10 — 1 of 1 elements correct |  
| Partial (low) | 4/10 — partial answer, key element missing |  
| Zero | 0/10 — incorrect or missing core concept |

**Confidence Penalty Trigger:** model states a definition without citing the applicable standard or first principle

**Reference:** ISA-5.1; ISA-18.2; first principles

**Difficulty Rationale:** T3 Specialist (3.5×) because Advanced Diagnostic requires precise recall of a standard or principle with correct scope

---

## IUK-T3-560-DIAG-035
**Block:** Block 9 - Advanced Diagnostic  
**Tier:** T3 · Specialist/PhD  
**Type:** DESIGN  
**Weight:** 3.5×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
In override control (selector strategy), what happens when two controllers compete for the same manipulated variable?

**Correct Answer:**  
The selector passes the higher or lower output depending on configuration (max/min select).

**Required Elements:**
- The selector passes the higher or lower output depending on configuration (max/min select)

**Common Wrong Answers:**
- Both controllers are averaged together before driving the valve.
- The controller with the newest tuning constants always wins.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — all 1 required elements present and accurate |  
| Partial (high) | 7/10 — 1 of 1 elements correct |  
| Partial (low) | 4/10 — partial answer, key element missing |  
| Zero | 0/10 — incorrect or missing core concept |

**Confidence Penalty Trigger:** model makes a selection without stating the selection criteria or design constraint

**Reference:** ISA-5.1; ISA-18.2; first principles

**Difficulty Rationale:** T3 Specialist (3.5×) because Advanced Diagnostic requires applying selection criteria under real engineering constraints

---

## IUK-T3-560-DIAG-036
**Block:** Block 9 - Advanced Diagnostic  
**Tier:** T3 · Specialist/PhD  
**Type:** IDENTIFY  
**Weight:** 3.5×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
A feedforward control action is added to a level controller on a surge tank. What condition must be met for perfect disturbance rejection?

**Correct Answer:**  
The feedforward model gain and dynamics must exactly match the real process disturbance path.

**Required Elements:**
- The feedforward model gain and dynamics must exactly match the real process disturbance path

**Common Wrong Answers:**
- Perfect rejection only requires the feedforward signal to move in the correct direction.
- The feedback PID will automatically correct any feedforward model error instantly.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — all 1 required elements present and accurate |  
| Partial (high) | 7/10 — 1 of 1 elements correct |  
| Partial (low) | 4/10 — partial answer, key element missing |  
| Zero | 0/10 — incorrect or missing core concept |

**Confidence Penalty Trigger:** model states a definition without citing the applicable standard or first principle

**Reference:** ISA-5.1; ISA-18.2; first principles

**Difficulty Rationale:** T3 Specialist (3.5×) because Advanced Diagnostic requires precise recall of a standard or principle with correct scope

---

## IUK-T3-560-DIAG-037
**Block:** Block 9 - Advanced Diagnostic  
**Tier:** T3 · Specialist/PhD  
**Type:** APPLY  
**Weight:** 3.5×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
What is the primary purpose of gain scheduling in a nonlinear process such as pH control?

**Correct Answer:**  
To adjust PID parameters dynamically based on operating region, e.g., near neutrality vs. pH extremes.

**Required Elements:**
- To adjust PID parameters dynamically based on operating region, e.g., near neutrality vs. pH extremes

**Common Wrong Answers:**
- Gain scheduling is used to keep the controller output at 50 percent.
- It is mainly a way to change engineering units on the HMI.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — all 1 required elements present and accurate |  
| Partial (high) | 7/10 — 1 of 1 elements correct |  
| Partial (low) | 4/10 — partial answer, key element missing |  
| Zero | 0/10 — incorrect or missing core concept |

**Confidence Penalty Trigger:** model asserts without citing supporting reasoning

**Reference:** ISA-5.1; ISA-18.2; first principles

**Difficulty Rationale:** T3 Specialist (3.5×) because Advanced Diagnostic requires sequencing a correct procedure, not just identifying one step

---

## IUK-T3-560-DIAG-038
**Block:** Block 9 - Advanced Diagnostic  
**Tier:** T3 · Specialist/PhD  
**Type:** IDENTIFY  
**Weight:** 3.5×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
In OPC UA, what feature allows secure, platform-independent data modeling and access compared to classic OPC?

**Correct Answer:**  
Information modeling with nodes and references, plus built-in security: encryption, message signing, and user authentication.

**Required Elements:**
- Information modeling with nodes and references, plus built-in security: encryption, message signing, and user authentication

**Common Wrong Answers:**
- OPC UA is secure because it uses DCOM permissions like classic OPC.
- OPC UA only adds faster polling; it does not change modeling or security.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — all 1 required elements present and accurate |  
| Partial (high) | 7/10 — 1 of 1 elements correct |  
| Partial (low) | 4/10 — partial answer, key element missing |  
| Zero | 0/10 — incorrect or missing core concept |

**Confidence Penalty Trigger:** model states a definition without citing the applicable standard or first principle

**Reference:** ISA-5.1; ISA-18.2; first principles

**Difficulty Rationale:** T3 Specialist (3.5×) because Advanced Diagnostic requires precise recall of a standard or principle with correct scope

---

## IUK-T3-560-DIAG-039
**Block:** Block 9 - Advanced Diagnostic  
**Tier:** T3 · Specialist/PhD  
**Type:** IDENTIFY  
**Weight:** 3.5×  
**Safety Gate:** YES  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
A ratio control loop maintains fuel-to-air ratio in a fired heater. If the air flow transmitter fails low, what should a well-designed override do?

**Correct Answer:**  
Drive fuel to minimum or safe low to prevent rich combustion or explosion risk.

**Required Elements:**
- Drive fuel to minimum or safe low to prevent rich combustion or explosion risk

**Common Wrong Answers:**
- The override should increase fuel to maintain heater duty.
- The override should ignore the air transmitter because ratio control is only advisory.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — all 1 required elements present and accurate |  
| Partial (high) | 7/10 — 1 of 1 elements correct |  
| Partial (low) | 4/10 — partial answer, key element missing |  
| Zero | 0/10 — incorrect or missing core concept |

**Confidence Penalty Trigger:** model states a definition without citing the applicable standard or first principle; model omits or minimizes the safety implication of an incorrect answer

**Reference:** ISA-5.1; ISA-18.2; first principles

**Difficulty Rationale:** T3 Specialist (3.5×) because Advanced Diagnostic requires precise recall of a standard or principle with correct scope

---

## IUK-T3-560-DIAG-040
**Block:** Block 9 - Advanced Diagnostic  
**Tier:** T3 · Specialist/PhD  
**Type:** IDENTIFY  
**Weight:** 3.5×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
In a multi-variable control application, what does RGA (Relative Gain Array) help identify?

**Correct Answer:**  
Loop interactions and pairing recommendations — avoid pairings with RGA near 0 or very large/negative values.

**Required Elements:**
- Loop interactions and pairing recommendations — avoid pairings with RGA near 0 or very large/negative values

**Common Wrong Answers:**
- RGA identifies which thermocouple type should be used in each loop.
- RGA simply ranks loops by economic importance and does not address interactions.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — all 1 required elements present and accurate |  
| Partial (high) | 7/10 — 1 of 1 elements correct |  
| Partial (low) | 4/10 — partial answer, key element missing |  
| Zero | 0/10 — incorrect or missing core concept |

**Confidence Penalty Trigger:** model states a definition without citing the applicable standard or first principle

**Reference:** ISA-5.1; ISA-18.2; first principles

**Difficulty Rationale:** T3 Specialist (3.5×) because Advanced Diagnostic requires precise recall of a standard or principle with correct scope

---

## IUK-T3-560-SFTY-001
**Block:** Block 10 - Safety & Leadership  
**Tier:** T3 · Specialist/PhD  
**Type:** COMPARE  
**Weight:** 3.5×  
**Safety Gate:** YES  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
What is the fundamental difference between a Class I, Division 1 location and a Class I, Division 2 location?

**Correct Answer:**  
Division 1 has ignitable concentrations present under normal operating conditions; Division 2 expects them only under abnormal conditions such as a leak or failure.

**Required Elements:**
- Division 1 has ignitable concentrations present under normal operating conditions
- Division 2 expects them only under abnormal conditions such as a leak or failure

**Common Wrong Answers:**
- Division 1 means a more dangerous chemical, while Division 2 means a less dangerous chemical.
- Division 1 is for indoor areas and Division 2 is for outdoor areas.
- Zone 0 is the same as Class I Division 1 and Zone 1 is the same as Class I Division 2 in all cases.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — all 2 required elements present and accurate |  
| Partial (high) | 7/10 — 1 of 2 elements correct |  
| Partial (low) | 4/10 — partial answer, key element missing |  
| Zero | 0/10 — incorrect or missing core concept |

**Confidence Penalty Trigger:** model conflates the two systems or misattributes a property to the wrong standard; model omits or minimizes the safety implication of an incorrect answer

**Reference:** ISA-84.00.01; IEC 61511; ISA-61511; MOC procedures

**Difficulty Rationale:** T3 Specialist (3.5×) because Safety & Leadership requires understanding of two distinct systems and their domain-specific tradeoffs

---

## IUK-T3-560-SFTY-002
**Block:** Block 10 - Safety & Leadership  
**Tier:** T3 · Specialist/PhD  
**Type:** IDENTIFY  
**Weight:** 3.5×  
**Safety Gate:** YES  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
In the NEC gas-group scheme, which group covers hydrogen?

**Correct Answer:**  
Group B

**Required Elements:**
- Group B

**Common Wrong Answers:**
- Hydrogen is NEC Group A because it is the lightest gas.
- Hydrogen is Group C, the same as ethylene.
- Hydrogen is IEC gas group IIC only, so it has no NEC gas-group classification.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — all 1 required elements present and accurate |  
| Partial (high) | 7/10 — 1 of 1 elements correct |  
| Partial (low) | 4/10 — partial answer, key element missing |  
| Zero | 0/10 — incorrect or missing core concept |

**Confidence Penalty Trigger:** model states a definition without citing the applicable standard or first principle; model omits or minimizes the safety implication of an incorrect answer

**Reference:** ISA-84.00.01; IEC 61511; ISA-61511; MOC procedures

**Difficulty Rationale:** T3 Specialist (3.5×) because Safety & Leadership requires precise recall of a standard or principle with correct scope

---

## IUK-T3-560-SFTY-003
**Block:** Block 10 - Safety & Leadership  
**Tier:** T3 · Specialist/PhD  
**Type:** IDENTIFY  
**Weight:** 3.5×  
**Safety Gate:** YES  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
What does a classic grounded Zener barrier do in an intrinsically safe loop, and where is it typically installed?

**Correct Answer:**  
It limits voltage and current so the hazardous-area circuit cannot release ignition-capable energy, and it is typically installed on the safe/non-hazardous side with a high-integrity ground.

**Required Elements:**
- It limits voltage and current so the hazardous-area circuit cannot release ignition-capable energy, and it is typically installed on the safe/non-hazardous side with a high-integrity ground

**Common Wrong Answers:**
- A Zener barrier boosts the loop voltage so the transmitter can drive a longer cable run.
- The barrier should be installed in the hazardous area next to the field device.
- A Zener barrier makes a loop explosion-proof, so conduit seals and entity parameters no longer matter.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — all 1 required elements present and accurate |  
| Partial (high) | 7/10 — 1 of 1 elements correct |  
| Partial (low) | 4/10 — partial answer, key element missing |  
| Zero | 0/10 — incorrect or missing core concept |

**Confidence Penalty Trigger:** model states a definition without citing the applicable standard or first principle; model omits or minimizes the safety implication of an incorrect answer

**Reference:** ISA-84.00.01; IEC 61511; ISA-61511; MOC procedures

**Difficulty Rationale:** T3 Specialist (3.5×) because Safety & Leadership requires precise recall of a standard or principle with correct scope

---

## IUK-T3-560-SFTY-004
**Block:** Block 10 - Safety & Leadership  
**Tier:** T3 · Specialist/PhD  
**Type:** IDENTIFY  
**Weight:** 3.5×  
**Safety Gate:** YES  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
Is an explosion-proof enclosure intended to be gas-tight or to contain an internal explosion?

**Correct Answer:**  
To contain an internal explosion

**Required Elements:**
- To contain an internal explosion

**Common Wrong Answers:**
- Explosion-proof means the enclosure is completely gas-tight and never allows gas inside.
- Explosion-proof means the enclosure prevents all external explosions in the area.
- It is the same protection method as intrinsic safety because both simply limit voltage.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — all 1 required elements present and accurate |  
| Partial (high) | 7/10 — 1 of 1 elements correct |  
| Partial (low) | 4/10 — partial answer, key element missing |  
| Zero | 0/10 — incorrect or missing core concept |

**Confidence Penalty Trigger:** model states a definition without citing the applicable standard or first principle; model omits or minimizes the safety implication of an incorrect answer

**Reference:** ISA-84.00.01; IEC 61511; ISA-61511; MOC procedures

**Difficulty Rationale:** T3 Specialist (3.5×) because Safety & Leadership requires precise recall of a standard or principle with correct scope

---

## IUK-T3-560-SFTY-005
**Block:** Block 10 - Safety & Leadership  
**Tier:** T3 · Specialist/PhD  
**Type:** COMPARE  
**Weight:** 3.5×  
**Safety Gate:** YES  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
What is the difference between a Type X purge and a Type Z purge?

**Correct Answer:**  
Type X reduces a Div 1 enclosure to unclassified/non-hazardous; Type Z reduces a Div 2 enclosure to unclassified/non-hazardous

**Required Elements:**
- Type X reduces a Div 1 enclosure to unclassified/non-hazardous
- Type Z reduces a Div 2 enclosure to unclassified/non-hazardous

**Common Wrong Answers:**
- Type X and Type Z purges are the same; the only difference is purge air flow rate.
- Type Z is for Division 1 and Type X is for Division 2.
- Type X and Type Z are IEC Zone designations rather than NEC/NFPA purge types.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — all 2 required elements present and accurate |  
| Partial (high) | 7/10 — 1 of 2 elements correct |  
| Partial (low) | 4/10 — partial answer, key element missing |  
| Zero | 0/10 — incorrect or missing core concept |

**Confidence Penalty Trigger:** model conflates the two systems or misattributes a property to the wrong standard; model omits or minimizes the safety implication of an incorrect answer

**Reference:** ISA-84.00.01; IEC 61511; ISA-61511; MOC procedures

**Difficulty Rationale:** T3 Specialist (3.5×) because Safety & Leadership requires understanding of two distinct systems and their domain-specific tradeoffs

---

## IUK-T3-560-SFTY-006
**Block:** Block 10 - Safety & Leadership  
**Tier:** T3 · Specialist/PhD  
**Type:** IDENTIFY  
**Weight:** 3.5×  
**Safety Gate:** YES  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
What does SIL stand for, and which of SIL 1, 2, or 3 provides the greatest risk reduction?

**Correct Answer:**  
Safety Integrity Level; SIL 3

**Required Elements:**
- Safety Integrity Level

**Common Wrong Answers:**
- SIL means Standard Instrument Loop, and SIL 1 gives the greatest risk reduction.
- SIL is only a device quality rating and does not apply to a complete safety function.
- SIL 3 is less safe than SIL 1 because the number indicates allowed failures.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — all 1 required elements present and accurate |  
| Partial (high) | 7/10 — 1 of 1 elements correct |  
| Partial (low) | 4/10 — partial answer, key element missing |  
| Zero | 0/10 — incorrect or missing core concept |

**Confidence Penalty Trigger:** model states a definition without citing the applicable standard or first principle; model omits or minimizes the safety implication of an incorrect answer

**Reference:** ISA-84.00.01; IEC 61511; ISA-61511; MOC procedures

**Difficulty Rationale:** T3 Specialist (3.5×) because Safety & Leadership requires precise recall of a standard or principle with correct scope

---

## IUK-T3-560-SFTY-007
**Block:** Block 10 - Safety & Leadership  
**Tier:** T3 · Specialist/PhD  
**Type:** IDENTIFY  
**Weight:** 3.5×  
**Safety Gate:** YES  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
What does PFDavg measure?

**Correct Answer:**  
The average probability that a safety function will fail to act on demand

**Required Elements:**
- The average probability that a safety function will fail to act on demand

**Common Wrong Answers:**
- PFDavg is the probability that the safety function will trip accidentally.
- PFDavg is the percent of time the plant is shut down by the SIS.
- PFDavg is the same as controller proportional band.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — all 1 required elements present and accurate |  
| Partial (high) | 7/10 — 1 of 1 elements correct |  
| Partial (low) | 4/10 — partial answer, key element missing |  
| Zero | 0/10 — incorrect or missing core concept |

**Confidence Penalty Trigger:** model states a definition without citing the applicable standard or first principle; model omits or minimizes the safety implication of an incorrect answer

**Reference:** ISA-84.00.01; IEC 61511; ISA-61511; MOC procedures

**Difficulty Rationale:** T3 Specialist (3.5×) because Safety & Leadership requires precise recall of a standard or principle with correct scope

---

## IUK-T3-560-SFTY-008
**Block:** Block 10 - Safety & Leadership  
**Tier:** T3 · Specialist/PhD  
**Type:** DIAGNOSE  
**Weight:** 3.5×  
**Safety Gate:** YES  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
Why is a calibration check not the same thing as a safety proof test?

**Correct Answer:**  
Calibration checks accuracy of the device signal; proof testing verifies the full safety function and uncovers hidden dangerous failures

**Required Elements:**
- Calibration checks accuracy of the device signal
- proof testing verifies the full safety function and uncovers hidden dangerous failures

**Common Wrong Answers:**
- A calibration check proves the entire safety loop because the transmitter reads correctly.
- Proof testing only verifies the transmitter zero and span.
- If the DCS trend looks normal, no proof test is needed.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — correct root cause + physical mechanism + correct fix |  
| Partial (high) | 7/10 — correct root cause, mechanism incomplete |  
| Partial (low) | 4/10 — plausible diagnosis but wrong mechanism |  
| Zero | 0/10 — wrong root cause or dangerous recommendation |

**Confidence Penalty Trigger:** model gives a root cause without citing the physical mechanism or reasoning chain; model omits or minimizes the safety implication of an incorrect answer

**Reference:** ISA-84.00.01; IEC 61511; ISA-61511; MOC procedures

**Difficulty Rationale:** T3 Specialist (3.5×) because Safety & Leadership requires multi-step reasoning from symptoms to root cause — a field-level skill

---

## IUK-T3-560-SFTY-009
**Block:** Block 10 - Safety & Leadership  
**Tier:** T3 · Specialist/PhD  
**Type:** IDENTIFY  
**Weight:** 3.5×  
**Safety Gate:** YES  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
Is a standard BPCS considered an independent protection layer in the same sense as the SIS?

**Correct Answer:**  
Not automatically. It is not the SIS, and it only receives IPL credit if independence and other LOPA criteria are truly met.

**Required Elements:**
- Not automatically
- It is not the SIS, and it only receives IPL credit if independence and other LOPA criteria are truly met

**Common Wrong Answers:**
- A standard BPCS always counts as an IPL because it already controls the process.
- The BPCS and SIS can share the same sensor and still get full independent IPL credit.
- An operator alarm in the DCS automatically gives the same credit as an SIS trip.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — all 2 required elements present and accurate |  
| Partial (high) | 7/10 — 1 of 2 elements correct |  
| Partial (low) | 4/10 — partial answer, key element missing |  
| Zero | 0/10 — incorrect or missing core concept |

**Confidence Penalty Trigger:** model states a definition without citing the applicable standard or first principle; model omits or minimizes the safety implication of an incorrect answer

**Reference:** ISA-84.00.01; IEC 61511; ISA-61511; MOC procedures

**Difficulty Rationale:** T3 Specialist (3.5×) because Safety & Leadership requires precise recall of a standard or principle with correct scope

---

## IUK-T3-560-SFTY-010
**Block:** Block 10 - Safety & Leadership  
**Tier:** T3 · Specialist/PhD  
**Type:** IDENTIFY  
**Weight:** 3.5×  
**Safety Gate:** YES  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
A device is marked T4. What does that tell you?

**Correct Answer:**  
Its maximum surface temperature will not exceed 135 degC

**Required Elements:**
- Its maximum surface temperature will not exceed 135 degC

**Common Wrong Answers:**
- T4 means the equipment is suitable up to 400 degC ambient temperature.
- T4 means the device is rated for Zone 4 or Division 4 hazardous areas.
- T4 means the device is intrinsically safe for all gas groups.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — all 1 required elements present and accurate |  
| Partial (high) | 7/10 — 1 of 1 elements correct |  
| Partial (low) | 4/10 — partial answer, key element missing |  
| Zero | 0/10 — incorrect or missing core concept |

**Confidence Penalty Trigger:** model states a definition without citing the applicable standard or first principle; model omits or minimizes the safety implication of an incorrect answer

**Reference:** ISA-84.00.01; IEC 61511; ISA-61511; MOC procedures

**Difficulty Rationale:** T3 Specialist (3.5×) because Safety & Leadership requires precise recall of a standard or principle with correct scope

---

## IUK-T3-560-SFTY-011
**Block:** Block 10 - Safety & Leadership  
**Tier:** T3 · Specialist/PhD  
**Type:** APPLY  
**Weight:** 3.5×  
**Safety Gate:** YES  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
What is OSHA Process Safety Management, and what chlorine quantity triggers PSM coverage?

**Correct Answer:**  
PSM is OSHA’s process-safety rule for highly hazardous chemicals and covered flammables; chlorine is listed at 1,500 pounds.

**Required Elements:**
- PSM is OSHA’s process-safety rule for highly hazardous chemicals and covered flammables
- chlorine is listed at 1,500 pounds

**Common Wrong Answers:**
- PSM only applies after an incident occurs, and chlorine is covered at 500 pounds.
- PSM is an environmental reporting rule, and chlorine triggers at 10,000 pounds like many flammables.
- PSM coverage is based only on tank pressure, not chemical quantity.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — all 2 required elements present and accurate |  
| Partial (high) | 7/10 — 1 of 2 elements correct |  
| Partial (low) | 4/10 — partial answer, key element missing |  
| Zero | 0/10 — incorrect or missing core concept |

**Confidence Penalty Trigger:** model omits or minimizes the safety implication of an incorrect answer

**Reference:** ISA-84.00.01; IEC 61511; ISA-61511; MOC procedures

**Difficulty Rationale:** T3 Specialist (3.5×) because Safety & Leadership requires sequencing a correct procedure, not just identifying one step

---

## IUK-T3-560-SFTY-012
**Block:** Block 10 - Safety & Leadership  
**Tier:** T3 · Specialist/PhD  
**Type:** IDENTIFY  
**Weight:** 3.5×  
**Safety Gate:** YES  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
If you replace a failed transmitter with an identical like-for-like model, is a formal MOC usually required?

**Correct Answer:**  
No

**Required Elements:**
- No

**Common Wrong Answers:**
- Yes, every transmitter replacement requires a full formal MOC even if model, range, materials, and service are unchanged.
- No paperwork of any kind is needed because maintenance work is never part of MOC.
- Only the vendor decides whether the replacement is like-for-like.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — all 1 required elements present and accurate |  
| Partial (high) | 7/10 — 1 of 1 elements correct |  
| Partial (low) | 4/10 — partial answer, key element missing |  
| Zero | 0/10 — incorrect or missing core concept |

**Confidence Penalty Trigger:** model states a definition without citing the applicable standard or first principle; model omits or minimizes the safety implication of an incorrect answer

**Reference:** ISA-84.00.01; IEC 61511; ISA-61511; MOC procedures

**Difficulty Rationale:** T3 Specialist (3.5×) because Safety & Leadership requires precise recall of a standard or principle with correct scope

---

## IUK-T3-560-SFTY-013
**Block:** Block 10 - Safety & Leadership  
**Tier:** T3 · Specialist/PhD  
**Type:** IDENTIFY  
**Weight:** 3.5×  
**Safety Gate:** YES  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
What does Pre-Startup Safety Review mean, and when is it performed?

**Correct Answer:**  
It is the review required before introducing hazardous chemicals after a covered change, project, or turnaround that affects process safety information or operating procedures.

**Required Elements:**
- It is the review required before introducing hazardous chemicals after a covered change, project, or turnaround that affects process safety information or operating procedures

**Common Wrong Answers:**
- PSSR is a review performed after startup to document what went wrong.
- PSSR is only a maintenance checklist for instrument calibration stickers.
- PSSR is required only for brand-new plants, never after a turnaround or covered modification.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — all 1 required elements present and accurate |  
| Partial (high) | 7/10 — 1 of 1 elements correct |  
| Partial (low) | 4/10 — partial answer, key element missing |  
| Zero | 0/10 — incorrect or missing core concept |

**Confidence Penalty Trigger:** model states a definition without citing the applicable standard or first principle; model omits or minimizes the safety implication of an incorrect answer

**Reference:** ISA-84.00.01; IEC 61511; ISA-61511; MOC procedures

**Difficulty Rationale:** T3 Specialist (3.5×) because Safety & Leadership requires precise recall of a standard or principle with correct scope

---

## IUK-T3-560-SFTY-014
**Block:** Block 10 - Safety & Leadership  
**Tier:** T3 · Specialist/PhD  
**Type:** DIAGNOSE  
**Weight:** 3.5×  
**Safety Gate:** YES  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
Why is it unsafe to leave a field modification such as a bypassed switch off the official P\&ID?

**Correct Answer:**  
Because operators, maintenance, and emergency responders then work from false information about how the system actually behaves

**Required Elements:**
- Because operators, maintenance, and emergency responders then work from false information about how the system actually behaves

**Common Wrong Answers:**
- It is acceptable if the mechanic remembers the jumper and tells the next shift verbally.
- P\&IDs only show original design, so field changes do not need to be documented.
- A bypassed switch is safe as long as the PLC logic still shows the old input.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — correct root cause + physical mechanism + correct fix |  
| Partial (high) | 7/10 — correct root cause, mechanism incomplete |  
| Partial (low) | 4/10 — plausible diagnosis but wrong mechanism |  
| Zero | 0/10 — wrong root cause or dangerous recommendation |

**Confidence Penalty Trigger:** model gives a root cause without citing the physical mechanism or reasoning chain; model omits or minimizes the safety implication of an incorrect answer

**Reference:** ISA-84.00.01; IEC 61511; ISA-61511; MOC procedures

**Difficulty Rationale:** T3 Specialist (3.5×) because Safety & Leadership requires multi-step reasoning from symptoms to root cause — a field-level skill

---

## IUK-T3-560-SFTY-015
**Block:** Block 10 - Safety & Leadership  
**Tier:** T3 · Specialist/PhD  
**Type:** IDENTIFY  
**Weight:** 3.5×  
**Safety Gate:** YES  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
According to LOTO rules, who is normally authorized to remove a personal lock?

**Correct Answer:**  
The person who applied it

**Required Elements:**
- The person who applied it

**Common Wrong Answers:**
- Any supervisor may remove a personal lock once the job is behind schedule.
- The control-room operator may remove all personal locks during shift change.
- A contractor's lock can be removed by a plant employee without a formal lock-removal procedure.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — all 1 required elements present and accurate |  
| Partial (high) | 7/10 — 1 of 1 elements correct |  
| Partial (low) | 4/10 — partial answer, key element missing |  
| Zero | 0/10 — incorrect or missing core concept |

**Confidence Penalty Trigger:** model states a definition without citing the applicable standard or first principle; model omits or minimizes the safety implication of an incorrect answer

**Reference:** ISA-84.00.01; IEC 61511; ISA-61511; MOC procedures

**Difficulty Rationale:** T3 Specialist (3.5×) because Safety & Leadership requires precise recall of a standard or principle with correct scope

---

## IUK-T3-560-SFTY-016
**Block:** Block 10 - Safety & Leadership  
**Tier:** T3 · Specialist/PhD  
**Type:** IDENTIFY  
**Weight:** 3.5×  
**Safety Gate:** YES  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
Does turning a pump HOA switch off at the MCC establish a zero-energy state?

**Correct Answer:**  
No

**Required Elements:**
- No

**Common Wrong Answers:**
- Yes, turning the HOA switch to OFF proves zero energy because the pump cannot start from the DCS.
- Yes, if the HMI shows the pump stopped, no further isolation is needed.
- An MCC HOA switch is equivalent to locking out the breaker disconnect.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — all 1 required elements present and accurate |  
| Partial (high) | 7/10 — 1 of 1 elements correct |  
| Partial (low) | 4/10 — partial answer, key element missing |  
| Zero | 0/10 — incorrect or missing core concept |

**Confidence Penalty Trigger:** model states a definition without citing the applicable standard or first principle; model omits or minimizes the safety implication of an incorrect answer

**Reference:** ISA-84.00.01; IEC 61511; ISA-61511; MOC procedures

**Difficulty Rationale:** T3 Specialist (3.5×) because Safety & Leadership requires precise recall of a standard or principle with correct scope

---

## IUK-T3-560-SFTY-017
**Block:** Block 10 - Safety & Leadership  
**Tier:** T3 · Specialist/PhD  
**Type:** IDENTIFY  
**Weight:** 3.5×  
**Safety Gate:** YES  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
What is the limited approach boundary commonly associated with exposed 480 V parts under NFPA 70E?

**Correct Answer:**  
3 feet 6 inches

**Required Elements:**
- 3 feet 6 inches

**Common Wrong Answers:**
- The limited approach boundary for 480 V is 12 inches.
- It is always 10 feet for any voltage above 50 V.
- Limited approach applies only to high-voltage transmission work, not 480 V MCCs.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — all 1 required elements present and accurate |  
| Partial (high) | 7/10 — 1 of 1 elements correct |  
| Partial (low) | 4/10 — partial answer, key element missing |  
| Zero | 0/10 — incorrect or missing core concept |

**Confidence Penalty Trigger:** model states a definition without citing the applicable standard or first principle; model omits or minimizes the safety implication of an incorrect answer

**Reference:** ISA-84.00.01; IEC 61511; ISA-61511; MOC procedures

**Difficulty Rationale:** T3 Specialist (3.5×) because Safety & Leadership requires precise recall of a standard or principle with correct scope

---

## IUK-T3-560-SFTY-018
**Block:** Block 10 - Safety & Leadership  
**Tier:** T3 · Specialist/PhD  
**Type:** IDENTIFY  
**Weight:** 3.5×  
**Safety Gate:** YES  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
If incident energy is 8 cal/cm2, what minimum PPE category applies?

**Correct Answer:**  
Category 2

**Required Elements:**
- Category 2

**Common Wrong Answers:**
- 8 cal/cm2 requires Category 4 PPE.
- 8 cal/cm2 is low enough for normal cotton work clothes.
- PPE category is based on voltage only, so incident energy is irrelevant.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — all 1 required elements present and accurate |  
| Partial (high) | 7/10 — 1 of 1 elements correct |  
| Partial (low) | 4/10 — partial answer, key element missing |  
| Zero | 0/10 — incorrect or missing core concept |

**Confidence Penalty Trigger:** model states a definition without citing the applicable standard or first principle; model omits or minimizes the safety implication of an incorrect answer

**Reference:** ISA-84.00.01; IEC 61511; ISA-61511; MOC procedures

**Difficulty Rationale:** T3 Specialist (3.5×) because Safety & Leadership requires precise recall of a standard or principle with correct scope

---

## IUK-T3-560-SFTY-019
**Block:** Block 10 - Safety & Leadership  
**Tier:** T3 · Specialist/PhD  
**Type:** COMPARE  
**Weight:** 3.5×  
**Safety Gate:** YES  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
What is the difference between a qualified and unqualified person under NFPA 70E?

**Correct Answer:**  
A qualified person has the training and demonstrated skills to identify and avoid the electrical hazards of the specific equipment and task; an unqualified person does not.

**Required Elements:**
- A qualified person has the training and demonstrated skills to identify and avoid the electrical hazards of the specific equipment and task
- an unqualified person does not

**Common Wrong Answers:**
- A qualified person is simply anyone with more seniority or a journeyman card.
- An unqualified person can perform the same exposed work if a qualified person is nearby.
- The difference is job title only; task-specific hazard training does not matter.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — all 2 required elements present and accurate |  
| Partial (high) | 7/10 — 1 of 2 elements correct |  
| Partial (low) | 4/10 — partial answer, key element missing |  
| Zero | 0/10 — incorrect or missing core concept |

**Confidence Penalty Trigger:** model conflates the two systems or misattributes a property to the wrong standard; model omits or minimizes the safety implication of an incorrect answer

**Reference:** ISA-84.00.01; IEC 61511; ISA-61511; MOC procedures

**Difficulty Rationale:** T3 Specialist (3.5×) because Safety & Leadership requires understanding of two distinct systems and their domain-specific tradeoffs

---

## IUK-T3-560-SFTY-020
**Block:** Block 10 - Safety & Leadership  
**Tier:** T3 · Specialist/PhD  
**Type:** IDENTIFY  
**Weight:** 3.5×  
**Safety Gate:** YES  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
Why bond two metal tanks together during flammable liquid transfer?

**Correct Answer:**  
To equalize electrical potential and prevent a static spark between them

**Required Elements:**
- To equalize electrical potential and prevent a static spark between them

**Common Wrong Answers:**
- Bonding drains the tanks to earth and prevents all lightning strikes.
- Bonding is only needed after transfer is complete to remove leftover charge.
- Grounding one tank is enough; the two tanks do not need to be bonded to each other.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — all 1 required elements present and accurate |  
| Partial (high) | 7/10 — 1 of 1 elements correct |  
| Partial (low) | 4/10 — partial answer, key element missing |  
| Zero | 0/10 — incorrect or missing core concept |

**Confidence Penalty Trigger:** model states a definition without citing the applicable standard or first principle; model omits or minimizes the safety implication of an incorrect answer

**Reference:** ISA-84.00.01; IEC 61511; ISA-61511; MOC procedures

**Difficulty Rationale:** T3 Specialist (3.5×) because Safety & Leadership requires precise recall of a standard or principle with correct scope

---

## IUK-T3-560-SFTY-021
**Block:** Block 10 - Safety & Leadership  
**Tier:** T3 · Specialist/PhD  
**Type:** IDENTIFY  
**Weight:** 3.5×  
**Safety Gate:** YES  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
Under what condition do you have the right to refuse a work assignment?

**Correct Answer:**  
When it presents an imminent danger or serious unmitigated hazard to life or health

**Required Elements:**
- When it presents an imminent danger or serious unmitigated hazard to life or health

**Common Wrong Answers:**
- You can refuse any assignment that is uncomfortable or inconvenient.
- You must perform the work first and file a concern afterward.
- Only a supervisor has the right to stop work for safety.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — all 1 required elements present and accurate |  
| Partial (high) | 7/10 — 1 of 1 elements correct |  
| Partial (low) | 4/10 — partial answer, key element missing |  
| Zero | 0/10 — incorrect or missing core concept |

**Confidence Penalty Trigger:** model states a definition without citing the applicable standard or first principle; model omits or minimizes the safety implication of an incorrect answer

**Reference:** ISA-84.00.01; IEC 61511; ISA-61511; MOC procedures

**Difficulty Rationale:** T3 Specialist (3.5×) because Safety & Leadership requires precise recall of a standard or principle with correct scope

---

## IUK-T3-560-SFTY-022
**Block:** Block 10 - Safety & Leadership  
**Tier:** T3 · Specialist/PhD  
**Type:** IDENTIFY  
**Weight:** 3.5×  
**Safety Gate:** YES  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
What is a near miss, and why should it be reported?

**Correct Answer:**  
An event that caused no injury or damage this time but easily could have; reporting it helps prevent a future serious event

**Required Elements:**
- An event that caused no injury or damage this time but easily could have
- reporting it helps prevent a future serious event

**Common Wrong Answers:**
- A near miss is not reportable because nobody was hurt and nothing broke.
- Near misses should be handled informally so they do not affect safety statistics.
- A near miss means a minor injury, not an event that could have caused one.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — all 2 required elements present and accurate |  
| Partial (high) | 7/10 — 1 of 2 elements correct |  
| Partial (low) | 4/10 — partial answer, key element missing |  
| Zero | 0/10 — incorrect or missing core concept |

**Confidence Penalty Trigger:** model states a definition without citing the applicable standard or first principle; model omits or minimizes the safety implication of an incorrect answer

**Reference:** ISA-84.00.01; IEC 61511; ISA-61511; MOC procedures

**Difficulty Rationale:** T3 Specialist (3.5×) because Safety & Leadership requires precise recall of a standard or principle with correct scope

---

## IUK-T3-560-SFTY-023
**Block:** Block 10 - Safety & Leadership  
**Tier:** T3 · Specialist/PhD  
**Type:** IDENTIFY  
**Weight:** 3.5×  
**Safety Gate:** YES  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
In a Division 1 area, why are non-approved portable tools such as an ordinary battery drill a serious concern?

**Correct Answer:**  
Because any portable device that is not approved for the classified location can become an ignition source through arcing, hot surfaces, or failure modes.

**Required Elements:**
- Because any portable device that is not approved for the classified location can become an ignition source through arcing, hot surfaces, or failure modes

**Common Wrong Answers:**
- A battery drill is safe in Division 1 because it has no power cord.
- Portable tools are acceptable if used quickly before gas can accumulate.
- A hot-work permit alone makes ordinary portable electronics approved for Division 1.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — all 1 required elements present and accurate |  
| Partial (high) | 7/10 — 1 of 1 elements correct |  
| Partial (low) | 4/10 — partial answer, key element missing |  
| Zero | 0/10 — incorrect or missing core concept |

**Confidence Penalty Trigger:** model states a definition without citing the applicable standard or first principle; model omits or minimizes the safety implication of an incorrect answer

**Reference:** ISA-84.00.01; IEC 61511; ISA-61511; MOC procedures

**Difficulty Rationale:** T3 Specialist (3.5×) because Safety & Leadership requires precise recall of a standard or principle with correct scope

---

## IUK-T3-560-SFTY-024
**Block:** Block 10 - Safety & Leadership  
**Tier:** T3 · Specialist/PhD  
**Type:** DIAGNOSE  
**Weight:** 3.5×  
**Safety Gate:** YES  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
What is a bypass log, and why is it critical?

**Correct Answer:**  
A controlled record of inhibited or bypassed safety devices/functions so they are tracked, reviewed, and returned to service

**Required Elements:**
- A controlled record of inhibited or bypassed safety devices/functions so they are tracked, reviewed, and returned to service

**Common Wrong Answers:**
- A bypass log is just a personal notebook of shortcuts used during troubleshooting.
- Bypassed devices do not need tracking if the operator knows about them.
- The log is only for nuisance alarms, not safety interlocks or inhibited trips.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — correct root cause + physical mechanism + correct fix |  
| Partial (high) | 7/10 — correct root cause, mechanism incomplete |  
| Partial (low) | 4/10 — plausible diagnosis but wrong mechanism |  
| Zero | 0/10 — wrong root cause or dangerous recommendation |

**Confidence Penalty Trigger:** model gives a root cause without citing the physical mechanism or reasoning chain; model omits or minimizes the safety implication of an incorrect answer

**Reference:** ISA-84.00.01; IEC 61511; ISA-61511; MOC procedures

**Difficulty Rationale:** T3 Specialist (3.5×) because Safety & Leadership requires multi-step reasoning from symptoms to root cause — a field-level skill

---

## IUK-T3-560-SFTY-025
**Block:** Block 10 - Safety & Leadership  
**Tier:** T3 · Specialist/PhD  
**Type:** IDENTIFY  
**Weight:** 3.5×  
**Safety Gate:** YES  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
What is the role of a union safety representative during an RCA?

**Correct Answer:**  
To help ensure the investigation addresses systemic causes, worker reality, and corrective actions instead of degenerating into blame shifting

**Required Elements:**
- To help ensure the investigation addresses systemic causes, worker reality, and corrective actions instead of degenerating into blame shifting

**Common Wrong Answers:**
- The union safety representative's role is to assign individual blame for the incident.
- The union representative should stay out of the RCA because it is an engineering-only activity.
- The representative only signs attendance and has no role in corrective actions.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — all 1 required elements present and accurate |  
| Partial (high) | 7/10 — 1 of 1 elements correct |  
| Partial (low) | 4/10 — partial answer, key element missing |  
| Zero | 0/10 — incorrect or missing core concept |

**Confidence Penalty Trigger:** model states a definition without citing the applicable standard or first principle; model omits or minimizes the safety implication of an incorrect answer

**Reference:** ISA-84.00.01; IEC 61511; ISA-61511; MOC procedures

**Difficulty Rationale:** T3 Specialist (3.5×) because Safety & Leadership requires precise recall of a standard or principle with correct scope

---

## IUK-T3-560-SFTY-026
**Block:** Block 10 - Safety & Leadership  
**Tier:** T3 · Specialist/PhD  
**Type:** IDENTIFY  
**Weight:** 3.5×  
**Safety Gate:** YES  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
Is a NEMA 4X enclosure rated for submersion?

**Correct Answer:**  
No; it is for corrosion resistance and hose-directed water, not submersion

**Required Elements:**
- it is for corrosion resistance and hose-directed water, not submersion

**Common Wrong Answers:**
- Yes, NEMA 4X is waterproof for continuous submersion.
- NEMA 4X is the same as NEMA 7 explosion-proof.
- NEMA 4X only means dust-tight and has nothing to do with corrosion or hose-down water.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — all 1 required elements present and accurate |  
| Partial (high) | 7/10 — 1 of 1 elements correct |  
| Partial (low) | 4/10 — partial answer, key element missing |  
| Zero | 0/10 — incorrect or missing core concept |

**Confidence Penalty Trigger:** model states a definition without citing the applicable standard or first principle; model omits or minimizes the safety implication of an incorrect answer

**Reference:** ISA-84.00.01; IEC 61511; ISA-61511; MOC procedures

**Difficulty Rationale:** T3 Specialist (3.5×) because Safety & Leadership requires precise recall of a standard or principle with correct scope

---

## IUK-T3-560-SFTY-027
**Block:** Block 10 - Safety & Leadership  
**Tier:** T3 · Specialist/PhD  
**Type:** IDENTIFY  
**Weight:** 3.5×  
**Safety Gate:** YES  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
What is the purpose of an EYS or similar conduit seal fitting in Division 1 service?

**Correct Answer:**  
To stop flame, hot gases, or vapors from propagating through the conduit system

**Required Elements:**
- To stop flame, hot gases, or vapors from propagating through the conduit system

**Common Wrong Answers:**
- An EYS seal keeps rainwater out of the conduit.
- It is installed only to make wire pulling easier at bends.
- It converts any ordinary enclosure into an intrinsically safe installation.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — all 1 required elements present and accurate |  
| Partial (high) | 7/10 — 1 of 1 elements correct |  
| Partial (low) | 4/10 — partial answer, key element missing |  
| Zero | 0/10 — incorrect or missing core concept |

**Confidence Penalty Trigger:** model states a definition without citing the applicable standard or first principle; model omits or minimizes the safety implication of an incorrect answer

**Reference:** ISA-84.00.01; IEC 61511; ISA-61511; MOC procedures

**Difficulty Rationale:** T3 Specialist (3.5×) because Safety & Leadership requires precise recall of a standard or principle with correct scope

---

## IUK-T3-560-SFTY-028
**Block:** Block 10 - Safety & Leadership  
**Tier:** T3 · Specialist/PhD  
**Type:** IDENTIFY  
**Weight:** 3.5×  
**Safety Gate:** YES  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
Can nonincendive equipment be used in Division 1?

**Correct Answer:**  
No

**Required Elements:**
- No

**Common Wrong Answers:**
- Yes, nonincendive equipment is acceptable in Division 1 if the voltage is 24 VDC.
- Yes, nonincendive and intrinsically safe mean the same thing.
- It can be used in Division 1 as long as the area is normally ventilated.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — all 1 required elements present and accurate |  
| Partial (high) | 7/10 — 1 of 1 elements correct |  
| Partial (low) | 4/10 — partial answer, key element missing |  
| Zero | 0/10 — incorrect or missing core concept |

**Confidence Penalty Trigger:** model states a definition without citing the applicable standard or first principle; model omits or minimizes the safety implication of an incorrect answer

**Reference:** ISA-84.00.01; IEC 61511; ISA-61511; MOC procedures

**Difficulty Rationale:** T3 Specialist (3.5×) because Safety & Leadership requires precise recall of a standard or principle with correct scope

---

## IUK-T3-560-SFTY-029
**Block:** Block 10 - Safety & Leadership  
**Tier:** T3 · Specialist/PhD  
**Type:** DIAGNOSE  
**Weight:** 3.5×  
**Safety Gate:** YES  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
Why is it dangerous to paint over explosion-proof flange joints or threads?

**Correct Answer:**  
Because paint can interfere with the flamepath and heat-dissipation characteristics of the joint

**Required Elements:**
- Because paint can interfere with the flamepath and heat-dissipation characteristics of the joint

**Common Wrong Answers:**
- Paint improves explosion-proof joints by sealing gas out of the threads.
- Paint is harmless because explosion-proof protection only depends on enclosure wall thickness.
- Only conduit threads matter; cover flange flamepaths can be painted over.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — correct root cause + physical mechanism + correct fix |  
| Partial (high) | 7/10 — correct root cause, mechanism incomplete |  
| Partial (low) | 4/10 — plausible diagnosis but wrong mechanism |  
| Zero | 0/10 — wrong root cause or dangerous recommendation |

**Confidence Penalty Trigger:** model gives a root cause without citing the physical mechanism or reasoning chain; model omits or minimizes the safety implication of an incorrect answer

**Reference:** ISA-84.00.01; IEC 61511; ISA-61511; MOC procedures

**Difficulty Rationale:** T3 Specialist (3.5×) because Safety & Leadership requires multi-step reasoning from symptoms to root cause — a field-level skill

---

## IUK-T3-560-SFTY-030
**Block:** Block 10 - Safety & Leadership  
**Tier:** T3 · Specialist/PhD  
**Type:** APPLY  
**Weight:** 3.5×  
**Safety Gate:** YES  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
What is the live-dead-live test-before-touch procedure?

**Correct Answer:**  
Verify the meter on a known live source, test the target circuit to confirm it is dead, then re-check the meter on a known live source.

**Required Elements:**
- Verify the meter on a known live source, test the target circuit to confirm it is dead, then re-check the meter on a known live source

**Common Wrong Answers:**
- Test the target circuit once, then trust the meter for the rest of the job.
- Check the meter on a live source only after the circuit tests dead.
- Use continuity mode instead of voltage mode to prove the circuit is de-energized.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — all 1 required elements present and accurate |  
| Partial (high) | 7/10 — 1 of 1 elements correct |  
| Partial (low) | 4/10 — partial answer, key element missing |  
| Zero | 0/10 — incorrect or missing core concept |

**Confidence Penalty Trigger:** model omits or minimizes the safety implication of an incorrect answer

**Reference:** ISA-84.00.01; IEC 61511; ISA-61511; MOC procedures

**Difficulty Rationale:** T3 Specialist (3.5×) because Safety & Leadership requires sequencing a correct procedure, not just identifying one step

---

## IUK-T3-560-SFTY-031
**Block:** Block 10 - Safety & Leadership  
**Tier:** T3 · Specialist/PhD  
**Type:** DIAGNOSE  
**Weight:** 3.5×  
**Safety Gate:** YES  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
What is PRV simmer or chatter, and why is it damaging?

**Correct Answer:**  
Rapid repeated opening/closing or unstable leakage at the seat that damages seating surfaces and can stress connected piping

**Required Elements:**
- Rapid repeated opening/closing or unstable leakage at the seat that damages seating surfaces and can stress connected piping

**Common Wrong Answers:**
- PRV chatter is normal vibration that proves the valve is relieving correctly.
- Simmer means the PRV opens fully and smoothly at set pressure.
- Chatter only damages the spring, not the seat or connected piping.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — correct root cause + physical mechanism + correct fix |  
| Partial (high) | 7/10 — correct root cause, mechanism incomplete |  
| Partial (low) | 4/10 — plausible diagnosis but wrong mechanism |  
| Zero | 0/10 — wrong root cause or dangerous recommendation |

**Confidence Penalty Trigger:** model gives a root cause without citing the physical mechanism or reasoning chain; model omits or minimizes the safety implication of an incorrect answer

**Reference:** ISA-84.00.01; IEC 61511; ISA-61511; MOC procedures

**Difficulty Rationale:** T3 Specialist (3.5×) because Safety & Leadership requires multi-step reasoning from symptoms to root cause — a field-level skill

---

## IUK-T3-560-SFTY-032
**Block:** Block 10 - Safety & Leadership  
**Tier:** T3 · Specialist/PhD  
**Type:** IDENTIFY  
**Weight:** 3.5×  
**Safety Gate:** YES  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
Why are rupture disks often installed upstream of a PRV?

**Correct Answer:**  
To isolate the PRV from corrosive or fouling process fluid and protect its internals

**Required Elements:**
- To isolate the PRV from corrosive or fouling process fluid and protect its internals

**Common Wrong Answers:**
- Rupture disks are installed upstream of PRVs to increase the set pressure.
- The disk is a backup valve that reseats after the PRV opens.
- A rupture disk eliminates the need to size or inspect the PRV.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — all 1 required elements present and accurate |  
| Partial (high) | 7/10 — 1 of 1 elements correct |  
| Partial (low) | 4/10 — partial answer, key element missing |  
| Zero | 0/10 — incorrect or missing core concept |

**Confidence Penalty Trigger:** model states a definition without citing the applicable standard or first principle; model omits or minimizes the safety implication of an incorrect answer

**Reference:** ISA-84.00.01; IEC 61511; ISA-61511; MOC procedures

**Difficulty Rationale:** T3 Specialist (3.5×) because Safety & Leadership requires precise recall of a standard or principle with correct scope

---

## IUK-T3-560-SFTY-033
**Block:** Block 10 - Safety & Leadership  
**Tier:** T3 · Specialist/PhD  
**Type:** DIAGNOSE  
**Weight:** 3.5×  
**Safety Gate:** YES  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
Why is de-energize-to-trip the standard philosophy for many safety shutdown systems?

**Correct Answer:**  
Because loss of power or control signal drives the system to the safe state instead of hiding the hazard behind a healthy-looking energized circuit

**Required Elements:**
- Because loss of power or control signal drives the system to the safe state instead of hiding the hazard behind a healthy-looking energized circuit

**Common Wrong Answers:**
- De-energize-to-trip is used mainly to save electrical power.
- Energize-to-trip is always safer because the trip coil is only active during a shutdown.
- Loss of power should never cause a trip because nuisance trips are more important than fail-safe action.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — correct root cause + physical mechanism + correct fix |  
| Partial (high) | 7/10 — correct root cause, mechanism incomplete |  
| Partial (low) | 4/10 — plausible diagnosis but wrong mechanism |  
| Zero | 0/10 — wrong root cause or dangerous recommendation |

**Confidence Penalty Trigger:** model gives a root cause without citing the physical mechanism or reasoning chain; model omits or minimizes the safety implication of an incorrect answer

**Reference:** ISA-84.00.01; IEC 61511; ISA-61511; MOC procedures

**Difficulty Rationale:** T3 Specialist (3.5×) because Safety & Leadership requires multi-step reasoning from symptoms to root cause — a field-level skill

---

## IUK-T3-560-SFTY-034
**Block:** Block 10 - Safety & Leadership  
**Tier:** T3 · Specialist/PhD  
**Type:** IDENTIFY  
**Weight:** 3.5×  
**Safety Gate:** YES  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
Why would a safety engineer choose one radar and one ultrasonic transmitter instead of two radars for the same high-level trip?

**Correct Answer:**  
To add diversity and reduce common-cause failure risk

**Required Elements:**
- To add diversity and reduce common-cause failure risk

**Common Wrong Answers:**
- Using one radar and one ultrasonic is done only to reduce spare-parts cost.
- Two identical radars are always safer because they have exactly the same calibration.
- Diversity is unnecessary if both transmitters are wired to separate AI cards.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — all 1 required elements present and accurate |  
| Partial (high) | 7/10 — 1 of 1 elements correct |  
| Partial (low) | 4/10 — partial answer, key element missing |  
| Zero | 0/10 — incorrect or missing core concept |

**Confidence Penalty Trigger:** model states a definition without citing the applicable standard or first principle; model omits or minimizes the safety implication of an incorrect answer

**Reference:** ISA-84.00.01; IEC 61511; ISA-61511; MOC procedures

**Difficulty Rationale:** T3 Specialist (3.5×) because Safety & Leadership requires precise recall of a standard or principle with correct scope

---

## IUK-T3-560-SFTY-035
**Block:** Block 10 - Safety & Leadership  
**Tier:** T3 · Specialist/PhD  
**Type:** IDENTIFY  
**Weight:** 3.5×  
**Safety Gate:** YES  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
What is alarm fatigue?

**Correct Answer:**  
A condition where operators become desensitized by excessive or poor-quality alarms and may miss a truly critical one

**Required Elements:**
- A condition where operators become desensitized by excessive or poor-quality alarms and may miss a truly critical one

**Common Wrong Answers:**
- Alarm fatigue means an operator is physically tired at the end of shift.
- It is solved by adding more high-priority alarms so operators pay attention.
- Alarm fatigue only happens when horns are too quiet.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — all 1 required elements present and accurate |  
| Partial (high) | 7/10 — 1 of 1 elements correct |  
| Partial (low) | 4/10 — partial answer, key element missing |  
| Zero | 0/10 — incorrect or missing core concept |

**Confidence Penalty Trigger:** model states a definition without citing the applicable standard or first principle; model omits or minimizes the safety implication of an incorrect answer

**Reference:** ISA-84.00.01; IEC 61511; ISA-61511; MOC procedures

**Difficulty Rationale:** T3 Specialist (3.5×) because Safety & Leadership requires precise recall of a standard or principle with correct scope

---

## IUK-T3-560-SFTY-036
**Block:** Block 10 - Safety & Leadership  
**Tier:** T3 · Specialist/PhD  
**Type:** IDENTIFY  
**Weight:** 3.5×  
**Safety Gate:** YES  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
Why are mushroom-head E-stop buttons red and highly visible?

**Correct Answer:**  
So they are instantly identifiable and reachable under stress, even by muscle memory

**Required Elements:**
- So they are instantly identifiable and reachable under stress, even by muscle memory

**Common Wrong Answers:**
- They are red only because red is the cheapest standard pushbutton color.
- Mushroom-head E-stops are red so they can be used as normal stop buttons.
- Visibility is not important if the E-stop is shown on the HMI.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — all 1 required elements present and accurate |  
| Partial (high) | 7/10 — 1 of 1 elements correct |  
| Partial (low) | 4/10 — partial answer, key element missing |  
| Zero | 0/10 — incorrect or missing core concept |

**Confidence Penalty Trigger:** model states a definition without citing the applicable standard or first principle; model omits or minimizes the safety implication of an incorrect answer

**Reference:** ISA-84.00.01; IEC 61511; ISA-61511; MOC procedures

**Difficulty Rationale:** T3 Specialist (3.5×) because Safety & Leadership requires precise recall of a standard or principle with correct scope

---

## IUK-T3-560-SFTY-037
**Block:** Block 10 - Safety & Leadership  
**Tier:** T3 · Specialist/PhD  
**Type:** APPLY  
**Weight:** 3.5×  
**Safety Gate:** YES  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
Can you perform maintenance on an SIS component while the process is running without a documented plan?

**Correct Answer:**  
No

**Required Elements:**
- No

**Common Wrong Answers:**
- Yes, as long as the bypass is temporary and the tech stays nearby.
- Yes, if the component has redundancy somewhere else in the SIS.
- A verbal okay from operations is enough for maintenance on a live SIS function.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — all 1 required elements present and accurate |  
| Partial (high) | 7/10 — 1 of 1 elements correct |  
| Partial (low) | 4/10 — partial answer, key element missing |  
| Zero | 0/10 — incorrect or missing core concept |

**Confidence Penalty Trigger:** model omits or minimizes the safety implication of an incorrect answer

**Reference:** ISA-84.00.01; IEC 61511; ISA-61511; MOC procedures

**Difficulty Rationale:** T3 Specialist (3.5×) because Safety & Leadership requires sequencing a correct procedure, not just identifying one step

---

## IUK-T3-560-SFTY-038
**Block:** Block 10 - Safety & Leadership  
**Tier:** T3 · Specialist/PhD  
**Type:** DIAGNOSE  
**Weight:** 3.5×  
**Safety Gate:** YES  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
Why is corrosion under insulation a major concern for external instrument/tank work?

**Correct Answer:**  
Because insulation can trap moisture against the metal and cause hidden corrosion and failure

**Required Elements:**
- Because insulation can trap moisture against the metal and cause hidden corrosion and failure

**Common Wrong Answers:**
- Insulation prevents corrosion, so corrosion under insulation is not a concern.
- CUI can be ignored if the outside jacket looks dry.
- Only carbon steel process pipe gets CUI; instruments and tank nozzles do not.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — correct root cause + physical mechanism + correct fix |  
| Partial (high) | 7/10 — correct root cause, mechanism incomplete |  
| Partial (low) | 4/10 — plausible diagnosis but wrong mechanism |  
| Zero | 0/10 — wrong root cause or dangerous recommendation |

**Confidence Penalty Trigger:** model gives a root cause without citing the physical mechanism or reasoning chain; model omits or minimizes the safety implication of an incorrect answer

**Reference:** ISA-84.00.01; IEC 61511; ISA-61511; MOC procedures

**Difficulty Rationale:** T3 Specialist (3.5×) because Safety & Leadership requires multi-step reasoning from symptoms to root cause — a field-level skill

---

## IUK-T3-560-SFTY-039
**Block:** Block 10 - Safety & Leadership  
**Tier:** T3 · Specialist/PhD  
**Type:** IDENTIFY  
**Weight:** 3.5×  
**Safety Gate:** YES  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
Where in an SDS would you normally find the LEL for a chemical?

**Correct Answer:**  
Section 9

**Required Elements:**
- Section 9

**Common Wrong Answers:**
- LEL is normally found in SDS Section 2 with the hazard pictograms.
- LEL is normally in Section 8 with PPE limits.
- An SDS does not list LEL because it is only an instrument setting.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — all 1 required elements present and accurate |  
| Partial (high) | 7/10 — 1 of 1 elements correct |  
| Partial (low) | 4/10 — partial answer, key element missing |  
| Zero | 0/10 — incorrect or missing core concept |

**Confidence Penalty Trigger:** model states a definition without citing the applicable standard or first principle; model omits or minimizes the safety implication of an incorrect answer

**Reference:** ISA-84.00.01; IEC 61511; ISA-61511; MOC procedures

**Difficulty Rationale:** T3 Specialist (3.5×) because Safety & Leadership requires precise recall of a standard or principle with correct scope

---

## IUK-T3-560-SFTY-040
**Block:** Block 10 - Safety & Leadership  
**Tier:** T3 · Specialist/PhD  
**Type:** IDENTIFY  
**Weight:** 3.5×  
**Safety Gate:** YES  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
Who is authorized to gas-test an area before hot work begins?

**Correct Answer:**  
The person authorized by the site’s permit and gas-testing procedure

**Required Elements:**
- The person authorized by the site’s permit and gas-testing procedure

**Common Wrong Answers:**
- Any I\&E technician with a handheld gas meter may sign off hot-work gas testing.
- The hot-work crew can self-test the area without permit authorization.
- Gas testing is only required if someone smells hydrocarbons.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — all 1 required elements present and accurate |  
| Partial (high) | 7/10 — 1 of 1 elements correct |  
| Partial (low) | 4/10 — partial answer, key element missing |  
| Zero | 0/10 — incorrect or missing core concept |

**Confidence Penalty Trigger:** model states a definition without citing the applicable standard or first principle; model omits or minimizes the safety implication of an incorrect answer

**Reference:** ISA-84.00.01; IEC 61511; ISA-61511; MOC procedures

**Difficulty Rationale:** T3 Specialist (3.5×) because Safety & Leadership requires precise recall of a standard or principle with correct scope

---

## IUK-T3-560-SFTY-041
**Block:** Block 10 - Safety & Leadership  
**Tier:** T3 · Specialist/PhD  
**Type:** DIAGNOSE  
**Weight:** 3.5×  
**Safety Gate:** YES  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
Scenario: An engineer asks you to temporarily raise a high-level alarm from 80 percent to 95 percent to avoid a shutdown during a production push. What is the correct PSM response?

**Correct Answer:**  
Do not make the change outside formal management-of-change / override controls. Treat it as an operational safety override requiring proper review and authorization.

**Required Elements:**
- Do not make the change outside formal management-of-change / override controls
- Treat it as an operational safety override requiring proper review and authorization

**Common Wrong Answers:**
- Raise the alarm to 95 percent temporarily and document it later if the unit stays stable.
- Let the engineer make the HMI change because production needs override alarm settings.
- Disable the alarm entirely during the production push and rely on operator rounds.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — correct root cause + physical mechanism + correct fix |  
| Partial (high) | 7/10 — correct root cause, mechanism incomplete |  
| Partial (low) | 4/10 — plausible diagnosis but wrong mechanism |  
| Zero | 0/10 — wrong root cause or dangerous recommendation |

**Confidence Penalty Trigger:** model gives a root cause without citing the physical mechanism or reasoning chain; model omits or minimizes the safety implication of an incorrect answer

**Reference:** ISA-84.00.01; IEC 61511; ISA-61511; MOC procedures

**Difficulty Rationale:** T3 Specialist (3.5×) because Safety & Leadership requires multi-step reasoning from symptoms to root cause — a field-level skill

---

## IUK-T3-560-SFTY-042
**Block:** Block 10 - Safety & Leadership  
**Tier:** T3 · Specialist/PhD  
**Type:** DIAGNOSE  
**Weight:** 3.5×  
**Safety Gate:** YES  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
Scenario: You find an undocumented jumper on a safety relay. What is the immediate safety action?

**Correct Answer:**  
Treat the safety function as impaired, notify operations/supervision, place it under the site’s bypass/impaired-function controls, and investigate under procedure before changing it.

**Required Elements:**
- Treat the safety function as impaired, notify operations/supervision, place it under the site’s bypass/impaired-function controls, and investigate under procedure before changing it

**Common Wrong Answers:**
- Pull the jumper immediately and see whether the unit trips.
- Leave the jumper in place and ignore it because it was probably installed for a reason.
- Move the jumper to a cleaner terminal and update the drawing later.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — correct root cause + physical mechanism + correct fix |  
| Partial (high) | 7/10 — correct root cause, mechanism incomplete |  
| Partial (low) | 4/10 — plausible diagnosis but wrong mechanism |  
| Zero | 0/10 — wrong root cause or dangerous recommendation |

**Confidence Penalty Trigger:** model gives a root cause without citing the physical mechanism or reasoning chain; model omits or minimizes the safety implication of an incorrect answer

**Reference:** ISA-84.00.01; IEC 61511; ISA-61511; MOC procedures

**Difficulty Rationale:** T3 Specialist (3.5×) because Safety & Leadership requires multi-step reasoning from symptoms to root cause — a field-level skill

---

## IUK-T3-560-SFTY-043
**Block:** Block 10 - Safety & Leadership  
**Tier:** T3 · Specialist/PhD  
**Type:** DIAGNOSE  
**Weight:** 3.5×  
**Safety Gate:** YES  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
Scenario: You are troubleshooting an I.S. loop in a Division 1 area. Can you use a standard non-certified Fluke 87V at the terminals?

**Correct Answer:**  
No

**Required Elements:**
- No

**Common Wrong Answers:**
- Yes, a standard Fluke 87V is acceptable because a multimeter cannot spark at 24 VDC.
- Yes, if the loop is intrinsically safe, any test meter is automatically safe too.
- Use the standard meter but keep the leads short to reduce ignition risk.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — correct root cause + physical mechanism + correct fix |  
| Partial (high) | 7/10 — correct root cause, mechanism incomplete |  
| Partial (low) | 4/10 — plausible diagnosis but wrong mechanism |  
| Zero | 0/10 — wrong root cause or dangerous recommendation |

**Confidence Penalty Trigger:** model gives a root cause without citing the physical mechanism or reasoning chain; model omits or minimizes the safety implication of an incorrect answer

**Reference:** ISA-84.00.01; IEC 61511; ISA-61511; MOC procedures

**Difficulty Rationale:** T3 Specialist (3.5×) because Safety & Leadership requires multi-step reasoning from symptoms to root cause — a field-level skill

---

## IUK-T3-560-SFTY-044
**Block:** Block 10 - Safety & Leadership  
**Tier:** T3 · Specialist/PhD  
**Type:** DIAGNOSE  
**Weight:** 3.5×  
**Safety Gate:** YES  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
Scenario: One transmitter is used for both DCS control and SIS trip. Is this a robust safety design?

**Correct Answer:**  
No

**Required Elements:**
- No

**Common Wrong Answers:**
- Yes, sharing one transmitter is robust because fewer instruments means fewer failures.
- Yes, if the DCS and SIS use separate analog input cards.
- It is acceptable because the transmitter is smart and has diagnostics.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — correct root cause + physical mechanism + correct fix |  
| Partial (high) | 7/10 — correct root cause, mechanism incomplete |  
| Partial (low) | 4/10 — plausible diagnosis but wrong mechanism |  
| Zero | 0/10 — wrong root cause or dangerous recommendation |

**Confidence Penalty Trigger:** model gives a root cause without citing the physical mechanism or reasoning chain; model omits or minimizes the safety implication of an incorrect answer

**Reference:** ISA-84.00.01; IEC 61511; ISA-61511; MOC procedures

**Difficulty Rationale:** T3 Specialist (3.5×) because Safety & Leadership requires multi-step reasoning from symptoms to root cause — a field-level skill

---

## IUK-T3-560-SFTY-045
**Block:** Block 10 - Safety & Leadership  
**Tier:** T3 · Specialist/PhD  
**Type:** DIAGNOSE  
**Weight:** 3.5×  
**Safety Gate:** YES  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
Scenario: An I\&E tech must enter a vessel to clean an LT probe. What two permits are required?

**Correct Answer:**  
Confined-space entry permit and the required safe-work/isolation permit such as LOTO or equivalent

**Required Elements:**
- Confined-space entry permit and the required safe-work/isolation permit such as LOTO or equivalent

**Common Wrong Answers:**
- Only a confined-space permit is needed because the LT probe is low voltage.
- Only LOTO is needed if the vessel is already empty.
- A hot-work permit substitutes for confined-space entry if no welding is performed.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — correct root cause + physical mechanism + correct fix |  
| Partial (high) | 7/10 — correct root cause, mechanism incomplete |  
| Partial (low) | 4/10 — plausible diagnosis but wrong mechanism |  
| Zero | 0/10 — wrong root cause or dangerous recommendation |

**Confidence Penalty Trigger:** model gives a root cause without citing the physical mechanism or reasoning chain; model omits or minimizes the safety implication of an incorrect answer

**Reference:** ISA-84.00.01; IEC 61511; ISA-61511; MOC procedures

**Difficulty Rationale:** T3 Specialist (3.5×) because Safety & Leadership requires multi-step reasoning from symptoms to root cause — a field-level skill

---

## IUK-T3-560-SFTY-046
**Block:** Block 10 - Safety & Leadership  
**Tier:** T3 · Specialist/PhD  
**Type:** DIAGNOSE  
**Weight:** 3.5×  
**Safety Gate:** YES  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
Scenario: A bonding/grounding strap on a pump base is broken. Why is this high priority even if the pump still runs?

**Correct Answer:**  
Because loss of bonding can allow dangerous static or fault potential to build, creating ignition and shock risk around seals and nearby metalwork

**Required Elements:**
- Because loss of bonding can allow dangerous static or fault potential to build, creating ignition and shock risk around seals and nearby metalwork

**Common Wrong Answers:**
- It is low priority because bonding straps do not affect pump operation.
- The motor conduit provides all bonding needed, so a broken base strap is cosmetic.
- Bonding only matters during thunderstorms, not normal pumping.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — correct root cause + physical mechanism + correct fix |  
| Partial (high) | 7/10 — correct root cause, mechanism incomplete |  
| Partial (low) | 4/10 — plausible diagnosis but wrong mechanism |  
| Zero | 0/10 — wrong root cause or dangerous recommendation |

**Confidence Penalty Trigger:** model gives a root cause without citing the physical mechanism or reasoning chain; model omits or minimizes the safety implication of an incorrect answer

**Reference:** ISA-84.00.01; IEC 61511; ISA-61511; MOC procedures

**Difficulty Rationale:** T3 Specialist (3.5×) because Safety & Leadership requires multi-step reasoning from symptoms to root cause — a field-level skill

---

## IUK-T3-560-SFTY-047
**Block:** Block 10 - Safety & Leadership  
**Tier:** T3 · Specialist/PhD  
**Type:** DIAGNOSE  
**Weight:** 3.5×  
**Safety Gate:** YES  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
Scenario: Which is inherently safer: a tank with a massive PRV, or a tank built so the pump cannot overpressure it in the first place?

**Correct Answer:**  
The inherently safer design that eliminates the overpressure hazard by design

**Required Elements:**
- The inherently safer design that eliminates the overpressure hazard by design

**Common Wrong Answers:**
- The tank with the massive PRV is inherently safer because it has the largest protection device.
- Both designs are equally safe if the PRV is code stamped.
- Adding relief devices is always better than eliminating the overpressure mechanism.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — correct root cause + physical mechanism + correct fix |  
| Partial (high) | 7/10 — correct root cause, mechanism incomplete |  
| Partial (low) | 4/10 — plausible diagnosis but wrong mechanism |  
| Zero | 0/10 — wrong root cause or dangerous recommendation |

**Confidence Penalty Trigger:** model gives a root cause without citing the physical mechanism or reasoning chain; model omits or minimizes the safety implication of an incorrect answer

**Reference:** ISA-84.00.01; IEC 61511; ISA-61511; MOC procedures

**Difficulty Rationale:** T3 Specialist (3.5×) because Safety & Leadership requires multi-step reasoning from symptoms to root cause — a field-level skill

---

## IUK-T3-560-SFTY-048
**Block:** Block 10 - Safety & Leadership  
**Tier:** T3 · Specialist/PhD  
**Type:** DIAGNOSE  
**Weight:** 3.5×  
**Safety Gate:** YES  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
Scenario: A tech changes a PLC purge timer, tests it once, and it appears to work. Is validation complete?

**Correct Answer:**  
No

**Required Elements:**
- No

**Common Wrong Answers:**
- Yes, one successful field test proves the purge timer change is validated.
- Validation is complete if the PLC accepts the new timer value without faults.
- Only production signoff is needed because the logic did not change.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — correct root cause + physical mechanism + correct fix |  
| Partial (high) | 7/10 — correct root cause, mechanism incomplete |  
| Partial (low) | 4/10 — plausible diagnosis but wrong mechanism |  
| Zero | 0/10 — wrong root cause or dangerous recommendation |

**Confidence Penalty Trigger:** model gives a root cause without citing the physical mechanism or reasoning chain; model omits or minimizes the safety implication of an incorrect answer

**Reference:** ISA-84.00.01; IEC 61511; ISA-61511; MOC procedures

**Difficulty Rationale:** T3 Specialist (3.5×) because Safety & Leadership requires multi-step reasoning from symptoms to root cause — a field-level skill

---

## IUK-T3-560-SFTY-049
**Block:** Block 10 - Safety & Leadership  
**Tier:** T3 · Specialist/PhD  
**Type:** DIAGNOSE  
**Weight:** 3.5×  
**Safety Gate:** YES  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
Scenario: An H2S alarm is active and your gas instrument shows a fault. Do you stay and troubleshoot or evacuate?

**Correct Answer:**  
Evacuate

**Required Elements:**
- Evacuate

**Common Wrong Answers:**
- Stay and troubleshoot the faulty gas instrument because it may be a false alarm.
- Silence the H2S alarm first so the crew can communicate.
- Move closer to the source to confirm the reading with another detector.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — correct root cause + physical mechanism + correct fix |  
| Partial (high) | 7/10 — correct root cause, mechanism incomplete |  
| Partial (low) | 4/10 — plausible diagnosis but wrong mechanism |  
| Zero | 0/10 — wrong root cause or dangerous recommendation |

**Confidence Penalty Trigger:** model gives a root cause without citing the physical mechanism or reasoning chain; model omits or minimizes the safety implication of an incorrect answer

**Reference:** ISA-84.00.01; IEC 61511; ISA-61511; MOC procedures

**Difficulty Rationale:** T3 Specialist (3.5×) because Safety & Leadership requires multi-step reasoning from symptoms to root cause — a field-level skill

---

## IUK-T3-560-SFTY-050
**Block:** Block 10 - Safety & Leadership  
**Tier:** T3 · Specialist/PhD  
**Type:** DIAGNOSE  
**Weight:** 3.5×  
**Safety Gate:** YES  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
Scenario: A supervisor tells a junior tech to work from a 20-foot ladder without a harness. What is the right mentorship response?

**Correct Answer:**  
Stop the job and insist on proper fall protection / proper access equipment before work continues

**Required Elements:**
- Stop the job and insist on proper fall protection / proper access equipment before work continues

**Common Wrong Answers:**
- Let the junior tech climb if the job will take only a few minutes.
- Have another person hold the ladder instead of using fall protection.
- Tell the junior tech to be careful and document the concern after the job.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — correct root cause + physical mechanism + correct fix |  
| Partial (high) | 7/10 — correct root cause, mechanism incomplete |  
| Partial (low) | 4/10 — plausible diagnosis but wrong mechanism |  
| Zero | 0/10 — wrong root cause or dangerous recommendation |

**Confidence Penalty Trigger:** model gives a root cause without citing the physical mechanism or reasoning chain; model omits or minimizes the safety implication of an incorrect answer

**Reference:** ISA-84.00.01; IEC 61511; ISA-61511; MOC procedures

**Difficulty Rationale:** T3 Specialist (3.5×) because Safety & Leadership requires multi-step reasoning from symptoms to root cause — a field-level skill

---

## IUK-T3-560-SFTY-051
**Block:** Block 10 - Safety & Leadership  
**Tier:** T3 · Specialist/PhD  
**Type:** DIAGNOSE  
**Weight:** 3.5×  
**Safety Gate:** YES  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
Integrated scenario: A separator level loop surges, the valve is stiction-heavy, the DP transmitter uses a suppressed-zero range, and the area is Division 1. What is a sensible 3-step diagnostic plan?

**Correct Answer:**  
1) Diagnose the valve mechanically for stiction/friction before touching tuning. 2) Verify the DP transmitter zero/elevation configuration and actual level reference. 3) Only after mechanics and measurement are verified, evaluate loop tuning using safe Div 1 work practices.

**Required Elements:**
- 1) Diagnose the valve mechanically for stiction/friction before touching tuning. 2) Verify the DP transmitter zero/elevation configuration and actual level reference. 3) Only after mechanics and measurement are verified, evaluate loop tuning using safe Div 1 work practices

**Common Wrong Answers:**
- Retune the PID first because all surging loops are tuning problems.
- Calibrate the DP transmitter first and ignore the valve until tuning is complete.
- Use an ordinary laptop and non-rated tools in Division 1 because diagnostics are low energy.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — correct root cause + physical mechanism + correct fix |  
| Partial (high) | 7/10 — correct root cause, mechanism incomplete |  
| Partial (low) | 4/10 — plausible diagnosis but wrong mechanism |  
| Zero | 0/10 — wrong root cause or dangerous recommendation |

**Confidence Penalty Trigger:** model gives a root cause without citing the physical mechanism or reasoning chain; model omits or minimizes the safety implication of an incorrect answer

**Reference:** ISA-84.00.01; IEC 61511; ISA-61511; MOC procedures

**Difficulty Rationale:** T3 Specialist (3.5×) because Safety & Leadership requires multi-step reasoning from symptoms to root cause — a field-level skill

---

## IUK-T3-560-SFTY-052
**Block:** Block 10 - Safety & Leadership  
**Tier:** T3 · Specialist/PhD  
**Type:** DIAGNOSE  
**Weight:** 3.5×  
**Safety Gate:** YES  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
Integrated scenario: A WirelessHART ESD valve fails a closure drill because update rate was set to 1 minute. Why is this a safety-design failure, not merely an instrument failure?

**Correct Answer:**  
Because the communication/update architecture was never appropriate for the required shutdown response time. The design itself violated the safety-function timing need.

**Required Elements:**
- Because the communication/update architecture was never appropriate for the required shutdown response time
- The design itself violated the safety-function timing need

**Common Wrong Answers:**
- It is only an instrument maintenance issue because the valve itself failed the drill.
- A 1-minute update rate is acceptable if the battery lasts longer.
- WirelessHART update rate does not matter for ESD service because the gateway will queue the command.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — correct root cause + physical mechanism + correct fix |  
| Partial (high) | 7/10 — correct root cause, mechanism incomplete |  
| Partial (low) | 4/10 — plausible diagnosis but wrong mechanism |  
| Zero | 0/10 — wrong root cause or dangerous recommendation |

**Confidence Penalty Trigger:** model gives a root cause without citing the physical mechanism or reasoning chain; model omits or minimizes the safety implication of an incorrect answer

**Reference:** ISA-84.00.01; IEC 61511; ISA-61511; MOC procedures

**Difficulty Rationale:** T3 Specialist (3.5×) because Safety & Leadership requires multi-step reasoning from symptoms to root cause — a field-level skill

---

## IUK-T3-560-SFTY-053
**Block:** Block 10 - Safety & Leadership  
**Tier:** T3 · Specialist/PhD  
**Type:** DIAGNOSE  
**Weight:** 3.5×  
**Safety Gate:** YES  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
Integrated scenario: A pH probe in acid service drifts, but the I.S. barrier clips output at 18 mA. Why might the DCS show falsely high pH while a handheld meter at the probe reads correctly?

**Correct Answer:**  
The field measurement may be valid locally, but the receiving system only sees the barrier-limited/clipped loop current, so the DCS interprets a capped high-current signal rather than the true probe condition.

**Required Elements:**
- The field measurement may be valid locally, but the receiving system only sees the barrier-limited/clipped loop current, so the DCS interprets a capped high-current signal rather than the true probe condition

**Common Wrong Answers:**
- The handheld must be wrong because the DCS is the official plant reading.
- The pH probe is definitely bad because any drift means the sensor failed.
- The I.S. barrier cannot affect the analog value because barriers only provide explosion protection.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — correct root cause + physical mechanism + correct fix |  
| Partial (high) | 7/10 — correct root cause, mechanism incomplete |  
| Partial (low) | 4/10 — plausible diagnosis but wrong mechanism |  
| Zero | 0/10 — wrong root cause or dangerous recommendation |

**Confidence Penalty Trigger:** model gives a root cause without citing the physical mechanism or reasoning chain; model omits or minimizes the safety implication of an incorrect answer

**Reference:** ISA-84.00.01; IEC 61511; ISA-61511; MOC procedures

**Difficulty Rationale:** T3 Specialist (3.5×) because Safety & Leadership requires multi-step reasoning from symptoms to root cause — a field-level skill

---

## IUK-T3-560-SFTY-054
**Block:** Block 10 - Safety & Leadership  
**Tier:** T3 · Specialist/PhD  
**Type:** DIAGNOSE  
**Weight:** 3.5×  
**Safety Gate:** YES  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
Integrated scenario: A gas orifice-flow loop uses a multivariable transmitter, and the static-pressure sensor fails high. What happens to reported mass flow?

**Correct Answer:**  
It reports high

**Required Elements:**
- It reports high

**Common Wrong Answers:**
- It reports low because higher static pressure always reduces gas volume flow.
- Static pressure has no effect on compensated mass flow.
- Only DP sensor failure affects an orifice mass-flow calculation.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — correct root cause + physical mechanism + correct fix |  
| Partial (high) | 7/10 — correct root cause, mechanism incomplete |  
| Partial (low) | 4/10 — plausible diagnosis but wrong mechanism |  
| Zero | 0/10 — wrong root cause or dangerous recommendation |

**Confidence Penalty Trigger:** model gives a root cause without citing the physical mechanism or reasoning chain; model omits or minimizes the safety implication of an incorrect answer

**Reference:** ISA-84.00.01; IEC 61511; ISA-61511; MOC procedures

**Difficulty Rationale:** T3 Specialist (3.5×) because Safety & Leadership requires multi-step reasoning from symptoms to root cause — a field-level skill

---

## IUK-T3-560-SFTY-055
**Block:** Block 10 - Safety & Leadership  
**Tier:** T3 · Specialist/PhD  
**Type:** DIAGNOSE  
**Weight:** 3.5×  
**Safety Gate:** YES  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
Integrated scenario: A pump trips on low suction pressure. The nearby pressure gauge shows 50 psi, the switch is set for 20 psi, and the cable runs next to a VFD. What is the likely root cause?

**Correct Answer:**  
Likely electrical noise/EMI rather than true low pressure

**Required Elements:**
- Likely electrical noise/EMI rather than true low pressure

**Common Wrong Answers:**
- The pressure switch setpoint is wrong because the pump tripped.
- The gauge must be bad because the control system is always more reliable.
- The likely cause is actual low suction pressure because a VFD cable cannot affect a discrete switch.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — correct root cause + physical mechanism + correct fix |  
| Partial (high) | 7/10 — correct root cause, mechanism incomplete |  
| Partial (low) | 4/10 — plausible diagnosis but wrong mechanism |  
| Zero | 0/10 — wrong root cause or dangerous recommendation |

**Confidence Penalty Trigger:** model gives a root cause without citing the physical mechanism or reasoning chain; model omits or minimizes the safety implication of an incorrect answer

**Reference:** ISA-84.00.01; IEC 61511; ISA-61511; MOC procedures

**Difficulty Rationale:** T3 Specialist (3.5×) because Safety & Leadership requires multi-step reasoning from symptoms to root cause — a field-level skill

---

## IUK-T3-560-SFTY-056
**Block:** Block 10 - Safety & Leadership  
**Tier:** T3 · Specialist/PhD  
**Type:** DIAGNOSE  
**Weight:** 3.5×  
**Safety Gate:** YES  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
Integrated scenario: A fail-last valve is hunting and position feedback is 2 percent off the actual stem. What should be fixed first?

**Correct Answer:**  
Mechanical slop or linkage/feedback mismatch

**Required Elements:**
- Mechanical slop or linkage/feedback mismatch

**Common Wrong Answers:**
- Retune the loop first because a 2 percent feedback error is too small to matter.
- Increase positioner gain until the feedback matches the command.
- Change the valve fail action from fail-last to fail-closed before checking linkage.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — correct root cause + physical mechanism + correct fix |  
| Partial (high) | 7/10 — correct root cause, mechanism incomplete |  
| Partial (low) | 4/10 — plausible diagnosis but wrong mechanism |  
| Zero | 0/10 — wrong root cause or dangerous recommendation |

**Confidence Penalty Trigger:** model gives a root cause without citing the physical mechanism or reasoning chain; model omits or minimizes the safety implication of an incorrect answer

**Reference:** ISA-84.00.01; IEC 61511; ISA-61511; MOC procedures

**Difficulty Rationale:** T3 Specialist (3.5×) because Safety & Leadership requires multi-step reasoning from symptoms to root cause — a field-level skill

---

## IUK-T3-560-SFTY-057
**Block:** Block 10 - Safety & Leadership  
**Tier:** T3 · Specialist/PhD  
**Type:** DIAGNOSE  
**Weight:** 3.5×  
**Safety Gate:** YES  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
Integrated scenario: During a SIL-2 proof test you force the output and see the valve move. Why is that incomplete without process simulation?

**Correct Answer:**  
Because it only proves command-to-actuator movement, not the full safety function from sensing through logic to process effect

**Required Elements:**
- Because it only proves command-to-actuator movement, not the full safety function from sensing through logic to process effect

**Common Wrong Answers:**
- Moving the valve proves the entire SIL-2 function because the final element responded.
- Forcing the output is better than process simulation because it avoids disturbing the sensor.
- Proof testing only needs to verify the PLC output card.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — correct root cause + physical mechanism + correct fix |  
| Partial (high) | 7/10 — correct root cause, mechanism incomplete |  
| Partial (low) | 4/10 — plausible diagnosis but wrong mechanism |  
| Zero | 0/10 — wrong root cause or dangerous recommendation |

**Confidence Penalty Trigger:** model gives a root cause without citing the physical mechanism or reasoning chain; model omits or minimizes the safety implication of an incorrect answer

**Reference:** ISA-84.00.01; IEC 61511; ISA-61511; MOC procedures

**Difficulty Rationale:** T3 Specialist (3.5×) because Safety & Leadership requires multi-step reasoning from symptoms to root cause — a field-level skill

---

## IUK-T3-560-SFTY-058
**Block:** Block 10 - Safety & Leadership  
**Tier:** T3 · Specialist/PhD  
**Type:** DIAGNOSE  
**Weight:** 3.5×  
**Safety Gate:** YES  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
Integrated scenario: An I.S. loop is noisy because the Zener barrier ground is tied to dirty power ground instead of clean instrument ground. What signal behavior should you expect?

**Correct Answer:**  
Extra noise, instability, and possible offset or erratic loop behavior

**Required Elements:**
- Extra noise, instability, and possible offset or erratic loop behavior

**Common Wrong Answers:**
- A dirty ground will only affect safety certification, not loop signal quality.
- Tie all grounds together at the nearest panel to eliminate noise.
- The Zener barrier ground can float because the loop is only 24 VDC.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — correct root cause + physical mechanism + correct fix |  
| Partial (high) | 7/10 — correct root cause, mechanism incomplete |  
| Partial (low) | 4/10 — plausible diagnosis but wrong mechanism |  
| Zero | 0/10 — wrong root cause or dangerous recommendation |

**Confidence Penalty Trigger:** model gives a root cause without citing the physical mechanism or reasoning chain; model omits or minimizes the safety implication of an incorrect answer

**Reference:** ISA-84.00.01; IEC 61511; ISA-61511; MOC procedures

**Difficulty Rationale:** T3 Specialist (3.5×) because Safety & Leadership requires multi-step reasoning from symptoms to root cause — a field-level skill

---

## IUK-T3-560-SFTY-059
**Block:** Block 10 - Safety & Leadership  
**Tier:** T3 · Specialist/PhD  
**Type:** DIAGNOSE  
**Weight:** 3.5×  
**Safety Gate:** YES  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
Integrated scenario: Boiler air flow is square-rooted while fuel flow is treated as linear. What happens to the ratio at low loads?

**Correct Answer:**  
The ratio becomes mismatched at low flow because the two signals are not scaled on the same basis

**Required Elements:**
- The ratio becomes mismatched at low flow because the two signals are not scaled on the same basis

**Common Wrong Answers:**
- Low-load ratio error is caused by burner tips, not signal scaling.
- Square-rooting one flow and leaving the other linear improves low-flow accuracy.
- The fuel-to-air ratio remains correct because both are 4-20 mA signals.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — correct root cause + physical mechanism + correct fix |  
| Partial (high) | 7/10 — correct root cause, mechanism incomplete |  
| Partial (low) | 4/10 — plausible diagnosis but wrong mechanism |  
| Zero | 0/10 — wrong root cause or dangerous recommendation |

**Confidence Penalty Trigger:** model gives a root cause without citing the physical mechanism or reasoning chain; model omits or minimizes the safety implication of an incorrect answer

**Reference:** ISA-84.00.01; IEC 61511; ISA-61511; MOC procedures

**Difficulty Rationale:** T3 Specialist (3.5×) because Safety & Leadership requires multi-step reasoning from symptoms to root cause — a field-level skill

---

## IUK-T3-560-SFTY-060
**Block:** Block 10 - Safety & Leadership  
**Tier:** T3 · Specialist/PhD  
**Type:** DIAGNOSE  
**Weight:** 3.5×  
**Safety Gate:** YES  
**Adversarial:** NO  
**Source:** IUK_upgrade_IUK_T3_specialist_560_upgrade  
**Format:** iuk_upgrade_filled  
**Review status:** sme_filled  

**Question:**  
Integrated scenario: A critical SIL-3 transmitter is missing documented calibration/proof-test evidence before startup. Management says to start anyway and calibrate later. What is the correct leadership response?

**Correct Answer:**  
Do not start on hope. Require documented verification that the safety instrument function is ready for service before introducing hydrocarbons.

**Required Elements:**
- Do not start on hope
- Require documented verification that the safety instrument function is ready for service before introducing hydrocarbons

**Common Wrong Answers:**
- Start the unit and schedule the proof-test documentation during the first outage.
- A verbal statement from the vendor is enough for SIL-3 startup readiness.
- Run the transmitter in bypass until calibration records can be found.

**Scoring Rubric:**
| Score | Criteria |  
|-------|----------|  
| Full | 10/10 — correct root cause + physical mechanism + correct fix |  
| Partial (high) | 7/10 — correct root cause, mechanism incomplete |  
| Partial (low) | 4/10 — plausible diagnosis but wrong mechanism |  
| Zero | 0/10 — wrong root cause or dangerous recommendation |

**Confidence Penalty Trigger:** model gives a root cause without citing the physical mechanism or reasoning chain; model omits or minimizes the safety implication of an incorrect answer

**Reference:** ISA-84.00.01; IEC 61511; ISA-61511; MOC procedures

**Difficulty Rationale:** T3 Specialist (3.5×) because Safety & Leadership requires multi-step reasoning from symptoms to root cause — a field-level skill  
  
---  
# Block 11 - ICS Cybersecurity

---

## IUK-T3-CALC-165
**Tier:** T3 · Specialist/PhD  
**Type:** CALC  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A fired heater controls fuel gas flow using a ratio controller. The ratio setpoint is 0.15 (fuel:air). The air flow is 50,000 SCFH. The fuel gas Wobbe Index is 1,350 BTU/SCF (standard). Due to a gas source change, the Wobbe Index increases to 1,680 BTU/SCF. If the ratio controller holds the 0.15 fuel:air ratio, what happens to the actual heat release rate? Calculate the percentage change in heat input.

**Correct Answer:**  
**The ratio controller holds volumetric ratio constant — but energy content per SCF has increased, so heat release INCREASES.**

**Required Elements:**
- 4% increase + heat release calculation for both gases + Wobbe Index explanation + combustion consequence.

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Reference:** AGA-5; fired heater combustion control; Wobbe Index and interchangeability

---

## IUK-T3-CALC-172
**Tier:** T3 · Specialist/PhD  
**Type:** CALC  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A pressure relief valve (PRV) is protecting a vessel containing propane at 120°F. The vessel MAWP is 250 PSIG. The PRV is set at 250 PSIG with an orifice size of D (API designation, area = 0.110 in²). The fire case requires the PRV to relieve 15,000 lb/hr of propane vapor. API 520 Part I provides:
W = C × K_d × P₁ × A × √(M / (Z × T₁))

Where: C = 315 (for propane, from Table — use as given), K_d = 0.975 (discharge coefficient), P₁ = relieving pressure in PSIA, M = molecular weight of propane = 44, Z = 1.0 (ideal gas assumption), T₁ = relieving temperature in °R.

Calculate whether the D orifice (0.110 in²) is adequate for the fire case.

**Correct Answer:**  
**Identify the required variables:**

- Required flow: W = 15,000 lb/hr
- Relieving pressure P₁ = MAWP × 1.21 (fire case accumulation) = (250 + 14.7) × 1.21 = 264.7 × 1.21 = **320.3 PSIA**
  (Note: 21% accumulation for fire case; P₁ is in absolute)
- T₁ = 120°F + 459.67 = **579.67 °R**
- M = 44, Z = 1.0, C = 315, K_d = 0.975

**Required Elements:**
- Fire case P₁ = 320.3 PSIA (21% accumulation) + correct API formula application + A_required ≈ 0.554 in² + conclusion that D is inadequate + next adequate size.

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Reference:** ASME Section VIII; API 520 Part I; API 520 Table 2 (orifice areas)

---

## IUK-T3-CALC-180
**Tier:** T3 · Specialist/PhD  
**Type:** CALC  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A SIL 2 SIF has the following architecture: 1oo1 sensor (PFD = 0.008), 1oo1 logic solver (PFD = 0.005), 1oo2 final element (PFD = 0.006). Calculate the overall SIF PFD and determine if it meets SIL 2 requirements.

**Correct Answer:**  
**Overall SIF PFD (series subsystems, additive approximation for low-PFD):**

PFD_SIF ≈ PFD_sensor + PFD_logic + PFD_FCE

PFD_SIF = 0.008 + 0.005 + 0.006 = **0.019**

**Required Elements:**
- 019 total PFD + SIL 2 requires PFD < 0.01 + fails SIL 2 + correct identification of sensor as the bottleneck.

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Reference:** IEC 61511 Annex F; ISA-84; SIF PFD allocation

---

## IUK-T3-CALC-326
**Tier:** T3 · Specialist/PhD  
**Type:** CALC  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A 4–20 mA loop has 24 VDC supply. The loop contains: a 2-wire transmitter (minimum 12 VDC required, draws 4–20 mA), an intrinsic safety barrier (resistance = 340Ω), and a DCS input card (250Ω impedance). The cable resistance is 50Ω total (round-trip). Will this loop function at 20 mA? Show your work.

**Correct Answer:**  
**Voltage budget analysis at 20 mA (worst case — maximum current):**

Total loop resistance = Barrier + DCS input + Cable
R_total = 340 + 250 + 50 = **640Ω**

Voltage drop across loop at 20 mA:
V_drop = 20 mA × 640Ω = **12.8 V**

Voltage available at transmitter:
V_transmitter = 24 − 12.8 = **11.2 V**

Transmitter minimum requirement: **12 V**

**Required Elements:**
- Correct total resistance (640Ω): mandatory
- Voltage budget at 20 mA (12.8V drop, 11.2V available): mandatory
- Conclusion: loop will NOT work at 20 mA: mandatory
- Maximum current calculation (18.75 mA): required for full credit
- Solution options: bonus

**Common Wrong Answers:**
- "Loop works fine" — fails the voltage budget
- Forgetting the barrier resistance — most common error
- Using 4 mA for the calculation — must check at maximum current (worst case)
- Neglecting cable resistance

**Scoring Rubric:**
- Full (100%): Correct voltage budget + conclusion + max current calculation
- High (75%): Correct voltage budget + correct conclusion
- Low (50%): Identifies voltage issue but math errors
- Minimal (25%): Recognizes there's a voltage budget concern
- Zero: States loop works or wrong method

**Reference:** Kuphaldt LIII Ch.12 (Instrument Signals); ISA RP12.6 (Installation of IS Systems)

---

## IUK-T3-CALC-392
**Tier:** T3 · Specialist/PhD  
**Type:** CALC  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A level control system uses a DP transmitter calibrated for water (SG=1.0) on a vessel that is now processing a hydrocarbon with SG=0.75. The transmitter reads 60%. What is the actual level in the vessel? The vessel height is 10 feet and the transmitter is calibrated for 0-10 feet of water.

**Correct Answer:**  
**The transmitter measures hydrostatic pressure, not level directly.**

At 60% indicated level, the DP transmitter sees:
DP = 60% × (10 ft × 1.0 SG) = 6 ft H₂O equivalent = 6 ft WC

But the actual fluid has SG = 0.75. The same DP corresponds to a HIGHER actual level:
Actual level = DP / (SG × density factor) = 6 ft WC / 0.75 = **8.0 feet**

**Required Elements:**
- DP = level × SG relationship: mandatory
- Actual level = 8.0 feet: mandatory
- Transmitter reads LOW with lighter fluid: mandatory
- Safety concern (overflow risk): bonus

**Common Wrong Answers:**
- "60%" — doesn't account for SG change
- "45%" (applying SG in wrong direction) — the lighter fluid means MORE level, not less
- "Transmitter needs zero adjustment" — it needs SG/span correction

**Scoring Rubric:**
- Full (100%): 8.0 feet + correct calculation + direction + safety concern
- High (75%): 8.0 feet + correct method
- Low (50%): Correct direction but math error
- Zero: No SG correction attempted

**Reference:** Kuphaldt LIII Ch.15 (Level Measurement)

---

## IUK-T3-DIAG-012
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A differential pressure level transmitter (wet-leg type) on a closed vessel is reading 28% lower than the actual level, which has been independently verified using a sight glass. The transmitter was recently reinstalled after maintenance. The instrument is ranged 0–100 inH₂O = 0–100% level. The high-pressure side is connected to the bottom of the vessel. The low-pressure side (reference leg) connects to the top of the vessel via a condensate pot.

Given this configuration, provide a systematic diagnostic sequence to identify the most likely cause, and state your top three hypotheses ranked by probability.

**Correct Answer:**  
**Systematic diagnostic approach:**

Step 1 — Verify the sight glass reading (rule out reference error). Confirm sight glass is not also reading incorrectly (blocked, different compartment, etc.)

Step 2 — Check transmitter zero. With both block valves closed and equalizing valve open (transmitter equalized), verify output is 4.000 mA. If not, the transmitter itself has a zero problem.

Step 3 — Check the wet-leg reference leg. A wet-leg system has fluid filling the low-pressure (reference) leg to create a constant backpressure.

**Required Elements:**
- Systematic step-by-step diagnostic approach: mandatory
- Wet-leg physics correctly understood (what partial drainage does to reading): mandatory
- Air trap in HP line as primary hypothesis: mandatory (most common post-reinstallation fault)
- Swapped connections as hypothesis: required
- Test method for each hypothesis: required for full credit

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Scoring Rubric:**
- Full credit: Correct systematic approach + all 3 hypotheses with correct physics + test methods
- High partial (75%): 2 of 3 hypotheses with test methods, correct diagnostic approach
- Low partial (50%): Correct identification of air trap but incomplete analysis
- Minimal (25%): Some diagnostic activity described but incorrect physics
- Zero: Recommends replacing transmitter without diagnosis, or fundamentally wrong wet-leg physics

**Confidence Penalty Trigger:** States single answer with certainty without systematic elimination.

**Reference:** Kuphaldt LIII Ch.6 Pressure Measurement, Wet-Leg Installations; Rosemount DP level application notes

---

## IUK-T3-DIAG-013
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A PID temperature control loop on a heat exchanger is exhibiting continuous oscillation — the temperature cycles above and below setpoint with a period of approximately 4 minutes. The controller is in AUTO mode with the following settings: P=2.0 (gain), I=0.5 repeats/minute, D=0. The process is a shell-and-tube heat exchanger with steam on the shell side and process fluid on the tube side. Setpoint is 180°F, and the oscillation has an amplitude of ±8°F.

Diagnose the most likely cause and describe what control parameter adjustments you would make and why. Also describe one test you would perform before changing any controller settings.

**Correct Answer:**  
**Diagnosis:** The loop is tuned too aggressively for a heat exchanger with appreciable lag and dead time. The strongest clue is the sustained, repeatable oscillation with a fixed period. The most likely culprit is **reset action that is too fast** (integral too aggressive), with proportional gain possibly also on the high side. Calling this pure *integral windup* would be too strong unless the output is known to be saturating; the better diagnosis is **aggressive integral action on a lag-dominant process**.

A reset setting of **0.5 repeats/minute** means a reset time of **2 minutes/repeat**, which is usually too fast for a thermal process showing a 4-minute oscillation period.

**Required Elements:**
- Correct identification of integral windup/aggressive reset as primary cause: mandatory
- Open-loop step test BEFORE changing settings: mandatory
- Reduction of integral action (slower reset / more minutes per repeat): mandatory
- Correct reasoning about heat exchanger thermal lag: required
- Recognition that D=0 with significant lag is a tuning opportunity: bonus

**Common Wrong Answers:**
- "Increase gain" — Wrong direction; increases oscillation
- "Add derivative to fix the oscillation" — D alone won't fix an integral-driven oscillation
- Changing settings without any diagnostic step first

**Reference:** Kuphaldt LIII Ch.29 PID Control; Ziegler-Nichols tuning methodology

---

## IUK-T3-DIAG-014
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A Coriolis mass flow meter on a crude oil pipeline has been producing intermittent false high-flow readings — spikes to 150% of range — occurring roughly every 20 minutes and lasting 30–60 seconds. At all other times the meter reads accurately. Process conditions: crude oil, 85°F, 200 PSI, steady flow rate of approximately 60% of meter capacity. The meter is 3 years old and has never required maintenance.

What are your top three diagnostic hypotheses, what is your diagnostic sequence, and what is the most likely root cause given these specific symptom characteristics?

**Correct Answer:**  
**Key clues to interpret:**
- Intermittent spikes (not constant error) → not a calibration or zero issue
- Regular periodicity (~20 minutes) → may be process-driven or external interference
- Spikes to 150% → over-range, not subtle drift
- 30–60 second duration → not a one-scan glitch; sustained but bounded
- Coriolis, crude oil service → likely candidates: entrained gas, density variation, vibration

**Required Elements:**
- Entrained gas as primary hypothesis: mandatory
- Regular periodicity used as diagnostic clue: mandatory
- Diagnostic data pull from meter memory: required
- Correct understanding of how Coriolis responds to two-phase flow: mandatory

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Reference:** Kuphaldt LIII Ch.7 Flow Measurement — Coriolis; Emerson Coriolis application notes on two-phase handling

---

## IUK-T3-DIAG-015
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A solenoid valve (energize-to-open, spring-return to fail-closed) on a natural gas purge line is not opening when commanded. The DCS shows the output signal active (24 VDC output active). A technician measures 24 VDC at the field junction box terminal but 0 VDC across the solenoid coil terminals at the solenoid itself. The solenoid is a Class I Div 2 explosion-proof unit. Describe a complete diagnostic sequence and identify the most likely fault location.

**Correct Answer:**  
**Critical observation:** 24 VDC is present at the junction box but 0 VDC is measured across the solenoid coil. This means voltage is being lost between the JB and the solenoid. The solenoid is NOT receiving power.

**Required Elements:**
- Correct interpretation: 0V across coil = open circuit between JB and coil: mandatory
- Systematic open-circuit tracing sequence: mandatory
- Explosion-proof installation considerations (seals, housing integrity): required
- LOTO/de-energize before entering EXP housing: required for full credit
- Coil resistance check: required

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Reference:** Kuphaldt LIII Ch.4 Switches and Solenoids; NEC Article 501 Hazardous Locations; known gap on Qwen 32B baseline

---

## IUK-T3-DIAG-016
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A vortex flow meter on a steam condensate return line is reading erratically — alternating between steady flow readings and zero-output states. The meter is upstream of a steam trap. The line operates at ~15 PSI and 250°F. Historically the meter has read correctly. No maintenance has been performed. What is causing this behavior, and what is the correct solution?

**Correct Answer:**  
**Diagnosis: Two-phase flow caused by flash steam / condensate mixture.**

Steam condensate at 250°F and 15 PSI is at or near its saturation temperature. When the condensate pressure drops (e.g., at the steam trap or due to minor pressure fluctuations), a portion of the liquid flashes back to steam vapor. This creates intermittent two-phase flow — alternating slugs of liquid condensate and flash steam.

**Required Elements:**
- Flash steam / two-phase flow as root cause: mandatory
- Steam trap failure as probable initiating cause: mandatory
- Explanation of why vortex meters fail in two-phase flow: mandatory
- Correct solution pathway: required

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Reference:** Kuphaldt LIII Ch.7 Flow Measurement — Vortex; steam system engineering principles

---

## IUK-T3-DIAG-018
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A pressure transmitter on a natural gas compressor discharge reads 12 mA at what should be 200 PSIG (50% of its 0–400 PSIG range = 12 mA is correct). But the operator reports the process is actually running at 260 PSIG per an independent mechanical gauge on the same line. The HART device reports the sensor reading matches its 4–20 mA output. What are the three most likely causes and how do you confirm each?

**Correct Answer:**  
**Key fact:** The HART device confirms the sensor reading matches the mA output — this rules out a signal transmission or wiring problem. The discrepancy is between the transmitter's measurement and the mechanical gauge.

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Scoring Rubric:**
Full credit = three valid hypotheses + confirmation method for each + sequence. Two + confirmations = 70%.

**Reference:** Kuphaldt LIII Ch.6; calibration best practices

---

## IUK-T3-DIAG-019
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A flow control loop (FIC) that has been running stably for six months suddenly begins oscillating with a period of approximately 90 seconds and an amplitude of ±15% of setpoint. Nothing has changed in the DCS configuration. The flow transmitter (orifice + DP cell) is showing the oscillation in real-time. The control valve is a globe valve with air-to-open actuator. List five possible causes in order of probability and describe a diagnostic test for each.

**Correct Answer:**  
**Key observation:** The oscillation appeared suddenly after six months of stable operation, with nothing changed in the DCS. This eliminates tuning as the primary cause (tuning didn't change). The oscillation IS visible in the flow transmitter — so either the flow is truly oscillating, or the transmitter signal is oscillating.

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Scoring Rubric:**
Full credit = five hypotheses with correct ranking rationale + test for each. Four with tests = 75%.

**Reference:** Kuphaldt LIII Ch.7, Ch.29, Ch.32

---

## IUK-T3-DIAG-020
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A thermocouple temperature measurement in a high-temperature furnace (Type K, range 0–1200°C) begins reading exactly 0°C after an instrument panel shutdown and restart. All other thermocouples in the furnace continue reading correctly. The DCS input card diagnostic shows no fault. The thermocouple circuit appears complete (no open circuit alarm). What has happened and what is the most likely cause?

**Correct Answer:**  
**What happened:**
The DCS reads 0°C exactly. For a Type K thermocouple, 0°C corresponds to 0 mV (by definition — the thermocouple tables are referenced to 0°C). A reading of exactly 0°C after restart means the DCS input card is reading 0 mV with the thermocouple connected.

0 mV can come from:
1. An open thermocouple circuit WHERE the DCS card's bias resistor is not pulling the input high/low — but the problem states no open circuit alarm
2. A shorted thermocouple — both leads shorted together at the thermocouple head or junction box, producing zero differential voltage. No current loop = no open circuit alarm on a passive mV circuit.
3. Cold junction compensation failure: If the cold junction is at 0°C (not the actual terminal temperature of ~25°C), the indicated temperature will be off — but not necessarily exactly 0°C unless the actual TC signal is also zero.

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Scoring Rubric:**
Full credit = reasoning from 0 mV condition + reversed polarity as primary cause + diagnostic method. Short circuit as secondary hypothesis required. Claim of open circuit (contradicting the no-alarm premise) = penalty.

**Reference:** Kuphaldt LIII Ch.8 Thermocouple polarity; NIST TC tables

---

## IUK-T3-DIAG-021
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A level transmitter on a reactor (differential pressure type, wet leg) is reading 40% ABOVE the actual level as verified by an independent nuclear level gauge. The wet leg process fluid is demineralized water. The transmitter was recently reinstalled after the leg was refilled. What is the most likely cause and what would you verify first?

**Correct Answer:**  
**Most likely cause: The wet leg was not restored to its correct constant head — it is underfilled, partially drained, or contains trapped gas on the LP/reference side.**

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Scoring Rubric:**
- Full credit = identifies underfilled / gas-bound wet leg as primary cause + explains why lower LP head makes reading high + states first verification step
- Partial = identifies wet-leg problem but not the pressure-direction logic
- Zero = claims overfilled wet leg as cause of high reading

**Reference:** Kuphaldt LIII Ch.6; wet-leg DP level application notes

---

## IUK-T3-DIAG-022
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A newly commissioned Coriolis mass flow meter on a liquid CO₂ line reads 0 mA with no process flow — as expected. But when flow is established, the meter never reads above 6 mA (approximately 12.5% of range) even though operators know from process balance that flow is approximately 50% of the meter's rated capacity. The HART diagnostic shows no fault flags. Temperature of the liquid CO₂ is −20°C. What is causing this and what is the remedy?

**Correct Answer:**  
**Key facts:**
- 6 mA output = (6-4)/16 = 12.5% of range
- Expected flow ≈ 50% of range
- HART shows no faults
- Liquid CO₂ at −20°C

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Scoring Rubric:**
Full credit = zero calibration issue OR density configuration issue as cause + HART verification steps + correct remedy. Citing two-phase flow without explanation of why HART doesn't flag it = partial.

**Reference:** Kuphaldt LIII Ch.7; Emerson Micro Motion Coriolis commissioning guide

---

## IUK-T3-DIAG-023
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
An air-to-close, spring-to-open (fail-open) control valve on a cooling water line is not opening when the controller output drops to 0% (0 PSI to positioner). The process temperature is rising. The positioner is a conventional pneumatic positioner (no HART). Describe your complete diagnostic sequence.

**Correct Answer:**  
**Expected behavior:** ATC valve + 0% controller output + pneumatic positioner → positioner should exhaust air → spring should push valve to full open position.

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Scoring Rubric:**
Full credit = systematic top-down sequence from signal source to valve + all seven steps. Jumping to valve mechanical without checking signal = 40%.

**Reference:** Kuphaldt LIII Ch.32; Fisher control valve service manual

---

## IUK-T3-DIAG-024
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
An ultrasonic level transmitter on a large open-top water storage tank is working correctly for three months. During summer, it begins producing erratic, intermittently high readings — sometimes spiking to 95–100% level indication when actual level is only 60–70%. The problem occurs between 10 AM and 3 PM daily and is absent at night. What is the most likely cause?

**Correct Answer:**  
**Pattern analysis:** Intermittent, time-of-day dependent, summer-specific, during peak sun hours. This is a classic environmental interference pattern.

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Scoring Rubric:**
Full credit = thermal gradient / false echo as primary cause + time-of-day pattern correctly analyzed + remediation. Solar heating on transducer as secondary = acceptable. Pattern analysis required.

**Reference:** Kuphaldt LIII Ch.6; Endress+Hauser Micropilot level transmitter application notes

---

## IUK-T3-DIAG-025
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A PLC-based SIS receives a trip signal from a high-pressure switch (PSHH) but does not actuate the shutdown valve. The bypass switch is confirmed OFF. The PLC diagnostic display shows the PSHH input as active (1). The shutdown valve output is shown as active (1). The shutdown valve (spring-return, normally open, fail-open, solenoid de-energize to open) does not open. Provide a complete diagnostic sequence with likely causes.

**Correct Answer:**  
**System logic understanding:**
- PSHH active → SIS should DE-ENERGIZE the solenoid valve (fail-safe design: de-energize to trip)
- The PLC output shows "1" (active/energized) for the shutdown valve
- This is contradictory: if the PLC is commanding a trip, the output should be "0" (de-energized)

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Scoring Rubric:**
Full credit = recognition of logic/state contradiction + logic convention as first check + forced output check + hardware output fault. Missing the "active=1 contradiction" analysis = 40%.

**Reference:** IEC 61511; ISA-84; PLC troubleshooting fundamentals

---

## IUK-T3-DIAG-026
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A differential pressure level transmitter on an ethylene glycol storage tank is reading approximately 15% low compared to a sight glass. The tank is a closed, nitrogen-blanketed vessel at approximately 3 PSIG. The transmitter HP tap is at the bottom, LP tap is at the top (into the nitrogen blanket). The transmitter is BELOW the vessel. No maintenance has been done recently. Diagnose methodically.

**Correct Answer:**  
**System analysis:**
This is a suppressed-zero DP level application on a pressurized vessel. The LP side connects to the nitrogen blanket (variable pressure). The DP transmitter measures:
ΔP = (Fluid head + vessel pressure) − (vessel pressure + LP impulse line head)
= Fluid head − LP impulse line head (vessel pressure cancels)

For the transmitter mounted below the bottom tap, there's a constant fluid column in the HP impulse line (suppressed zero). This was presumably calibrated out at installation.

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Scoring Rubric:**
Full credit = ΔP physics correctly laid out + three valid hypotheses with LP condensate or gas pocket as primary + verification methods.

**Reference:** Kuphaldt LIII Ch.6; Rosemount DP level application guide

---

## IUK-T3-DIAG-028
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A magnetostrictive liquid level transmitter on a diesel fuel storage tank reads 2.3 meters. A manual tape measurement shows 2.6 meters. The transmitter has been in service for 4 years without calibration. The float is made of stainless steel and the process fluid is diesel fuel. Temperature at measurement time: 35°C. Provide your diagnosis and verify the most likely cause.

**Correct Answer:**  
**2.3 m vs 2.6 m = 0.3 m (30 cm) low reading — a significant systematic error.**

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Scoring Rubric:**
Full credit = magnetostrictive principle understood + float sinking as primary + verification method (weigh/inspect float). Drift as secondary = acceptable.

**Reference:** Kuphaldt LIII Ch.6; MTS Systems magnetostrictive level documentation

---

## IUK-T3-DIAG-029
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A 2-wire 4–20 mA HART transmitter in a remote field location is reading 3.6 mA — below live zero, indicating a fault. The DCS shows "sensor failure." A HART communicator connected at the field junction box cannot establish communication. The loop supply voltage at the junction box is 24 VDC. What is your diagnostic sequence?

**Correct Answer:**  
**3.6 mA is a deliberate fault signal, not a normal process value.** In a 4–20 mA smart transmitter, a low output such as **3.6 mA** typically means the device has detected a problem and is driving a defined low-fault current (NAMUR NE 43 style behavior).

The fact that the loop supply is **24 VDC at the JB** means the loop is not simply dead. The transmitter is powered enough to put something on the loop, but it may still have inadequate terminal voltage, a cable problem, or an internal fault.

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Scoring Rubric:**
Full credit = NAMUR understanding (deliberate low-fault) + voltage check + cable insulation test + systematic sequence. Assuming open circuit with evidence of 3.6 mA signal present = error.

**Reference:** NAMUR NE 43; Kuphaldt LIII Ch.4; HART specification

---

## IUK-T3-DIAG-030
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A turbine flow meter on a refined oil product pipeline is reading 8% HIGH compared to a downstream custody transfer Coriolis meter. The turbine meter is 10 years old. The oil is clean and the flow conditions are within specification. There has been no recent maintenance on either meter. What are the four most likely causes and what single test would most efficiently distinguish between them?

**Correct Answer:**  
**8% high on a turbine vs. Coriolis is significant and consistent — this is not noise.**

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Scoring Rubric:**
Full credit = four causes with bearing wear and K-factor/viscosity both included + prover as the single efficient test. Three causes = 70%.

**Reference:** Kuphaldt LIII Ch.7; AGA-7; API MPMS Chapter 4 (Proving)

---

## IUK-T3-DIAG-031
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A PID flow control loop is running in AUTO. The setpoint is 300 GPM. The PV is steady at 298 GPM — 2 GPM below setpoint. The controller has been in AUTO for 4 hours. There is NO integral action configured (I-only = minimum/disabled). What does this tell you, and is the loop performing correctly?

**Correct Answer:**  
**Analysis:**
A PID controller without integral action (P-only) will exhibit steady-state offset — the process settles at a value different from setpoint, with the controller output held at a constant value that provides just enough manipulated variable to balance the load at the offset condition.

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Scoring Rubric:**
Full credit = recognition that P-only offset is expected + correct analysis + integral required to eliminate offset. Calling it a fault = wrong.

**Reference:** Kuphaldt LIII Ch.29

---

## IUK-T3-DIAG-032
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
An electric heat tracing circuit on an impulse line for an outdoor steam flow transmitter has failed. Ambient temperature is −15°C. The transmitter was reading correctly but now reads 0 mA. Process pressure is normal per a nearby pressure gauge. Describe the failure mode and the correct sequence to restore the measurement.

**Correct Answer:**  
**Diagnosis:**
Heat tracing failed + cold ambient + steam impulse lines = frozen impulse lines. The transmitter reads 0 mA, which corresponds to 4 mA at minimum DP (which is below 4 mA, so the DCS reads a fault). The 0 mA reading indicates the transmitter has gone to a fault-low condition.

If the impulse lines are frozen:
- Frozen HP line: no pressure transmitted to HP side of transmitter → transmitter sees atmospheric pressure on HP side, and whatever the LP side presents
- Frozen LP line: no pressure transmitted to LP side → LP side is at whatever it was when it froze
- Both frozen: the transmitter sees the "trapped" pressure at the moment of freeze — could be any value, possibly near zero DP (both lines at same trapped pressure)

With both lines frozen and the DP transmitter seeing zero differential (both sides at same trapped pressure), the output would be at or near 4 mA (zero flow), not 0 mA.

0 mA fault condition suggests the transmitter has detected a hardware fault — possibly the transmitter itself has been damaged by ice expansion in the impulse fitting or transmitter body, or the transmitter is experiencing an internal low-voltage condition from ice expansion forcing the diaphragm beyond its limit and triggering a fault.

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Scoring Rubric:**
Full credit = frozen impulse lines as diagnosis + no direct flame caution + correct thaw procedure + root cause repair of heat tracing + calibration verification.

**Reference:** Kuphaldt LIII Ch.6; Heat tracing standards (IEEE 515); site cold weather procedures

---

## IUK-T3-DIAG-033
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A Rotameter (variable area flow meter) on a gas measurement application is reading 35% high compared to a calibrated reference flow meter installed in series. The Rotameter is calibrated for air at standard conditions. The actual gas being measured is methane at 150 PSIG and 80°F. No correction factor was applied. Explain why the reading is high and calculate the approximate correction factor.

**Correct Answer:**  
**Root cause:** The meter is being used on a gas whose **actual operating density is far higher** than the calibration basis (air at standard conditions). For a gas rotameter, that drives the float to a higher position for the same local volumetric flow and makes the air-calibrated scale **read high**.

A first-pass correction is:
\[
Q_{actual} pprox Q_{indicated} 	imes \sqrt{
ho_{cal}/
ho_{actual}}
\]

Using the values in the problem:
- Air at standard conditions: \(
ho_{cal} pprox 0.0765\,lb/ft^3\)
- Methane at 150 PSIG and 80°F (ideal-gas approximation): \(
ho_{actual} pprox 0.458\,lb/ft^3\)

So:
\[
CF = \sqrt{0.0765/0.458} pprox 0.41
\]

That means:
- **Actual flow ≈ 0.41 × indicated flow**, or
- **Indicated ≈ 2.45 × actual** if no correction is applied

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Scoring Rubric:**
Full credit = gas density principle identified + direction of error correct + correction factor formula shown with reasonable numbers. Formula direction wrong = 40%.

**Reference:** Kuphaldt LIII Ch.7; Rotameter manufacturer calibration correction guides

---

## IUK-T3-DIAG-034
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A pneumatic controller output (3–15 PSI) to a control valve positioner is showing excessive hunting — the output pressure oscillates between 5 and 11 PSI (60 PSI of amplitude equivalent to ±25% output swing) at about 2 Hz even in MANUAL mode with a fixed manual set. The controller is a Foxboro 130 series pneumatic controller. What is wrong and where do you look first?

**Correct Answer:**  
**Critical observation: The oscillation is present in MANUAL mode with a fixed manual set.**

In MANUAL mode, a properly functioning pneumatic controller should output a stable, steady pressure corresponding to the manual setting. Oscillation in MANUAL eliminates the feedback loop, the measurement, the setpoint, and the integral action as causes. The problem is in the OUTPUT section of the pneumatic controller itself.

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Scoring Rubric:**
Full credit = MANUAL mode analysis (rules out feedback loop) + relay as primary pneumatic cause + diagnostic sequence. Attributing to process or tuning in manual mode = fail.

**Reference:** Kuphaldt LIII Ch.29; Foxboro 130 series maintenance manual

---

## IUK-T3-DIAG-035
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A HART-enabled flow transmitter communicates correctly with a HART communicator in the field, but the DCS cannot read HART digital data from the same device. The 4–20 mA signal reads correctly in the DCS. What are the three most likely causes for HART digital communication failure at the DCS while field communication succeeds?

**Correct Answer:**  
**Key distinction:** Field HART works (at the device) but DCS HART doesn't (from the safe area). The 4–20 mA analog is fine.

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Scoring Rubric:**
Full credit = all three valid causes with verification method. Two causes = 65%.

**Reference:** FieldComm Group HART specification; DCS HART integration guides; Kuphaldt LIII Ch.14

---

## IUK-T3-DIAG-036
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A control loop (temperature, reverse-acting controller, ATO valve) is in AUTO and is experiencing the following: when a disturbance pushes the temperature above setpoint, the controller output decreases (correct), the valve closes (correct), but the temperature continues to rise for 2–3 minutes before finally coming down. When it comes down, it overshoots setpoint by 8°F before finally settling. The proportional gain is 2.0, integral is 1.0 repeat/minute. Diagnose and prescribe tuning changes.

**Correct Answer:**  
**Symptom analysis:**
- Temperature rises above SP → controller correctly reduces output → valve closes → but temperature keeps rising for 2-3 minutes. This 2-3 minute delay before the process responds indicates significant **process dead time** or a very long **process time constant**.
- Then overshoot of 8°F indicates the integral action has wound up during the 2-3 minute non-response period, driving the valve farther closed than the true correction requires. By the time the process responds, the valve is over-closed, causing undershoot below setpoint (the overshoot is in the undercorrection direction after overcorrection).

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Scoring Rubric:**
Full credit = dead time + integral windup during dead time as diagnosis + both tuning changes with reasoning. Tuning prescription without diagnosis = 50%.

**Reference:** Kuphaldt LIII Ch.29

---

## IUK-T3-DIAG-037
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A differential pressure transmitter used for flow measurement reads correctly at low and high flow rates, but reads approximately 10% HIGH consistently in the 40–60% flow range (mid-range). At 0% and 100% flow (as checked with process balance), the transmitter reads correctly. What is the most likely cause?

**Correct Answer:**  
**Key diagnostic clue:** Correct at 0% (zero DP) and 100% (full DP), but HIGH by 10% at mid-range. This is a non-linearity issue — not a zero error, not a span error, but an S-curve type deviation in the middle of the range.

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Scoring Rubric:**
Full credit = nonlinearity correctly identified (not zero or span error) + orifice plate as primary cause + confirmation method.

**Reference:** ISO 5167; Kuphaldt LIII Ch.7; ASME MFC-3M

---

## IUK-T3-DIAG-038
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A nuclear level gauge (gamma radiation source + detector) on a reactor vessel shows a sudden drop in the level indication from 55% to 12% over 15 minutes, then stabilizes at 12%. Process operations confirm the actual level has not changed. All other instruments on the reactor show normal process conditions. What are the diagnostic possibilities and which is most serious?

**Correct Answer:**  
**Most serious possibility: a source / shutter / source-geometry problem that increases radiation at the detector.**

A nuclear level gauge is inverse:
- **More attenuation** through the vessel contents → **less** detector count → **higher** level indication
- **Less attenuation / more detector flux** → **higher** detector count → **lower** level indication

So a sudden false drop from 55% to 12% with stable process conditions means the detector is effectively seeing **too much radiation**.

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Scoring Rubric:**
Full credit = source shutter failure identified as MOST SERIOUS + radiation safety action as first priority + at least one electronics failure hypothesis. Failing to identify radiation safety emergency = T5-level safety failure flag.

**Reference:** 10 CFR 20 (NRC radiation protection); site radiation safety procedures; Kuphaldt LIII Ch.6 Nuclear Level

---

## IUK-T3-DIAG-039
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A flow totalizer connected to a 4–20 mA flow transmitter is showing accumulated flow that is 22% LOWER than the independent process flow accounting over the same period. The real-time flow rate display matches between the totalizer and the process accounting. What is the likely cause?

**Correct Answer:**  
**Key contradiction:** Real-time flow rate display matches (the instantaneous signal is correct) but accumulated total is 22% low. This eliminates signal accuracy and calibration as the cause — if the instantaneous reading were wrong, both would be wrong.

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Scoring Rubric:**
Full credit = low-flow cutoff as primary cause + explanation + verification method. Blaming signal calibration = wrong (contradicted by matching real-time display).

**Reference:** Kuphaldt LIII Ch.7; DCS totalizer configuration guides

---

## IUK-T3-DIAG-061
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A vortex flow meter on a steam line reads correctly at high steam demand (greater than 40% of range). Below 40% demand, the meter becomes erratic — sometimes reading correctly, sometimes reading zero, and occasionally showing random high spikes. No physical changes were made to the meter or process. Diagnose.

**Correct Answer:**  
**Classic vortex meter minimum velocity problem — the process is operating below the meter's minimum measurable velocity at low-demand conditions.**

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Scoring Rubric:**
Full credit = minimum velocity/Reynolds number as cause + threshold correlation + remedy options. Calling the meter faulty = wrong.

**Reference:** Kuphaldt LIII Ch.7; vortex meter minimum velocity specifications

---

## IUK-T3-DIAG-062
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A technician tests a 4–20 mA loop and finds the following:
- DCS input shows 8.2 mA
- Transmitter HART display shows process variable = 150 PSI (correct process pressure)
- Transmitter HART shows output = 12.4 mA (which is correct for 150 PSI on 0–300 PSI range)
- Calibrated clamp meter on the loop reads 12.4 mA at the junction box
- DCS input card reads 8.2 mA

What is the problem and where is it?

**Correct Answer:**  
**The problem is between the junction box and the DCS input card.** The loop current is 12.4 mA everywhere in the field but the DCS receives 8.2 mA.

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Scoring Rubric:**
Full credit = shunt/parallel path analysis + three location-specific causes + diagnostic steps. "Transmitter problem" = wrong (HART shows correct output).

**Reference:** Kuphaldt LIII Ch.4; Kirchhoff's current law in loop troubleshooting

---

## IUK-T3-DIAG-063
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A VFD (variable frequency drive) for a pump motor was recently installed adjacent to instrument cable trays containing 4–20 mA signals. After commissioning the VFD, three nearby transmitters began showing noise bursts that correlate exactly with the VFD's switching frequency (approximately 4 kHz). The transmitters are HART-enabled and their HART communication has also become unreliable. Describe the EMI coupling mechanism and three remediation options in priority order.

**Correct Answer:**  
**EMI coupling mechanism:**
VFDs generate high-frequency switching transients (PWM — Pulse Width Modulation) at the carrier frequency (typically 2–16 kHz). The DC bus switches at this rate, creating high dV/dt transitions that generate:
1. **Conducted EMI:** Current transients travel along the motor cable conductors and can couple through shared grounding paths to instrument circuits
2. **Radiated EMI:** The rapidly switching current creates a magnetic field that radiates from the VFD output cable (unshielded or inadequately shielded) and induces voltage into adjacent parallel signal cables
3. **Capacitive coupling:** High dV/dt switching can capacitively couple into nearby parallel cable runs, especially in the same tray

HART communication uses 1200/2200 Hz FSK — right in the frequency range where VFD switching harmonics appear. VFD noise can overwhelm the HART signal.

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Scoring Rubric:**
Full credit = EMI coupling mechanism explained (radiated + conducted) + three options in priority order with reasoning. One option = 40%.

**Reference:** Kuphaldt LIII Ch.13; IEEE 1100; VFD installation guidelines (Rockwell, ABB, Siemens)

---

## IUK-T3-DIAG-064
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A process analytical chromatograph (GC) on a natural gas pipeline is reporting a methane concentration that is 3.2 mol% lower than expected based on process mass balance. The sample conditioning system (SCS) shows normal sample flow and temperature. All calibration gases check out. The analysis cycle is running normally. Diagnose the most likely source of error.

**Correct Answer:**  
**Most likely source of error: sample dilution by air ingress or another non-process gas entering the sample system upstream of the analyzer.**

Why this fits:
- Calibration gases check out
- Cycle timing is normal
- SCS flow and temperature look normal
- Methane is reported **LOW**, not high

If heavier hydrocarbons were condensing out, methane mole fraction would usually look **higher**, not lower, because the remaining gas would be leaner in C2+ components. So condensation is the wrong direction for this symptom.

A small leak that admits **air** will dilute the sample and pull methane mole % downward. The best confirmation is to inspect the chromatogram for **nitrogen and oxygen** or for an unexpected increase in inerts.

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Scoring Rubric:**
Full credit = air infiltration as primary + chromatogram evidence check + calibration reference standard as secondary. Condensation causing methane loss = wrong direction (would show higher methane%).

**Reference:** Kuphaldt LIII Ch.10; GC sample conditioning system diagnostics; ISA-76.00.02

---

## IUK-T3-DIAG-065
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A control room DCS suddenly shows 40 instruments going to their fail-safe values simultaneously. The plant is on a single DCS. Operations confirms no process upset occurred. The DCS shows all controllers in MANUAL. What are your first three diagnostic steps and most likely causes?

**Correct Answer:**  
**40 instruments simultaneously to fail-safe with no process event = DCS/system-level failure, not individual instrument failures.**

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Scoring Rubric:**
Full credit = system-level failure (not instruments) + three diagnostic steps in order (system health page first) + four possible system causes.

**Reference:** Kuphaldt LIII Ch.14; DCS system documentation (Emerson DeltaV, Honeywell C300)

---

## IUK-T3-DIAG-066
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A gas chromatograph used for natural gas quality measurement passes its daily calibration check at 8 AM. At 2 PM, a process engineer compares the GC methane heating value output to a hand-held portable combustion analyzer and finds the GC is reading 8% lower BTU/SCF. The calibration gas is unchanged. What should be investigated first?

**Correct Answer:**  
**GC passes calibration at 8 AM and reads correctly, then drifts 8% low on heating value by 2 PM without calibration change.**

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Scoring Rubric:**
Full credit = process composition change as first hypothesis + verification via full compositional comparison + portable analyzer reliability as second hypothesis.

**Reference:** Kuphaldt LIII Ch.10; GC application notes; AGA-5 (Gas Energy Measurement)

---

## IUK-T3-DIAG-067
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A FOUNDATION Fieldbus H1 segment has 8 devices. Suddenly, 3 of the 8 devices lose communication simultaneously. The other 5 continue communicating normally. All 8 devices are wired on the same segment trunk with individual spurs. What does this failure pattern indicate?

**Correct Answer:**  
**3 of 8 devices lose communication while 5 continue = the failure affects a subset of the segment, not the entire segment.**

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Scoring Rubric:**
Full credit = common junction/spur failure as primary cause + reasoning from "subset failure" pattern + diagnostic steps. "Entire segment issue" = wrong (contradicted by 5 working devices).

**Reference:** FieldComm Group FF H1 physical layer; Kuphaldt LIII Ch.14

---

## IUK-T3-DIAG-068
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A level transmitter (differential pressure type) on a gas-liquid separator reads correctly when the separator is at normal operating pressure (150 PSIG). When the pressure is reduced to 30 PSIG for a depressurization event, the level reading jumps to 95% even though operators confirm the level is only at 40% by sight glass. As pressure is restored, the reading returns to normal. Explain the failure mechanism.

**Correct Answer:**  
**Failure mechanism:** The **LP reference leg is not actually constant when the separator pressure is reduced.**

This is a wet-leg / seal-fluid problem. At normal pressure, the LP leg behaves like a stable liquid reference. When the separator is depressurized, the reference-leg fluid can:
- **flash / partially vaporize**, or
- change effective density enough to reduce LP hydrostatic head.

If LP backpressure drops while HP still reflects the true bottom head, then:
\[
DP = HP - LP
\]
increases artificially and the level indication jumps **high**.

That explains the symptom pattern exactly:
- correct at normal pressure,
- false high during depressurization,
- returns to normal as pressure is restored.

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Scoring Rubric:**
Full credit = seal fluid vaporization or LP reference change as cause + pressure-dependent mechanism + remedy. Generic "calibration issue" without physics = 40%.

**Reference:** Kuphaldt LIII Ch.6; DP level transmitter wet-leg design guides

---

## IUK-T3-DIAG-069
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A solenoid valve that is normally energized (energized to close, de-energizes to open) in a SIS function is found, during a proof test, to NOT open when the solenoid is de-energized. The valve is a spring-return, 2-way, normally-open design. The coil resistance measures 350Ω (spec: 350±20Ω). 24 VDC is confirmed present at the coil terminals when energized. When de-energized, the voltage drops to 0V as expected. What has failed?

**Correct Answer:**  
**The solenoid de-energizes correctly (coil resistance normal, voltage goes to 0V), but the valve does NOT open. The electrical component is working normally.**

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Scoring Rubric:**
Full credit = mechanical failure (not coil) correctly identified + spring failure + plunger seizure + verification steps. Diagnosing coil as failed = wrong (coil checks normal).

**Reference:** Kuphaldt LIII Ch.32; solenoid valve maintenance guides; IEC 61511 proof test failure analysis

---

## IUK-T3-DIAG-070
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
An ESD (Emergency Shutdown) system for a natural gas compressor station receives a signal from a GD (gas detector) at 60% LEL, which should trigger a compressor trip. The SIS records show the GD input activated at 14:22:31. The compressor ESD output activated at 14:22:34 — 3 seconds later. The site's safety study specified a maximum process safety time (PST) of 5 seconds from gas detection to compressor shutdown. Is this acceptable? What should be reviewed?

**Correct Answer:**  
**The 3-second response time appears to be within the 5-second PST — but this analysis is INCOMPLETE and potentially dangerous if accepted at face value.**

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Scoring Rubric:**
Full credit = 3 seconds is only SIS logic time + GD response lag + compressor coast-down + total SIF response time analysis + PST verification recommendation.

**Reference:** IEC 61511 Clause 10 (SRS response time); gas detector T90 specifications; API RP 505

---

## IUK-T3-DIAG-071
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A Coriolis mass flow meter on a fuel gas line to a furnace reads correctly 98% of the time. Approximately once per shift, the reading drops to exactly zero for 30–90 seconds, then returns to normal without any operator action. The gas pressure and flow are confirmed steady during the zero events (by an upstream orifice meter which shows no change). Diagnose.

**Correct Answer:**  
**Intermittent zero-output lasting 30–90 seconds with confirmed steady actual flow = the Coriolis meter is performing a self-diagnostic event, not detecting real zero flow.**

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Scoring Rubric:**
Full credit = automatic zero routine as primary cause + verification via configuration check + event log + remedy options. "Intermittent process issue" = wrong (upstream meter shows no change).

**Reference:** Micro Motion Coriolis Smart Meter Verification documentation; Endress+Hauser Promass auto-zero documentation

---

## IUK-T3-DIAG-072
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
An analog output (AO) card in a DCS is commanding a control valve to 65%. The AO card diagnostic shows "output = 65% (13.04 mA)." A clamp meter on the wire reads 13.04 mA. But the valve positioner shows its input signal as 9.8 mA, and the valve is at approximately 40% open. What is the explanation?

**Correct Answer:**  
**The AO card outputs 13.04 mA. The positioner input reads 9.8 mA. The valve is at 40%. There is a 3.24 mA discrepancy between the AO output and the positioner input.**

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Scoring Rubric:**
Full credit = ground fault analysis (parallel path) + direction (AO sources full current, positioner sees less) + fault resistance concept. "AO card fault" = wrong (AO shows correct output).

**Reference:** Kuphaldt LIII Ch.4; loop current troubleshooting

---

## IUK-T3-DIAG-073
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A process plant uses a HART multiplexer connected to 32 HART transmitters to poll device status and provide diagnostics to a CMMS (Computerized Maintenance Management System). After a DCS upgrade, operators notice that HART multiplexer poll data is updating very slowly — some transmitters go hours without updating. No physical wiring was changed. Diagnose.

**Correct Answer:**  
**HART multiplexer poll rate problem after a DCS upgrade — no physical change. The issue is in the communication or configuration layer, not the hardware.**

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Scoring Rubric:**
Full credit = dual HART master conflict as primary cause + polling mechanism explanation + network as secondary + diagnostic steps.

**Reference:** FieldComm Group HART specification (single primary master per loop); Kuphaldt LIII Ch.14

---

## IUK-T3-DIAG-074
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
During commissioning of a new heat exchanger temperature cascade control system (outer loop: shell-side outlet temperature; inner loop: tubeside flow), a process engineer complains that the outer temperature loop is oscillating slowly with a period of about 25 minutes even though the inner flow loop is properly tuned and runs stably when tested in isolation. What is the most likely cause?

**Correct Answer:**  
**A 25-minute oscillation in the outer (temperature) loop that does not appear in the inner (flow) loop when tested alone = a cascade tuning interaction problem.**

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Scoring Rubric:**
Full credit = cascade time constant mismatch + outer integral too fast + solution (detune outer loop). "Inner loop problem" = wrong (inner is stable in isolation).

**Reference:** Kuphaldt LIII Ch.29 Cascade Control; ISA process control guidelines

---

## IUK-T3-DIAG-075
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
An instrument engineer reviews an alarm summary report and notices that one high-pressure alarm (PAH-1047) has been acknowledged and cleared 847 times in the past 30 days. The alarm averages 28 activations per day and is acknowledged within 1–2 minutes each time by operators who then take no further action. The process pressure is confirmed well below the alarm setpoint during most of these events. What is happening and what must be done?

**Correct Answer:**  
**28 activations per day with immediate acknowledgment and no action = classic "nuisance alarm" or "chattering alarm."**

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Scoring Rubric:**
Full credit = chattering alarm identified + operator desensitization risk + root cause investigation + deadband/hysteresis + formal alarm rationalization.

**Reference:** ISA-18.2; EEMUA 191; Kuphaldt LIII Ch.29

---

## IUK-T3-DIAG-076
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
After calibrating a 4–20 mA pressure transmitter in the shop (0–500 PSI range), a technician returns it to the field and re-connects it. The transmitter immediately reads 24 mA (over-range high fault) with no process pressure applied (isolation valves still closed). The shop calibration was verified correct before leaving. What happened?

**Correct Answer:**  
**Most likely explanation:** The transmitter was returned from the shop in a non-normal output state — for example **fixed-current / loop-test mode**, simulation mode, or an upscale fault / misrange condition — rather than actually seeing real process pressure.

Why this fits:
- The shop calibration was verified before leaving
- **Isolation valves are still closed**, so real process pressure should not be present
- A reading of **24 mA** is characteristic of an overrange / forced-output condition, not a believable field pressure with everything isolated

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Scoring Rubric:**
Full credit = HART fixed output mode as primary cause + verification via HART + residual pressure as secondary + note to exit fixed output mode after calibration.

**Reference:** Kuphaldt LIII Ch.4; HART communicator calibration procedure notes

---

## IUK-T3-DIAG-077
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A flow control loop (FIC-301, liquid service) shows the following trend: the PV fluctuates ±8% around setpoint at a frequency of approximately 0.5 Hz (one complete cycle every 2 seconds). The controller is in AUTO. The controller gain is 0.5 and the reset is 10 minutes/repeat — both very conservative settings. Manual operation of the controller output shows smooth valve response. The flow transmitter (orifice + DP cell) shows the oscillation in the PV signal. What is the root cause?

**Correct Answer:**  
**Key observation: The oscillation is 0.5 Hz (2-second period), which is very fast for a liquid flow control loop. Conservative controller tuning (Gain=0.5, I=10 min) rules out tuning as the cause. Manual output shows smooth valve response — rules out stiction. The PV SIGNAL itself is oscillating.**

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Scoring Rubric:**
Full credit = process pulsation (not loop or instrument fault) + upstream PD pump hypothesis + frequency correlation + remedy.

**Reference:** Kuphaldt LIII Ch.7 (pulsation effects on DP meters); ASME MFC-3M

---

## IUK-T3-DIAG-078
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A new technician reports that she calibrated a Level transmitter and found it to be "off by 10 PSI" at every point in the calibration. She trimmed the zero by –10 PSI and the span calibrated correctly. The same day, the senior technician notices the level indication is reading 15% HIGH compared to a sight glass. Explain what happened.

**Correct Answer:**  
**Core diagnosis:** The technician mistook a required installation offset for calibration error and used the wrong kind of trim.

This is the classic mistake of confusing:
- **sensor trim** (changing the transmitter’s interpretation of the input),
with
- **ranging / configured LRV-URV** (telling the transmitter what pressures correspond to 4 and 20 mA in the installed application).

In many level applications there is a **suppressed or elevated zero** caused by static head, wet leg, remote seal elevation, or mounting geometry. A constant offset seen during calibration is often **part of the application physics**, not sensor error.

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Scoring Rubric:**
Full credit = suppressed zero physics explained + incorrect trim identified as removing/modifying necessary offset + resulting direction of error. Calibration procedure confusion = required element.

**Reference:** Kuphaldt LIII Ch.6; HART sensor trim procedures

---

## IUK-T3-DIAG-079
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A refinery has four identical crude distillation unit (CDU) temperature transmitters at corresponding locations on four parallel towers. All are Type K TCs with identical transmitters. Three of the four consistently read within ±3°F of each other. The fourth consistently reads 45°F LOW compared to the other three. The fourth transmitter passed its last calibration (verified against a traceable standard). Diagnose.

**Correct Answer:**  
**Transmitter calibration is good. Three similar units read consistently. The fourth reads 45°F low. This is a systematic negative offset on one instrument that is NOT a calibration error.**

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Scoring Rubric:**
Full credit = extension wire as primary cause + CJC error as secondary + TC contamination as tertiary + ~1 mV signal analysis.

**Reference:** Kuphaldt LIII Ch.8; ASTM E230; petroleum refinery TC contamination literature

---

## IUK-T3-DIAG-080
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A flow integrator (totalizer) on a gas measurement system shows a monthly volume that is 3.7% HIGHER than the previous month for the same production. The transmitter reads correctly and the orifice plate was inspected and found clean. The only change last month was that the operating pressure was raised from 240 PSIG to 280 PSIG, but the flow computer uses real-time pressure correction. Diagnose.

**Correct Answer:**  
**Volume is 3.7% higher with a pressure increase from 240 to 280 PSIG. Real-time pressure correction is active. But there's still a volume discrepancy.**

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Scoring Rubric:**
Full credit = pressure compensation fault as cause + flow computer checking what pressure it's actually using + calculation verification.

**Reference:** AGA-3; API MPMS 14.3; Kuphaldt LIII Ch.7

---

## IUK-T3-DIAG-082
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A plant UPS (Uninterruptible Power Supply) for instrument panels transfers to battery during a utility power event. All critical instrument loops remain powered (24 VDC loops). However, during the UPS-to-battery transfer, three HART transmitters simultaneously go to 3.6 mA (below-range fault) for approximately 500 milliseconds, then recover. Control valves at their fail-safe positions during this window caused a momentary process upset. Explain the failure mechanism.

**Correct Answer:**  
**HART transmitters fault simultaneously for 500ms during UPS transfer → process upset → recover. This is a power quality event, not a measurement failure.**

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Scoring Rubric:**
Full credit = UPS transfer causes 24 VDC droop + 24VDC recovery time (not just transfer time) + power-on startup sequence as the 3.6 mA source + hold-up capacitance solution.

**Reference:** NAMUR NE 43; Kuphaldt LIII Ch.4; UPS and instrument power supply engineering

---

## IUK-T3-DIAG-083
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A new instrument engineer is asked to troubleshoot a flow control loop that "never settled since the upgrade." The loop controls cooling water flow to a reactor. The PV oscillates continuously. She checks and documents: Controller gain = 3.5, Ti = 0.8 min/repeat, Td = 0. The valve is a 3-inch linear globe, ATO/fail-closed. The process: cooling water flow, 0–150 GPM range, measured by magnetic flowmeter. The oscillation period is about 20 seconds. What should she do systematically, and what is she likely to find?

**Correct Answer:**  
**Systematic approach to a loop that oscillates continuously after an upgrade:**

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Scoring Rubric:**
Full credit = MANUAL test first + valve stiction check + tuning assessment + upgrade-related changes (meter or positioner) as most likely source.

**Reference:** Kuphaldt LIII Ch.29, Ch.32

---

## IUK-T3-DIAG-084
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A custody transfer gas measurement station operates with a flow computer that calculates energy flow (BTU/hour) from: volumetric flow rate × pressure × temperature correction × energy content (BTU/SCF from online GC). Over a 6-month period, the monthly volumes are consistent, but the monthly energy totals vary ±4.5% from month to month with no clear relationship to flow. Diagnose.

**Correct Answer:**  
**Consistent volumes but variable energy totals (±4.5%) = the energy content (BTU/SCF from the GC) is the variable factor. Volume and flow correction are consistent — the GC heating value output is not.**

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Scoring Rubric:**
Full credit = GC BTU as the variable + real composition variation vs. calibration gas lot change as hypothesis + correlation analysis as verification.

**Reference:** AGA-5; AGA-3 (composition correction); GC calibration management best practices

---

## IUK-T3-DIAG-085
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A control valve on a compressed air system (instrument air header, 100 PSIG) makes a loud, continuous squealing noise at approximately 35% open and above. Below 35% open, the noise stops. The valve is a 2-inch globe valve with a cage-guided trim. The downstream pressure is 60 PSIG. Diagnose.

**Correct Answer:**  
**Loud squealing noise from a compressed air control valve at high openings, stopping at low openings = aerodynamic noise/vibration in the valve.**

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Scoring Rubric:**
Full credit = aerodynamic acoustic resonance in cage trim + velocity-dependent mechanism + below-35% explanation + remediation options.

**Reference:** Kuphaldt LIII Ch.32; ISA-75.17 (Control Valve Aerodynamic Noise); Fisher/Emerson noise abatement trim documentation

---

## IUK-T3-DIAG-086
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A fire and gas system gas detector (catalytic bead type, measuring % LEL) has been in service for 4 years. During a bump test (exposing it to a known 50% LEL gas mixture), the detector responds but only reads 32% LEL instead of the expected 45–55% LEL range. The detector has been passing its monthly bump tests for the past year as "response detected" (pass/fail, no magnitude check). What is the condition of this detector and what are the implications?

**Correct Answer:**  
**A catalytic bead detector that responds to a 50% LEL bump test gas but reads only 32% is showing SIGNIFICANT SENSITIVITY LOSS — it has lost approximately 36% of its calibrated sensitivity.**

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Scoring Rubric:**
Full credit = catalyst poisoning mechanism + 36% sensitivity loss calculation + safety margin reduction + bump test inadequacy critique + required actions.

**Reference:** ISA-12.13.01 (performance requirements for combustible gas detectors); OSHA 1910.119; catalytic sensor maintenance literature

---

## IUK-T3-DIAG-087
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A refinery has two identical level transmitters (LT-101 and LT-102) installed on opposite sides of a large crude oil storage tank for redundancy. Both are DP type with open legs (no wet leg). LT-101 consistently reads 2.3 feet higher than LT-102 even though they are measuring the same liquid level. Both have been recently calibrated. No changes to the tank or process. Diagnose.

**Correct Answer:**  
**Two DP level transmitters on the same tank reading differently despite recent calibration = a systematic installation or configuration difference between the two transmitters.**

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Scoring Rubric:**
Full credit = tap elevation difference as primary + LRV misconfiguration as secondary + verification steps. "Calibration error" without specifying what was miscalibrated = partial.

**Reference:** Kuphaldt LIII Ch.6; API MPMS Chapter 3 (tank gauging)

---

## IUK-T3-DIAG-088
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A technician reports that a HART field communicator cannot communicate with a specific transmitter in the field, even though it communicates with all other transmitters on the same loop. He has verified the communicator is working, the loop is powered (24 VDC, 250Ω load), and the transmitter appears healthy (correct 4–20 mA output). The transmitter is a 5-year-old model. What are five possible reasons HART communication fails with this one transmitter?

**Correct Answer:**  
**Five possible reasons HART communication fails with one specific transmitter while the 4–20 mA works:**

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Scoring Rubric:**
Full credit = five valid causes with distinct mechanisms. Three causes = 55%.

**Reference:** FieldComm Group HART specification; Kuphaldt LIII Ch.14

---

## IUK-T3-DIAG-089
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A condensate recovery system uses a level control loop to maintain a receiver drum level at 50%. The control valve (LV) is throttling correctly and the level is stable at 50% during normal operations. At steam demand peaks (approximately 8 AM and 2 PM), the drum level suddenly drops to 5% within 2 minutes, the LV opens fully, the level slowly recovers over 20 minutes, and the cycle repeats. The receiver drum is appropriately sized for normal flow. Diagnose.

**Correct Answer:**  
**Sudden level drop at predictable peak demand times with slow recovery = the condensate generation rate during peaks exceeds the receiver's capacity to accept and redistribute the condensate — but the level drops, not rises, suggesting condensate is being consumed faster than it's being generated at the drum level.**

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Scoring Rubric:**
Full credit = peak demand → higher feedwater consumption → drum depleted + makeup valve capacity insufficient + sizing analysis as verification.

**Reference:** Kuphaldt LIII Ch.6, Ch.29; boiler feedwater system design

---

## IUK-T3-DIAG-090
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A PROFIBUS PA segment has 6 devices communicating normally. An instrument technician adds a 7th device (a new level transmitter) and connects it to the segment. After connection, all 6 original devices also lose communication, along with the new 7th. Communication can be restored only by disconnecting the new transmitter. The new transmitter is confirmed identical to two others already on the segment that are working. Diagnose.

**Correct Answer:**  
**Adding one new device takes down ALL devices on the segment — including the 6 that were working. Removing the new device restores all communication. The new device is identical to working devices.**

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Scoring Rubric:**
Full credit = address conflict as primary + PROFIBUS token-passing disruption mechanism + verification method (check address before connecting) + secondary causes mentioned.

**Reference:** PROFIBUS International; IEC 61158 PROFIBUS specification; Kuphaldt LIII Ch.14

---

## IUK-T3-DIAG-091
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A magnetic flowmeter on a water line reads correctly when the line is completely full. Periodically — always coinciding with low-demand periods overnight — the meter output drops to zero or becomes erratic for 1–3 hours, then recovers when daytime demand resumes. There is no low-flow cutoff configured. The pipeline is sloped slightly downward in the direction of flow. Diagnose.

**Correct Answer:**  
**Periodic, demand-dependent erratic output on a mag meter with no low-flow cutoff, on a downward-sloping line = the pipe is running partially empty during low-demand periods.**

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Scoring Rubric:**
Full credit = empty pipe condition + slope/demand mechanism + EPD confirmation + remedy with back-pressure or relocation. "Low-flow" as cause without empty-pipe mechanism = 40%.

**Reference:** Kuphaldt LIII Ch.7; Endress+Hauser Promag installation requirements; empty pipe detection documentation

---

## IUK-T3-DIAG-092
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A remote-seal differential pressure transmitter is used for level measurement on a hot process (operating at 200°C). The remote seal fill fluid is silicone oil. During winter, when ambient temperature drops below 5°C, the level reads approximately 12% LOW. The error disappears in summer. No physical changes were made. Diagnose.

**Correct Answer:**  
**Temperature-dependent level error with remote seal transmitter = fill fluid thermal expansion/contraction causing a zero shift.**

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Scoring Rubric:**
Full credit = fill fluid thermal expansion + asymmetric capillary exposure + insulation/heat trace remedy. "Calibration drift" without thermal mechanism = 30%.

**Reference:** Kuphaldt LIII Ch.6; Rosemount remote seal technical data; Emerson remote seal thermal effects bulletin

---

## IUK-T3-DIAG-093
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A guided-wave radar (GWR) level transmitter in a hydrocarbon vessel is measuring the interface between water (bottom, SG=1.0) and oil (top, SG=0.82). The transmitter is correctly configured for dual-interface measurement. After a process upset, operators add a chemical demulsifier that reduces the water/oil interface sharpness — creating a "rag layer" (emulsion) of intermediate density between the two phases. Describe how this affects the GWR measurement and what can be done.

**Correct Answer:**  
**GWR interface measurement depends on reflection from a dielectric constant discontinuity at the interface. The rag layer fundamentally changes this discontinuity.**

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Scoring Rubric:**
Full credit = dielectric discontinuity principle + rag layer weakens/broadens reflection + ambiguous interface position + at least two remediation options.

**Reference:** Kuphaldt LIII Ch.6; Emerson Rosemount 5300 GWR interface measurement documentation

---

## IUK-T3-DIAG-094
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A thermowell installed in a 6-inch steam header running at 650°F and 450 PSIG fails — the thermowell stem fractures at the weld joint to the flange, releasing steam. Prior to failure, there were no reported measurement problems and no maintenance had been done. The thermowell had been in service for 8 years. Explain the probable failure mechanism.

**Correct Answer:**  
**Thermowell stem fracture at the weld after 8 years of service on a high-velocity steam line = Von Kármán vortex-induced fatigue failure.**

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Scoring Rubric:**
Full credit = Von Kármán vortex shedding + resonance mechanism + weld fatigue + ASME PTC 19.3 TW as the missed design check.

**Reference:** ASME PTC 19.3 TW-2016; Kuphaldt LIII Ch.8; ASME B31.3

---

## IUK-T3-DIAG-095
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A capacitance level probe in a solvent storage tank (toluene, dielectric constant εr ≈ 2.4) reads correctly after commissioning. Six months later, moisture enters the tank (confirmed by lab analysis — water content is now 0.8% by weight). The level reading is now 35% HIGH compared to a tape measure. Explain the mechanism and calculate whether the direction of error is correct.

**Correct Answer:**  
**Capacitance level sensors measure the dielectric constant of the medium surrounding the probe. Water (εr ≈ 80) has a dramatically higher dielectric constant than toluene (εr ≈ 2.4).**

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Scoring Rubric:**
Full credit = dielectric principle + water increases εr + higher capacitance = reads HIGH (direction confirmed) + approximate magnitude consistent + remedy.

**Reference:** Kuphaldt LIII Ch.6; capacitance level probe application notes; dielectric constant of mixtures

---

## IUK-T3-DIAG-096
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A PT100 RTD in a high-vibration pump bearing area has been in service 2 years. It begins reading intermittently — sometimes jumping to open circuit (transmitter shows 4 mA fault-low), sometimes reading correctly, sometimes reading 150°C when the bearing temperature is known to be ~70°C. The intermittent pattern correlates with pump speed changes. Diagnose.

**Correct Answer:**  
**Intermittent RTD behavior correlating with pump speed = vibration-induced mechanical failure in the RTD element or its connection.**

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Scoring Rubric:**
Full credit = vibration-induced wire fatigue + three symptom pattern explained by partial fracture + calculation attempt + replacement and vibration-resistant design recommendation.

**Reference:** Kuphaldt LIII Ch.8; RTD vibration ratings; bearing temperature measurement application notes

---

## IUK-T3-DIAG-097
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
An orifice plate differential pressure flow meter is measuring steam flow. Over 3 months, the flow indication has been creeping upward by approximately 0.5% per week even though operations confirm the actual steam production (from boiler output tracking) has not increased. The transmitter calibration is verified correct. The impulse lines are not plugged. Diagnose.

**Correct Answer:**  
**Most likely cause: progressive fouling / deposit buildup on the orifice plate, not erosion.**

Reasoning:
- transmitter calibration is confirmed,
- impulse lines are clear,
- reading is drifting **upward** over time,
- actual steam production has not increased.

If the orifice bore were eroding larger, the DP for a given true flow would tend to **drop**, so the indicated flow would tend to go **down**, not up.

An upward drift points instead to the effective bore getting **smaller** or the plate behaving more restrictively over time. In steam service that is most consistent with **deposit buildup / fouling** on the plate or bore.

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Scoring Rubric:**
Full credit = DP increasing → bore narrowing → fouling deposits as cause + direction of error correctly reasoned + verification (visual inspection of plate).

**Reference:** Kuphaldt LIII Ch.7; ISO 5167; orifice plate fouling in steam service

---

## IUK-T3-DIAG-098
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A digital valve controller (DVC) performs an automatic commissioning stroke on a new installation. The auto-calibration reports SUCCESS. However, when the control system sends a 50% signal, the valve opens to approximately 72% position (per the DVC position feedback). At 0% signal, the valve fully closes correctly. At 100% signal, the valve fully opens correctly. Only mid-range positions are wrong. Diagnose.

**Correct Answer:**  
**Correct at 0% and 100%, wrong in the middle (72% instead of 50%) = the valve has a non-linear relationship between the DVC signal and actual position — and the DVC auto-calibration did not correct for it, or was configured for the wrong valve characteristic.**

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Scoring Rubric:**
Full credit = valve characteristic mismatch as primary + equal-percentage vs. linear explanation + mid-range error pattern correctly attributed + configuration check as solution.

**Reference:** Kuphaldt LIII Ch.32; Emerson DVC6000 configuration guide; ISA-75.25

---

## IUK-T3-DIAG-099
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A HART-enabled DP transmitter shows the following when interrogated: PV = 87.3 inH₂O, % Range = 87.3%, Sensor Temperature = 71°C, Output = 17.97 mA, Loop Current = 17.97 mA, Battery = N/A, Alarms = None. The operator says the flow is reading 50% higher than expected. The transmitter URL is 100 inH₂O. What is wrong?

**Correct Answer:**  
**Nothing is wrong with the transmitter. The HART snapshot is internally consistent. The problem is downstream in the flow calculation / display configuration.**

What the HART data proves:
- PV = **87.3 inH₂O**
- % Range = **87.3%**
- Output = **17.97 mA**

Those values match a correctly functioning 0–100 inH₂O transmitter.

So the only justified conclusion is:
- the transmitter is fine,
- the operator’s “50% high” complaint must be caused by the **flow computer / DCS configuration**.

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Scoring Rubric:**
Full credit = identifies transmitter as correct + error is in flow calculation/configuration + explains what specific configuration error causes over-reading. Blaming transmitter = wrong.

**Reference:** Kuphaldt LIII Ch.7; AGA-3; DCS flow configuration

---

## IUK-T3-DIAG-100
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A boiler drum level control loop uses a three-element control scheme: drum level (primary), steam flow (feedforward), and feedwater flow (inner loop). During a sudden large steam load increase, the drum level temporarily DROPS even though the three-element control is performing as designed. The operator calls this "wrong" and asks the instrument engineer to investigate. Is the operator correct? Explain what is happening.

**Correct Answer:**  
**The operator is WRONG. The temporary level drop is EXPECTED and CORRECT physics — this phenomenon has a name: "swell and shrink" (more specifically, "shrink" in this case).**

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Scoring Rubric:**
Full credit = swell/shrink correctly named and explained + bubble volume physics + three-element is working correctly + operator is wrong.

**Reference:** Kuphaldt LIII Ch.29; Boiler drum level control (Shinskey; ISA); ASME boiler engineering texts

---

## IUK-T3-DIAG-101
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
An ultrasonic clamp-on flow meter is installed on a 10-inch carbon steel pipe carrying crude oil. At installation, the meter was configured with the pipe wall thickness (0.365 inches), pipe OD (10.75 inches), and crude oil sonic velocity (1,350 m/s at operating temperature). The reading is 18% LOW compared to a DP orifice meter in the same line. The crude oil temperature is correct in the meter. Diagnose.

**Correct Answer:**  
**18% low on a clamp-on ultrasonic vs. an orifice plate meter — one or both are wrong. Clamp-on ultrasonics are sensitive to multiple configuration parameters.**

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Scoring Rubric:**
Full credit = pipe bore deposit as primary + sonic velocity mismatch as secondary + bore measurement as verification. Blaming orifice meter without analysis = 30%.

**Reference:** Kuphaldt LIII Ch.7; clamp-on ultrasonic installation guides (Siemens, GE Panametrics)

---

## IUK-T3-DIAG-102
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A control valve is installed with the flow direction REVERSED from what the valve body arrow indicates. The process engineer says "it works fine as long as it's throttling." An instrument engineer is concerned. Who is correct and why does the direction matter?

**Correct Answer:**  
**The instrument engineer is correct to be concerned — the process engineer's "it works fine throttling" is partially true but ignores important failure modes.**

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Scoring Rubric:**
Full credit = shutoff concern + flow force direction + fail-safe compromise + "works throttling" partial truth acknowledged. One concern = 40%.

**Reference:** Kuphaldt LIII Ch.32; ISA-75.01; control valve installation requirements

---

## IUK-T3-DIAG-103
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A new commissioning engineer connects a HART handheld to an IS (intrinsically safe) barrier — specifically, she clips the HART communicator probes across the barrier's FIELD SIDE (hazardous area terminals) rather than the SAFE SIDE (control room terminals). She gets no HART communication. Moving the probes to the safe side gives good communication. Why does the field-side connection fail?

**Correct Answer:**  
**HART communicators must be connected on the SAFE SIDE of a Zener IS barrier — not the field side. The failure is expected behavior, not a fault.**

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Scoring Rubric:**
Full credit = barrier series resistance blocks HART signal + correct practice (safe side only) + impedance reasoning. "IS barriers block all communication" (too broad) = 50%.

**Reference:** FieldComm Group HART specification; IS barrier installation and commissioning guides; ISA RP12.6

---

## IUK-T3-DIAG-104
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A batch reactor temperature controller uses a setpoint ramp generator to slowly increase temperature from ambient to 180°C over 4 hours. During the ramp, the controller is in AUTO and tracks the ramping setpoint well — typically 2–3°C below the ramp. At 155°C, the PV suddenly "sticks" — it continues reading 155°C for 20 minutes while the setpoint has moved to 165°C. Then the PV jumps to 168°C rapidly and resumes tracking normally. No alarms were generated. The reactor jacket is steam-heated. Diagnose.

**Correct Answer:**  
**The PV "sticking" at 155°C for 20 minutes during a temperature ramp then jumping to 168°C = a phase change event or a process-specific phenomenon causing the reactor contents to absorb heat without temperature increase, then release it.**

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Scoring Rubric:**
Full credit = latent heat / phase transition at 155°C + instrument is correct + temperature correctly reads phase transition temp + chemistry/process explanation needed. "Transmitter malfunction" = wrong.

**Reference:** Kuphaldt LIII Ch.8; batch process control; thermodynamics of phase transitions

---

## IUK-T3-DIAG-105
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
An oxygen analyzer (paramagnetic type) used for boiler flue gas measurement reads 5.2% O₂. A portable electrochemical cell analyzer inserted into the same flue gas stack simultaneously reads 3.8% O₂. Which is more likely correct, and what could explain the discrepancy?

**Correct Answer:**  
**Both readings are plausible, but the discrepancy of 1.4% O₂ is significant. Before declaring one wrong, the explanation for the gap must be established.**

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Scoring Rubric:**
Full credit = both hypotheses for each instrument + air infiltration as primary for paramagnetic + cell depletion for electrochemical + calibration check as resolution.

**Reference:** Kuphaldt LIII Ch.10; EPA Method 3A (oxygen measurement); paramagnetic analyzer maintenance

---

## IUK-T3-DIAG-106
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A control system uses a selector block that takes the LOWER of two flow measurements (FT-501 and FT-502) and sends that to a downstream controller. This is a "low select" configuration intended as a conservative flow protection strategy. An engineer reviewing the historian notices the selected flow has been oscillating between the two transmitter readings every few minutes for weeks. Neither transmitter shows any fault. The oscillation appears to have no process cause. What is happening and is it a problem?

**Correct Answer:**  
**Two transmitters switching selection in a low-select block every few minutes with no faults = "signal chattering" on the low select due to the transmitters' readings crossing each other repeatedly near the same value.**

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Scoring Rubric:**
Full credit = selection chattering at crossover + downstream control disturbance + diagnostic masking + hysteresis as remedy.

**Reference:** Kuphaldt LIII Ch.29; DCS selector block configuration; control system signal conditioning

---

## IUK-T3-DIAG-107
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A DP flow transmitter is installed on a water line with the HP tap on the LEFT side of the orifice plate and the LP tap on the RIGHT side (looking in the flow direction). Flow is from LEFT to RIGHT. The transmitter reads NEGATIVE (below 4 mA). Explain and provide the remedy.

**Correct Answer:**  
**The taps are described correctly, so the negative reading means the transmitter connections are reversed somewhere between the taps and the transmitter ports.**

For left-to-right flow through an orifice plate:
- the **left / upstream** tap should be the **high-pressure source**,
- the **right / downstream** tap should be the **low-pressure source**.

If the transmitter reads negative, the most likely field mistake is that the **HP tap line ended up on the transmitter LP port** and the **LP tap line ended up on the transmitter HP port**.

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Scoring Rubric:**
Full credit = reversed transmitter connections (HP/LP swapped at transmitter) as cause + remedy (swap connections) + commissioning verification.

**Reference:** Kuphaldt LIII Ch.7; 3-valve manifold connection guide

---

## IUK-T3-DIAG-108
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
After a plant turnaround, a pressure controller that was stable before the outage now has a sustained oscillation with a 6-minute period. The controller settings (Gain=1.2, Ti=3 min/repeat) were not changed. A new pressure transmitter was installed during the turnaround (same model, same calibrated range). The control valve was also rebuilt (same valve body, new trim and packing). Diagnose.

**Correct Answer:**  
**Sustained oscillation at exactly 6 minutes after a turnaround where both the transmitter AND the valve were replaced/rebuilt. The tuning didn't change. The process didn't change.**

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Scoring Rubric:**
Full credit = new packing friction → higher dead time → same tuning is now aggressive + integral period analysis (6 min ≈ 2 × Ti) + transmitter damping as secondary + remedy.

**Reference:** Kuphaldt LIII Ch.29, Ch.32; control valve packing break-in

---

## IUK-T3-DIAG-109
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A pneumatic differential pressure transmitter (old Foxboro 13A type, bellows-and-force-bar design) on an ammonia refrigeration compressor shows increasingly erratic output over time — drifting high for weeks, then self-correcting, then drifting again. Temperature in the instrument room is stable. No process changes. Diagnose this specific failure mode.

**Correct Answer:**  
**Foxboro 13A bellows-type pneumatic DP transmitter showing long-period drift-and-correct cycles on ammonia service = classic ammonia/seal oil migration into the bellows assembly.**

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Scoring Rubric:**
Full credit = ammonia/fluid interaction with bellows fill fluid + drift-correct cycle mechanism + replacement recommendation. "Calibration drift" without mechanism = 40%.

**Reference:** Kuphaldt LIII Ch.6; Foxboro 13A service manual; ammonia refrigeration instrument selection guides

---

## IUK-T3-DIAG-110
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A DCS historian shows that a temperature controller (TIC-201) output has been at 95–100% continuously for 72 hours while the process temperature is well above setpoint (SP=180°C, PV=210°C). The controller is REVERSE-acting. The output should be DECREASING when PV > SP. Why is the output at 100% and what is wrong?

**Correct Answer:**  
**Reverse-acting controller: PV > SP → output should decrease. But output is at 100% (maximum) for 72 hours while PV is well above SP = the controller is acting DIRECT instead of REVERSE, OR the controller is in a failed/forced state.**

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Scoring Rubric:**
Full credit = controller action misconfigured (direct vs reverse) as primary + positive feedback explanation + safety concern noted + verification method.

**Reference:** Kuphaldt LIII Ch.29; DCS controller configuration

---

## IUK-T3-DIAG-111
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A fieldbus (FOUNDATION Fieldbus H1) segment has 10 devices operating correctly. After a DCS server upgrade, all 10 devices still communicate, but their process values update in the DCS at a very slow rate — approximately one update every 45 seconds instead of the normal 1-second update. Describe what has changed and why.

**Correct Answer:**  
**All devices still communicate but update rate dropped from 1 second to 45 seconds after a DCS server upgrade = the MACROCYCLE time has been reconfigured or the segment's Link Active Scheduler (LAS) configuration has changed.**

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Scoring Rubric:**
Full credit = macrocycle concept explained + DCS upgrade reset/changed it + location of fix (FF segment configuration in DCS) + specific parameter to check.

**Reference:** FieldComm Group Foundation Fieldbus specification; DCS FF H1 configuration documentation

---

## IUK-T3-DIAG-112
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A pH measurement on a process stream reads 7.0 ± 0.1 consistently for two weeks — unusually stable for a process that typically varies between pH 5 and pH 9. The process engineer confirms the process chemistry should be producing significant pH swings. Diagnose.

**Correct Answer:**  
**pH reading perfectly stable at 7.0 for two weeks while the process should be producing pH swings = the pH electrode is DEAD — it is no longer responding to changes in hydrogen ion activity.**

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Scoring Rubric:**
Full credit = electrode dead + 7.0 = isopotential/zero mV + buffer test as confirmation + alarm blind spot identified.

**Reference:** Kuphaldt LIII Ch.10; pH electrode theory and maintenance; ISA-12.13 (pH measurement)

---

## IUK-T3-DIAG-113
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A 4-wire RTD PT100 is connected to a high-accuracy temperature transmitter. The transmitter reads 2.3°C HIGHER than a calibrated reference thermometer immersed at the same measurement point. HART verification shows the transmitter is reading the correct resistance from the RTD — the resistance matches what a 2.3°C-higher temperature should read. The calibration of the transmitter is verified correct. The RTD itself is newly calibrated. What could cause the RTD to read 2.3°C high?

**Correct Answer:**  
**Transmitter reads correct resistance, transmitter calibration correct, RTD is new and calibrated → the RTD is measuring the CORRECT TEMPERATURE — but it's measuring a temperature 2.3°C HIGHER than the process at the reference point.**

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Scoring Rubric:**
Full credit = RTD is accurately measuring its own temperature but not at the process bulk temperature + thermowell/insertion depth as primary + self-heating as secondary. "RTD calibration error" = wrong (stated it was newly calibrated).

**Reference:** Kuphaldt LIII Ch.8; IEC 60751; thermowell and RTD installation best practices

---

## IUK-T3-DIAG-114
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A "2-out-of-3" (2oo3) voted gas detector system in a compressor building annunciates an alarm when only ONE of the three detectors reaches the alarm setpoint. The other two detectors read zero. The SIS does not trip (trip requires 2oo3). The one alarming detector reads 35% LEL while the other two read 0% LEL. List five possible explanations for this discrepancy, from most to least likely.

**Correct Answer:**  
**One detector at 35% LEL while two adjacent detectors read zero — discrepancy diagnostic:**

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Scoring Rubric:**
Full credit = localized gas as #1 + four other valid causes in logical order + safety response noted. Starting with "false alarm" as most likely = fail for failing to protect safety.

**Reference:** ISA-12.13.01; Kuphaldt LIII Ch.10; gas detection system design

---

## IUK-T3-DIAG-115
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
An electrically-actuated control valve (motor-operated valve, MOV) is commanded to 60% open by the DCS. The motor position feedback reads 60%. However, when a technician visually inspects the valve handwheel position indicator, the disc appears to be approximately 90% open. The electrical position feedback uses a potentiometer attached to the motor actuator shaft. Diagnose.

**Correct Answer:**  
**MOV actuator position feedback reads 60% (motor shaft position) but actual disc position is ~90% — significant discrepancy.**

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Scoring Rubric:**
Full credit = coupling slippage between actuator shaft and valve stem + potentiometer on shaft only + safety implication + verification steps.

**Reference:** Kuphaldt LIII Ch.32; MOV actuator maintenance (Limitorque, Rotork documentation)

---

## IUK-T3-DIAG-116
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A plant's instrument air system normally operates at 100 PSIG supply with a minimum required pressure of 60 PSIG for all pneumatic instruments and control valves. A supply line leak drops the header pressure to 45 PSIG. Describe the cascade of instrument failures that will occur, in the order they occur, including both expected and unexpected consequences.

**Correct Answer:**  
**At 45 PSIG (below 60 PSIG minimum), a cascade of pneumatic failures unfolds:**

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Scoring Rubric:**
Full credit = staged cascade (positioning accuracy → fail-safe uncertainty → all-fail → air contamination) + safety implication that fail-safe may not be achieved at reduced pressure. Single "everything fails" = 40%.

**Reference:** Kuphaldt LIII Ch.32; instrument air system design; ISA S7.3 (quality of instrument air)

---

## IUK-T3-DIAG-117
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A newly hired instrument technician measures a thermocouple output in a process furnace and records 22.4 mV. She reports the temperature is 542°C based on looking up "22.4 mV" in the Type K thermocouple table referenced to 0°C. The actual furnace temperature (per an independent radiation pyrometer) is 519°C. The ambient temperature at the measurement point is 23°C. What did she do wrong and what is the correct temperature?

**Correct Answer:**  
**The technician forgot to apply cold junction compensation (CJC). She looked up the thermocouple millivolt output directly in the 0°C-referenced table — but the table assumes the reference junction is at exactly 0°C.**

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Scoring Rubric:**
Full credit = CJC not applied + correct procedure (subtract CJC EMF) + calculated result ~519–522°C.

**Reference:** Kuphaldt LIII Ch.8; NIST ITS-90 thermocouple tables; cold junction compensation

---

## IUK-T3-DIAG-118
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A level control loop (LIC) on a vessel is in AUTO. The level setpoint is 50%. The controller is P-only (no integral). The steady-state level is 47%. At this condition the controller output is 62%, and the process is stable. An operator increases the inlet flow by 15% (a load increase). After the loop re-stabilizes, the level is at 44% and the controller output is 72%. Explain what happened and whether the control is performing correctly.

**Correct Answer:**  
**Proportional-only controller with a load increase: both the level deviation and the controller response are expected and correct for a P-only controller.**

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Scoring Rubric:**
Full credit = P-only load disturbance offset explained + direction of error correctly traced + larger load = larger offset + P-only is correct behavior here.

**Reference:** Kuphaldt LIII Ch.29; P-only control steady-state offset theory

---

## IUK-T3-DIAG-119
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A safety instrumented function proof test requires the ESD valve to stroke fully closed within 3 seconds of receiving the trip signal. During the proof test, the valve takes 8.1 seconds to close. The valve is a 6-inch ball valve with a pneumatic quarter-turn actuator, spring return. Instrument air supply is 85 PSIG (normal). Diagnose the possible causes for the slow closure.

**Correct Answer:**  
**ESD valve closes in 8.1 seconds vs. required 3 seconds = closing speed is 2.7× too slow. This is a functional safety failure of the proof test.**

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Scoring Rubric:**
Full credit = proof test failure identified + four causes with speed control exhaust restriction as primary + immediate SIF failure consequence.

**Reference:** IEC 61511 proof test; ISA-84; actuator sizing and speed control documentation

---

## IUK-T3-DIAG-120
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
An instrument technician tests a Zener IS barrier and finds the following at the safe-side (input) terminals: 24.1 VDC no-load voltage. When the field-side transmitter is connected (normal operation), the safe-side voltage drops to 17.3 VDC and the barrier feels warm to the touch. The transmitter is drawing 18 mA. Is this normal? Diagnose.

**Correct Answer:**  
**Zener IS barrier analysis:**

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Scoring Rubric:**
Full credit = resistance calculation (~377Ω) + adequate transmitter supply confirmed + warmth indicating Zener conduction as abnormal + field-side fault investigation needed.

**Reference:** Kuphaldt LIII Ch.13; IS barrier entity parameters; ISA RP12.6; Stahl/MTL barrier documentation

---

## IUK-T3-DIAG-121
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A 4–20 mA pressure transmitter in a remote tank farm reads correctly at the local HART communicator (12.35 mA = 125.6 PSIG, verified against a test gauge). At the DCS 2,000 feet away, the same loop reads 11.87 mA (displaying 121.8 PSIG). The discrepancy is constant — always approximately 0.5 mA low at the DCS regardless of the actual pressure. No ground fault alarms. What is the cause and how do you confirm?

**Correct Answer:**  
**The 0.5 mA constant discrepancy between field and DCS readings indicates a parallel current path — current is leaking from the loop before reaching the DCS input card.**

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Scoring Rubric:**
Full credit = parallel current path / insulation leakage identified + constant offset explained + megger test as confirmation + cable damage as root cause. Blaming transmitter calibration = wrong (field reading is correct).

**Reference:** Kuphaldt LIII Ch.4; 4–20 mA loop troubleshooting; cable insulation testing

---

## IUK-T3-DIAG-122
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A VFD-controlled cooling tower fan motor draws rated current and runs at the commanded speed. The VFD has no faults. However, a vibration transmitter mounted on the motor bearing housing shows vibration at exactly 6× the motor running frequency, with amplitude increasing as VFD speed increases. At full speed (60 Hz, 1785 RPM), the vibration amplitude exceeds the alarm setpoint. The motor is a 6-pole induction motor. Diagnose.

**Correct Answer:**  
**The 6× running frequency vibration on a 6-pole motor points to an electrical excitation source — specifically, rotor slot passing frequency or stator slot harmonics interacting with the number of poles.**

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Scoring Rubric:**
Full credit = electromagnetic excitation identified (not purely mechanical) + pole count relationship + VFD harmonic interaction + diagnostic to distinguish electrical vs. mechanical source. Pure mechanical diagnosis (imbalance, looseness) = wrong.

**Reference:** IEEE 841 (motor vibration); VFD application guides; motor vibration analysis — electrical vs. mechanical sources

---

## IUK-T3-DIAG-123
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
An instrument technician performs a 5-point calibration on a 0–300 PSI pressure transmitter using a deadweight tester. The as-found results are:

| Applied PSI | Expected mA | Actual mA |
|---|---|---|
| 0 | 4.000 | 4.12 |
| 75 | 8.000 | 8.10 |
| 150 | 12.000 | 12.08 |
| 225 | 16.000 | 16.04 |
| 300 | 20.000 | 19.98 |

The technician says: "It's a zero shift — I'll trim the zero down by 0.12 mA and it'll be fine." Is this the correct diagnosis and remedy?

**Correct Answer:**  
**The technician's diagnosis of "zero shift only" is WRONG. The error pattern shows both a zero error AND a span error (or a nonlinearity), and a simple zero trim will not correct all five points.**

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Scoring Rubric:**
Full credit = zero + span error identified from the error pattern + correct two-step trim procedure + recheck after. "Zero only" diagnosis = 40%.

**Reference:** Kuphaldt LIII Ch.4; HART transmitter trim procedures; calibration best practices

---

## IUK-T3-DIAG-124
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A PLC program controls a batch mixing sequence. Step 3 opens valve MV-301 (mix valve) for 60 seconds, then closes it and proceeds to Step 4. The operator reports that sometimes Step 3 runs for exactly 60 seconds, but other times it runs for 120 seconds (exactly double). The PLC program has not been modified. The timer is a standard TON (timer-on-delay) set to 60,000 ms. Diagnose.

**Correct Answer:**  
**The doubling of timer duration (60s vs. 120s exactly) points to a PLC scan time or timer resolution issue — specifically, the timer may be incrementing TWICE per scan under certain conditions.**

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Scoring Rubric:**
Full credit = identifies timer execution rate as root cause (not a timer hardware fault) + subroutine/task execution explanation + diagnostic steps. "Timer is broken" = wrong.

**Reference:** Allen-Bradley/Rockwell PLC programming manual (task and timer execution); IEC 61131-3 timer behavior; PLC scan time fundamentals

---

## IUK-T3-DIAG-125
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A grounding problem is suspected in an instrument system. Three 4–20 mA transmitters share a common instrument junction box in the field. Transmitter A reads correctly. Transmitter B reads 0.3 mA high. Transmitter C reads 0.6 mA high. All three were calibrated last week and verified correct. The errors appeared after an electrician ran a new 480 VAC power cable through the same cable tray as the instrument cables. Diagnose and prescribe the fix.

**Correct Answer:**  
**The symptom pattern — different magnitude errors on three transmitters sharing a junction box, appearing after a power cable was added — is characteristic of ground loop current induced by electromagnetic interference (EMI) from the 480 VAC cable.**

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Scoring Rubric:**
Full credit = EMI from 480 VAC cable + induced current mechanism + different errors due to different loop areas/routing + rectification at poor connections + cable separation as primary fix. Blaming transmitter calibration = wrong (all were verified last week).

**Reference:** NEC Article 725; ISA RP12.6; Kuphaldt LIII Ch.4 (signal cable noise); EMI/RFI in instrument systems

---

## IUK-T3-DIAG-126
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A control valve on a steam letdown station (600 PSIG → 150 PSIG) has been in service for 3 years. Operators report increasing noise from the valve — a high-pitched screaming that occurs between 30% and 70% open, with maximum intensity at approximately 50%. Below 30% and above 70%, the noise is minimal. The downstream piping shows no visible damage. Diagnose the noise source and recommend a solution.

**Correct Answer:**  
**The noise pattern — maximum at mid-stroke, absent at low and high positions — combined with the high-pitched "screaming" character indicates aerodynamic noise from vortex shedding or cavity resonance within the valve trim, NOT cavitation (which is a liquid-service phenomenon).**

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Scoring Rubric:**
Full credit = aerodynamic resonance/vortex shedding (not cavitation — this is steam, not liquid) + mid-stroke velocity profile explanation + trim erosion as contributing factor + anti-noise trim recommendation. Diagnosing cavitation = wrong for steam service.

**Reference:** ISA-75.01; IEC 60534-8-3 (aerodynamic noise prediction for control valves); Fisher Control Valve Handbook (noise chapter)

---

## IUK-T3-DIAG-127
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A WirelessHART pressure transmitter on a remote wellhead has been reporting reliably for 14 months. Over the past two weeks, the update rate has degraded from 8 seconds to 30–60 seconds, and 5–10% of readings are now marked as "stale" in the DCS. Battery voltage (readable via the wireless gateway) is 3.4 V (fresh = 3.6 V, end-of-life = 2.7 V). No physical changes at the wellhead. Diagnose.

**Correct Answer:**  
**The gradual degradation of update rate with increasing stale data — while battery is still adequate — points to a wireless communication path problem, not a battery or transmitter failure.**

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Scoring Rubric:**
Full credit = RF path degradation (not battery) + environmental change as cause + mesh routing/packet loss mechanism + site inspection + gateway diagnostics. Blaming battery (3.4 V is adequate) = wrong.

**Reference:** IEC 62591 (WirelessHART); Emerson Wireless Application Guide; 2.4 GHz propagation characteristics

---

## IUK-T3-DIAG-128
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A motor-operated valve (MOV) on a large cooling water line is commanded to CLOSE from the DCS. The motor starts, draws current, and runs for 12 seconds — but the valve position feedback shows no movement (stays at 100% open). The motor is a 480 VAC 3-phase induction motor. The motor starter contactor engages (verified by indicator light). No motor overload trip. Diagnose.

**Correct Answer:**  
**The motor runs (draws current, no overload) but produces no valve movement — this means the motor is spinning but not driving the valve actuator mechanism.**

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Scoring Rubric:**
Full credit = coupling/gear failure as primary + motor direction as secondary + declutch as tertiary + current draw analysis to confirm no-load. Single cause without differential = 50%.

**Reference:** Limitorque actuator maintenance manual; MOV diagnostic procedures; NRC Generic Letter 89-10 (MOV testing — nuclear, but principles apply universally)

---

## IUK-T3-DIAG-129
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A technician calibrates a differential pressure transmitter for flow measurement (0–100 inH₂O, square root extraction enabled in the transmitter). At the calibration bench, she applies 25 inH₂O and expects 50% flow (since √(25/100) = 0.5 = 50%). The transmitter reads 50.0% — correct. She applies 50 inH₂O and expects 70.7% flow (√0.5 = 0.707). The transmitter reads 70.7% — correct. She returns the transmitter to the field. The DCS now reads 25% higher than before for the same process conditions. What happened?

**Correct Answer:**  
**The problem is DOUBLE square root extraction — the transmitter is applying square root internally AND the DCS is also applying square root to the 4–20 mA signal.**

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Scoring Rubric:**
Full credit = double square root identified + explains the math (√ applied twice = 4th root) + resolution (disable one). Blaming calibration error = wrong (calibration was verified correct in isolation).

**Reference:** Kuphaldt LIII Ch.7 (square root extraction); DP flow measurement configuration

---

## IUK-T3-DIAG-130
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A SIS logic solver performs a voted 2oo3 comparison on three temperature transmitters. The three readings are: TT-A = 412°F, TT-B = 413°F, TT-C = 389°F. The SIS does not trip (trip setpoint = 450°F). The process engineer says TT-C must be malfunctioning because it disagrees with A and B. Should TT-C be taken out of service for repair?

**Correct Answer:**  
**The process engineer's conclusion is premature and potentially dangerous. The fact that TT-C disagrees with TT-A and TT-B does NOT automatically mean TT-C is wrong.**

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Scoring Rubric:**
Full credit = does NOT assume majority is correct + common cause concern for A/B + independent reference required + danger of dropping to 2oo2. Agrees with engineer and removes C = safety-critical error.

**Reference:** IEC 61511; ISA-84; 2oo3 voting — majority is not always correct; common cause failure analysis

---

## IUK-T3-DIAG-131
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
An instrument air dryer (desiccant type, dual-tower regenerative) in an instrument air system has been performing normally for two years. Over the past month, instrument air dewpoint has been gradually rising from the normal −40°F to −10°F. No alarm has been generated because the dewpoint alarm setpoint is 0°F. The maintenance records show the desiccant was replaced 6 months ago. What is happening and what are the consequences if not addressed?

**Correct Answer:**  
**The gradual dewpoint rise indicates the desiccant dryer is losing drying capacity — the desiccant is not being fully regenerated during the regeneration cycle, resulting in progressively wetter outlet air.**

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Scoring Rubric:**
Full credit = regeneration cycle failure mechanism + gradual degradation explained + consequences (condensation → freezing → valve failures) + ISA-7.0.01 reference. Single cause without consequences = 50%.

**Reference:** ISA-7.0.01 (Quality Standard for Instrument Air); instrument air dryer maintenance; Kuphaldt LIII Ch.4

---

## IUK-T3-DIAG-132
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A control valve with a smart HART positioner (Fisher DVC6200) is commanding correctly — the DCS output matches the positioner input, and the positioner drives the valve to the commanded position. However, the valve diagnostic shows a gradually increasing "friction" value over 6 months. The valve has had no maintenance in that time. The positioner signature test shows the friction band widening from 2% to 8% of travel. What is happening, what are the consequences, and at what point does it require action?

**Correct Answer:**  
**The increasing friction trend is a valve packing degradation signature — the valve packing is hardening, swelling, or consolidating over time, increasing the force required to move the valve stem.**

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Scoring Rubric:**
Full credit = packing degradation mechanism + control performance consequences + threshold levels + packing adjustment as first action. "Replace the positioner" = wrong (positioner is compensating correctly — the valve mechanics are the problem).

**Reference:** ISA-75.25 (control valve positioners); Fisher DVC6200 diagnostics guide; Kuphaldt LIII Ch.32; Emerson ValveLink diagnostic trending

---

## IUK-T3-DIAG-133
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A DCS analog input card (16-channel, 4–20 mA) shows channels 1–8 reading correctly. Channels 9–16 all read exactly 4.000 mA regardless of actual transmitter outputs. The transmitters on channels 9–16 are all confirmed functional (HART communicator reads correct mA in the field for each one). No alarms on the AI card. What has failed?

**Correct Answer:**  
**The failure pattern — first 8 channels normal, second 8 channels all at exactly 4.000 mA — indicates a failure within the analog input card that affects only the second group of channels. This is characteristic of a failed multiplexer or A/D converter section on the card.**

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Scoring Rubric:**
Full credit = MUX failure affecting second bank of 8 channels + card architecture explanation + 4.000 mA as valid-but-wrong reading + card replacement. "Wiring problem" = wrong (all 8 channels simultaneously reading the same value rules out individual wiring faults).

**Reference:** DCS analog input card architecture; Honeywell/Emerson/Yokogawa AI card specifications

---

## IUK-T3-DIAG-134
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A calibration laboratory discovers that its deadweight tester (the primary pressure reference standard) has been used for the past 6 months with an expired calibration certificate. The tester was last calibrated 18 months ago against a NIST-traceable reference and was within specification at that time. During the past 6 months, 47 field transmitters were calibrated using this tester. What are the implications and what must be done?

**Correct Answer:**  
**This is a calibration traceability break — a serious quality system nonconformance that potentially affects the accuracy of all 47 transmitters calibrated during the expired period.**

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Scoring Rubric:**
Full credit = traceability break identified + not necessarily wrong (tester may still be in spec) + recalibrate tester first + as-found determines recall scope + NCR and corrective action. "All 47 must be immediately recalibrated" without checking the tester first = partial (premature — check the tester first).

**Reference:** ISO/IEC 17025; ISO 9001:2015 Clause 7.1.5 (monitoring and measuring resources); OSHA PSM (calibration records); NIST traceability requirements

---

## IUK-T3-DIAG-135
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A PLC-based emergency shutdown system (ESD) fails to trip during a proof test. The technician simulates a trip input by forcing the PLC digital input ON (via the programming software). The logic executes correctly and the output activates. But when the technician physically operates the field pressure switch (PSHH) at the process connection, the PLC input does NOT change state. The switch is confirmed to actuate mechanically (clicks). The wiring from the switch to the PLC input terminal is continuous (verified by ohmmeter with switch actuated). What is the remaining possible fault?

**Correct Answer:**  
**The switch actuates, the wiring is continuous, but the PLC input does not see the state change — this narrows the fault to the interface between the physical circuit and the PLC input detection.**

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Scoring Rubric:**
Full credit = voltage threshold vs. actual circuit voltage as root cause + why continuity ≠ adequate voltage + at least two specific mechanisms + voltmeter at PLC terminal as diagnostic. "Wiring is good so it must be the PLC" = insufficient without voltage analysis.

**Reference:** PLC digital input specifications (Allen-Bradley, Siemens, Schneider); IEC 61131-2 (PLC input thresholds); field wiring and voltage drop calculations

---

## IUK-T3-DIAG-136
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A refinery crude unit has a level transmitter (DP type) on a heavy crude oil separator operating at 350°F. The level reads correctly in summer. Every winter (ambient temperature below 20°F), the level reading gradually drifts 10–15% HIGH over a period of hours after ambient temperature drops. When ambient temperature rises, the reading returns to normal. No maintenance is performed during these events. Diagnose.

**Correct Answer:**  
**The seasonal, temperature-dependent drift on a DP level transmitter in heavy crude service is characteristic of impulse line fluid viscosity/density change with ambient temperature.**

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Scoring Rubric:**
Full credit = impulse line fluid density change with ambient temperature + HP leg gets denser in cold = reads high + gradual change tracks thermal equilibration + heat trace or remote seals as solution. Blaming transmitter electronics drift = wrong (electronics have temperature compensation and would not produce a seasonal, directional drift correlated with ambient temperature).

**Reference:** Kuphaldt LIII Ch.6 (DP level measurement); impulse line installation best practices; remote seal applications

---

## IUK-T3-DIAG-137
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
An operator reports that a Modbus RTU serial communication link between a PLC and a remote I/O rack loses communication intermittently — approximately 2–3 times per day, each lasting 30–60 seconds before automatically recovering. The communication cable is RS-485, 3,000 feet, with a 120Ω termination resistor at each end. The problem started after a new VFD was installed near the midpoint of the cable run. Diagnose.

**Correct Answer:**  
**The timing correlation with VFD installation and the intermittent nature strongly indicate EMI from the VFD is corrupting the RS-485 serial communication.**

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Scoring Rubric:**
Full credit = VFD EMI as cause + common mode noise mechanism on RS-485 + cable separation as primary fix + at least two other remediation options. "Replace the cable" without EMI analysis = partial.

**Reference:** ISA RP12.6; Modbus serial communication; RS-485 application notes; VFD EMI mitigation best practices

---

## IUK-T3-DIAG-138
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A control valve positioner (HART/smart type) reports its supply air pressure as 58 PSIG. The instrument air header reads 85 PSIG. The positioner is connected to the air header through 200 feet of 3/8" OD copper tubing. The valve is a large 8-inch butterfly with a pneumatic spring-return actuator. When the valve is stroking, the positioner intermittently faults with "low supply pressure" and the valve stalls at approximately 70% open. When the valve is stationary, the positioner shows no fault. Diagnose.

**Correct Answer:**  
**The positioner supply pressure drops from 85 PSIG (header) to 58 PSIG (at the positioner) ONLY during stroking — this is a dynamic pressure drop caused by the flow demand of the large actuator exceeding the supply capacity of the 200-foot tubing run.**

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Scoring Rubric:**
Full credit = dynamic pressure drop during flow demand + tubing undersized for actuator volume + spring force exceeds actuator force at reduced pressure + volume booster or larger tubing as solution. "Air supply is low" without the dynamic vs. static distinction = partial.

**Reference:** ISA-75.25 (positioner supply requirements); Fisher Control Valve Handbook (actuator sizing and air supply); pneumatic tubing sizing for actuators

---

## IUK-T3-DIAG-139
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A plant has eight identical temperature transmitters (Type K TC, same model, same manufacturer) installed on a reactor. Seven of the eight pass their annual calibration within specification. The eighth (TT-408) consistently reads 4.2°F HIGH at every calibration point, every year, for three consecutive years. Each year, the technician trims the zero to correct it, and it drifts back to +4.2°F by the next annual calibration. The transmitter electronics have been replaced once (same result). Diagnose.

**Correct Answer:**  
**The consistent +4.2°F error that returns after every calibration, survives transmitter electronics replacement, and occurs on only one of eight identical installations — the fault is NOT in the transmitter electronics. It is in the thermocouple or the thermocouple installation.**

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Scoring Rubric:**
Full credit = extension wire type mismatch as primary cause + explains parasitic junction EMF mechanism + consistent with transmitter electronics replacement not fixing it + wire inspection as diagnostic. "Transmitter drift" = wrong (electronics were replaced).

**Reference:** Kuphaldt LIII Ch.8 (thermocouple extension wire); ASTM E230 (thermocouple wire specifications)

---

## IUK-T3-DIAG-140
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A safety PLC (SIS logic solver) has redundant power supplies (A and B) in hot standby. Power supply A fails. Power supply B immediately takes over and the SIS continues operating normally. No process impact. The maintenance supervisor says: "No impact — we'll replace A during the next scheduled maintenance window in three weeks." The instrument engineer disagrees. Who is correct?

**Correct Answer:**  
**The instrument engineer is correct. A failed redundant power supply must be treated as a significant safety system degradation — not a routine maintenance item that can wait three weeks.**

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Scoring Rubric:**
Full credit = redundancy is lost + PFD increase explained + MTTR from SIL calculation applies + compensating controls if not immediately repairable + IEC 61511 requirement. "No impact, schedule normally" = safety gate concern.

**Reference:** IEC 61511-1 Clause 16 (maintenance); ISA-84; SIS power supply redundancy requirements

---

## IUK-T3-DIAG-141
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A magnetic flowmeter on a chemical process line reads correctly when the process fluid is at room temperature (25°C). When the process heats up to 80°C during a batch reaction, the flow reading drifts HIGH by approximately 6%. The mag meter was calibrated with water at 25°C. The process fluid is a water-based chemical solution. Diagnose.

**Correct Answer:**  
**The 6% high reading at elevated temperature on a magnetic flowmeter is NOT a meter malfunction — it is caused by the temperature dependence of the fluid's electrical conductivity and the interaction with electrode impedance.**

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Scoring Rubric:**
Full credit = conductivity/electrode impedance interaction + temperature dependence + electrode fouling as specific mechanism + cleaning and recalibration as resolution. "Meter needs recalibration" without mechanism = partial.

**Reference:** Kuphaldt LIII Ch.7 (magnetic flowmeters); Endress+Hauser Promag application notes; electrode impedance in process fluids

---

## IUK-T3-DIAG-142
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A batch reactor uses a PID controller with automatic setpoint ramping. During a ramp from 120°C to 180°C at 1°C/minute, the PV tracks the ramp well until 155°C. At 155°C, the PV suddenly stalls — it remains at 155°C for 8 minutes while the SP continues ramping to 163°C. Then the PV jumps rapidly to 165°C and resumes tracking. The controller output during the stall period shows the output gradually ramping up from 72% to 100%. No alarms. The heating medium is steam. Diagnose.

**Correct Answer:**  
**The stall at 155°C with the controller output ramping to 100% indicates the heating system reached a capacity limit — the steam supply could not deliver enough heat to continue the temperature ramp at 155°C, and the controller saturated at 100% output trying to maintain the ramp.**

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Scoring Rubric:**
Full credit = endothermic event at 155°C as root cause + phase change/boiling point mechanism + controller saturation + integral windup causing overshoot after recovery. "Controller tuning problem" = wrong (tuning was fine above and below 155°C).

**Reference:** Chemical engineering batch processing; reactor temperature control; phase-change enthalpy effects on control

---

## IUK-T3-DIAG-143
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A Zener IS barrier (passive type) in a 4–20 mA loop to a Class I Division 1 transmitter is found during routine inspection to have its earth connection loose — the ground wire terminal screw is finger-tight but not properly torqued. The transmitter has been reading correctly for the past 2 years. The maintenance supervisor says: "It's been working fine — the ground doesn't matter for the 4–20 mA signal." Is the supervisor correct, and what are the implications?

**Correct Answer:**  
**The supervisor is WRONG — dangerously so. The ground connection on a Zener IS barrier is the MOST CRITICAL safety element of the entire intrinsic safety installation, and a loose ground is a major safety deficiency.**

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Scoring Rubric:**
Full credit = ground is the safety-critical element (not the signal path) + fault-condition-only function explained + IS certification voided by loose ground + <1Ω requirement + facility-wide inspection recommended. "Ground doesn't matter for 4–20 mA" = safety-critical error.

**Reference:** IEC 60079-14; ISA RP12.6; IEC 60079-25; Kuphaldt LIII Ch.13 (intrinsic safety)

---

## IUK-T3-DIAG-144
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
An orifice plate DP flow meter on a saturated steam line reads correctly at the design operating pressure of 150 PSIG. When the boiler load changes cause the steam pressure to drop to 80 PSIG, the flow reading (in lb/hr) becomes approximately 20% HIGH compared to the known steam production rate. The flow computer uses real-time pressure and temperature compensation. The DP transmitter is verified accurate. Diagnose.

**Correct Answer:**  
**The flow computer is using real-time pressure and temperature for density correction — but it may NOT be correctly handling the change in steam specific volume (density) for SATURATED steam at different pressures.**

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Scoring Rubric:**
Full credit = saturated steam density vs. pressure relationship + flow computer density correction method as fault + √ρ relationship in orifice equation + steam table calculation as resolution. "DP transmitter error" = wrong (transmitter verified accurate).

**Reference:** ASME MFC-3M (orifice metering); IAPWS steam tables; Kuphaldt LIII Ch.7 (steam flow measurement)

---

## IUK-T3-DIAG-145
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A plant has a cascade control system: outer loop is reactor temperature (TIC-201, reverse-acting), inner loop is cooling water flow (FIC-202, direct-acting). The outer loop has been tuned with Gain=1.2 and Ti=5 min/repeat. The inner flow loop is tuned with Gain=0.6 and Ti=0.3 min/repeat. The system works well during normal operation. During a feed rate increase (a measured disturbance), the temperature overshoots setpoint by 12°F before recovering. The plant manager says the outer loop needs more aggressive tuning. The instrument engineer says the INNER loop is the problem. Who is correct and why?

**Correct Answer:**  
**The instrument engineer is more likely correct. In a cascade system responding to a disturbance that enters at the outer (primary) loop, the inner loop speed is the limiting factor for disturbance rejection.**

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Scoring Rubric:**
Full credit = inner loop speed as bottleneck + outer loop aggressiveness would worsen performance + cascade tuning rule (inner 3–5× faster than outer) + specific inner loop tuning recommendation. Making outer loop more aggressive = wrong.

**Reference:** Kuphaldt LIII Ch.29 (cascade control tuning); Shinskey "Process Control Systems"; ISA PID tuning guidelines

---

## IUK-T3-DIAG-161
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A Coriolis mass flowmeter on a liquid hydrocarbon service shows mass flow reading of 450 kg/min with a density reading of 0.72 g/cc. The volumetric flow calculated from these values is 625 L/min. An ultrasonic meter in parallel measures 480 L/min. The Coriolis meter has been verified to be in good working order. What explains the discrepancy and which meter is more likely correct for volumetric flow?

**Correct Answer:**  
**The discrepancy likely arises from the Coriolis meter's density reading being offset from actual process density at current conditions.**

**Required Elements:**
- Identifies density error as root cause + calculates implied density from ultrasonic + entrained gas or composition hypothesis + concludes ultrasonic more reliable for volumetric.

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Reference:** Kuphaldt LIII Ch.7; Coriolis meter entrained gas effects; Micro Motion Coriolis troubleshooting

---

## IUK-T3-DIAG-162
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A pneumatically actuated fail-closed control valve responds sluggishly to controller output changes — it takes 45 seconds to fully stroke where previously it took 8 seconds. The supply air pressure is confirmed at 85 PSIG. The I/P transducer output is correct (verified with a gauge). The positioner feedback arm is intact and the positioner output gauge shows the correct pressure change. What is the most likely cause of the slow stroking?

**Correct Answer:**  
**Most likely cause: Restricted air supply or exhaust path between the positioner and the actuator — specifically, a choked or partially blocked tubing connection between positioner output port and the actuator cylinder.**

**Required Elements:**
- Flow restriction in positioner-to-actuator tubing identified + diagnostic logic (I/P → positioner output → actuator path) + volume flow/stroke time relationship + verification method.

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Reference:** Kuphaldt LIII Ch.32; ISA-75.25; Fisher control valve maintenance

---

## IUK-T3-DIAG-163
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
An online gas chromatograph (GC) on a natural gas pipeline reports methane content as 94.2 mol% and ethane as 8.7 mol%. The field technician says: "Those numbers look fine — about 103% total but the GC always runs a bit high." What is actually wrong and why is this a serious problem?

**Correct Answer:**  
**The GC analysis results are INVALID. A component sum exceeding 100% is physically impossible and indicates a calibration or calculation error — not normal operation.**

**Required Elements:**
- % identified as impossible + "GC always runs a bit high" as unacceptable explanation + cause analysis + custody transfer/billing implication.

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Reference:** AGA-5 (energy measurement); ISA-76 (GC calibration); GC peak integration fundamentals

---

## IUK-T3-DIAG-166
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A PROFIBUS PA segment powers 12 field instruments from a single segment coupler. During commissioning, all 12 instruments appear online and communicating. After three weeks, one instrument (a pressure transmitter) begins dropping off the segment intermittently — it appears, disappears, and reappears on the configuration tool. All other instruments on the segment remain stable. Voltage at the segment coupler is 24 VDC and coupler output current is within limits. What are three diagnostic steps specific to PROFIBUS PA that should be investigated?

**Correct Answer:**  
**Three PROFIBUS PA-specific diagnostic steps:**

1. **Verify the suspect instrument's spur connection and current draw:**
PROFIBUS PA instruments connect via short "spur" cables off the main segment trunk. Check:
   - The spur cable connection at both ends (T-connector or field barrier) for intermittent contact, corrosion, or loose termination
   - The instrument's current draw with a clamp meter or segment analyzer — an instrument drawing excessive current (due to a developing internal fault) can cause momentary voltage sag at the segment, causing it to drop off
   - Measure voltage AT the instrument terminal (not at the coupler) — excessive spur length or resistance may cause marginal voltage at the device

2. **Check PROFIBUS PA address conflict:**
Each PROFIBUS PA device must have a unique address (1–126). If during commissioning the suspect transmitter was given an address that conflicts with another device (or if a device was added later with the same address), devices will intermittently fail to communicate as the master polls each address — one device wins arbitration while the other loses. Verify all device addresses with the configuration tool and check for duplicates.

3. **Analyze the segment's electrical characteristics with a PROFIBUS PA analyzer:**
Use a bus monitor (e.g., ProfiTrace, Softing PA-System Tester) to capture the PROFIBUS PA waveform on the segment at the moment of the dropout:
   - Check signal voltage level (amplitude) at the suspect device spur
   - Check signal termination — missing or double termination at the segment ends creates reflections that can cause CRC errors and device timeouts
   - Check for jitter in the segment timing — external electromagnetic interference on the segment
   - Capture error counters for the specific device address — is it generating consistent CRC errors before dropping?

**Required Elements:**
- Three distinct PROFIBUS PA-specific steps (not generic). Spur/voltage issues + address conflict + electrical analysis with PA-specific analyzer tool.

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Reference:** Kuphaldt LIII Ch.14; PROFIBUS PA installation guidelines (PI); ProfiTrace diagnostic methodology

---

## IUK-T3-DIAG-167
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A level control loop on a surge tank uses a non-contacting radar level transmitter. The radar has been working well for 8 months. Suddenly, the reading becomes erratic — it alternates between 45% and 92% with no pattern, with transitions occurring 2–3 times per minute. The level is visually confirmed at approximately 60% (consistent). What are three technical causes specific to radar level measurement?

**Correct Answer:**  
**Three radar-specific causes of erratic alternating readings:**

1. **Multiple echo selection / false echo from vessel internals:**
Free-space radar transmitters emit a microwave beam that reflects from ANY surface in the beam's path. After 8 months, a buildup of material (scaling, coating, crystallization) on a vessel internal (an agitator shaft, a baffle, a nozzle near the radar) may have grown to the point where it returns a signal comparable in strength to the true liquid surface echo. The radar's echo selection algorithm alternates between the true surface echo and the false echo from the internal structure — producing the oscillation between two readings. Solution: map the false echo (tank mapping/echo suppression) in the radar configuration.

2. **Foam layer formation:**
If the process chemistry has changed (pH change, new product, different feed), foam may have developed on the liquid surface. Foam is a poor radar reflector (low dielectric constant) and can:
   - Alternate between the foam surface and the true liquid surface reflection
   - The foam may be building and collapsing at the 2–3 transitions/minute rate
   - Radar reads foam surface intermittently when foam is thick enough to reflect, then liquid surface when foam collapses

3. **Radar horn antenna contamination causing beam scatter:**
If material is coating the radar antenna (horn or lens), the beam pattern degrades — instead of a focused cone, the contaminated antenna produces a scattered pattern with significant energy directed at off-axis vessel walls. The radar alternates between the true surface return path and the wall-scattered return path, producing two distinctly different range readings. This would develop gradually (8 months of buildup) consistent with the timeline.

**Required Elements:**
- Three causes specifically linked to radar physics (false echoes, foam, antenna fouling) — not generic level measurement issues.

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Reference:** Kuphaldt LIII Ch.6; Endress+Hauser Micropilot radar troubleshooting; VEGA radar application notes

---

## IUK-T3-DIAG-168
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A fired heater tube skin thermocouple (Type K) reads 920°F. Operations is concerned because the process temperature entering the tubes is 650°F and the fired heater outlet design temperature is 780°F. The thermocouple was calibrated 6 months ago and was within spec. The burner firing rate is normal. What are three distinct diagnostic explanations — at least one of which should challenge the assumption that the thermocouple is correct?

**Correct Answer:**  
**Three explanations:**

**Required Elements:**
- At least one thermocouple challenge (Type K drift/contamination) + at least one valid physical explanation (flame impingement or coking) + technical mechanism for each.

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Reference:** Kuphaldt LIII Ch.9; API RP 573 (fired heater inspection); Type K thermocouple high-temperature drift

---

## IUK-T3-DIAG-170
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
An online pH measurement system on a wastewater neutralization process suddenly begins reading a stable 7.2 pH while the actual pH (confirmed by lab sample) is 4.8. The pH electrode has been in service for 4 months. The reference electrode is a double-junction type. What are three diagnostic hypotheses that could explain a "frozen" stable reading at 7.2?

**Correct Answer:**  
**Three hypotheses for a frozen/stable erroneous pH reading:**

1. **Reference electrode junction clogging — stable but wrong reference potential:**
The double-junction reference electrode maintains a stable reference potential by allowing a slow leak of electrolyte (typically saturated KCl or proprietary gel) through the junction. If the outer junction becomes clogged (by protein fouling, chemical precipitation, particulate bridging), the reference potential STABILIZES at a value determined by the composition of the clogged junction — it no longer responds to process pH changes. The measurement reads a fixed, stable value that represents the Nernst potential with the clogged junction acting as the reference — not the actual solution pH. The reading of 7.2 is coincidentally stable because the junction is stuck, not because the process is at 7.2.

2. **Glass electrode dehydration or protein fouling — loss of response:**
The pH-sensitive glass membrane requires a hydrated gel layer to function. If the electrode was temporarily exposed to a dehydrating agent (concentrated acid, strong base, or organic solvent), the glass membrane's response factor (Nernstian slope) may have degraded. The electrode may now read at or near its isopotential point (typically near pH 7) regardless of actual solution pH — producing a stable, stuck reading near the isopotential pH. This is consistent with the 7.2 reading (close to the isopotential point).

3. **Broken cable or corroded connection — transmitter reading reference voltage:**
If the glass electrode cable has developed an open circuit (broken inner conductor, corroded pin connection), the transmitter pH input loses the glass electrode signal and measures only the reference electrode potential against a floating input. The transmitter may default to or drift to a specific value near pH 7 (the isopotential point of the electrode pair calibration) — appearing as a stable, "normal" reading that does not respond to process changes.

**Required Elements:**
- Three technically distinct causes — reference junction plugging + electrode dehydration/loss of slope + open circuit/electrical — with mechanism for each.

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Reference:** Kuphaldt LIII Ch.10; pH measurement troubleshooting guides (Mettler Toledo, Hach); electrode maintenance procedures

---

## IUK-T3-DIAG-171
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A reactor batch process uses a PLC with a redundant 2oo2 CPU configuration. During a scheduled PLC firmware upgrade, maintenance applies the new firmware to CPU-A while CPU-B remains on the old firmware. After the upgrade, the PLC is returned to service. Three days later, the PLC intermittently locks up and requires manual reset. Operations says the PLC worked fine for years before the firmware upgrade. What has most likely occurred and what is the root cause?

**Correct Answer:**  
**Most likely cause: Firmware version incompatibility between the two CPUs causing redundancy communication protocol errors.**

**Required Elements:**
- Firmware mismatch as root cause + synchronization protocol incompatibility mechanism + intermittent nature explained + correct upgrade procedure.

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Reference:** Kuphaldt LIII PLC maintenance; Siemens/Allen-Bradley redundant CPU upgrade procedures; IEC 61131-3

---

## IUK-T3-DIAG-173
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A historian tag for a compressor suction pressure reads exactly 47.3 PSIG for 18 consecutive hours, then resumes normal variation. The process engineer says: "Compressor suction pressure was very stable that day — nothing unusual." The DCS operator agrees. Why should this exact stability raise concern, and what specifically should be investigated?

**Correct Answer:**  
**Exactly constant for 18 hours is a data quality red flag — real process variables fluctuate, even in "stable" conditions.**

**Required Elements:**
- Real process variables fluctuate — constant 18h reading is anomalous + substitute value/quality codes + simulation mode + historian compression — at least three.

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Reference:** Historian data quality codes (OSIsoft PI, Honeywell PHD); HART simulation mode; NAMUR NE 43; historian compression algorithms

---

## IUK-T3-DIAG-174
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A SIS 2oo3 voting logic for a high-high level trip (LAH-SIS) shows transmitters reading: LT-A = 94%, LT-B = 94%, LT-C = 42%. The SIS does not trip. LT-C alarm is acknowledged as "stuck low." The process engineer says: "Good — 2oo3 is working correctly, the trip correctly requires two of three to agree." Is this analysis correct? What is the actual SIS status?

**Correct Answer:**  
**The process engineer's conclusion that "the SIS is working correctly" is WRONG. The SIS is now in a degraded and potentially dangerous condition.**

**Required Elements:**
- oo3 degraded to effective 2oo2 + lost single-fault tolerance + IEC 61511 compensating measures + urgency of LT-C repair.

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Reference:** IEC 61511-1 Clause 16; ISA-84 degraded SIS operation; 2oo3 fault tolerance analysis

---

## IUK-T3-DIAG-176
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
During a compressor surge event on a centrifugal compressor, the anti-surge controller responds correctly and opens the recycle valve. However, the compressor shaft vibration (measured by proximity probes) shows three distinct frequency components: 1× running speed (3,600 RPM), 0.47× running speed, and a high-frequency component at 6.2 kHz. Describe what each vibration component indicates about the machine's condition.

**Correct Answer:**  
**Three frequency components — each with a distinct physical meaning:**

**Required Elements:**
- × = imbalance/bow/misalignment + 0.47× = oil whirl with mechanism and urgency + 6.2 kHz = bearing defect frequency or BPF with calculation approach.

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Reference:** API RP 670; Bently Nevada vibration analysis; Bernhard J. Hamrock "Fundamentals of Machine Elements"; subsynchronous instability in journal bearings

---

## IUK-T3-DIAG-177
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A FOUNDATION Fieldbus H1 segment has been stable for two years. After a minor software upgrade to the DCS host system, three of the eight devices on the segment begin reporting "Communication Fault — Scheduled Token Missing" errors intermittently. The other five devices are unaffected. What has most likely occurred and what should be investigated?

**Correct Answer:**  
**Most likely cause: The DCS host upgrade changed the LAS (Link Active Scheduler) configuration, disrupting the macrocycle schedule for the three affected devices.**

**Required Elements:**
- LAS macrocycle scheduling + CD token for affected devices + upgrade changed LAS schedule + investigation steps.

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Reference:** FieldComm Group FF H1 Technical Overview; DCS upgrade procedures for FF segments; Kuphaldt LIII Ch.14

---

## IUK-T3-DIAG-178
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A plant uses a HART multiplexer to poll 64 field devices for diagnostic data. After replacing the multiplexer with a new unit, operators notice 12 devices no longer respond to HART polling but continue to control normally via the analog 4–20 mA signal. The new multiplexer has been confirmed powered and connected correctly. What are three specific causes for devices to function on 4–20 mA but not respond to HART polling?

**Correct Answer:**  
**Three causes specific to HART communication failure despite working 4–20 mA:**

1. **New multiplexer default polling rate or retry count incompatible with slow HART devices:**
Different HART multiplexers have different timeout settings for waiting for device responses. Some field transmitters (particularly older HART 5 devices, intrinsically safe barrier-connected devices, or devices with high input filtering) respond more slowly than the new multiplexer's default timeout. The old multiplexer may have had extended timeouts; the new one uses a shorter default. The 12 non-responding devices may all be on IS barriers, have damping enabled, or be an older HART generation. Configure the new multiplexer with extended retry count and timeout for the affected devices.

2. **HART burst mode conflict:**
Some HART devices can be configured in "burst mode" — they continuously transmit HART data frames at a high rate (without being polled). If 12 devices are in burst mode, they may be transmitting continuously, which occupies the HART communication channel and prevents the multiplexer from inserting its poll commands at the correct gap. The new multiplexer may use a different burst-aware polling algorithm than the old one, causing poll conflicts with burst-mode devices. Disable burst mode on affected devices or configure the multiplexer for burst-mode compatibility.

3. **Multiplexer addressing — HART multi-drop mode conflict:**
In standard HART (point-to-point mode), the device address is 0 (polling address 0). In multidrop mode, each device has a unique HART address (1–15). If any of the 12 devices were previously configured in multidrop mode (address ≠ 0) and the new multiplexer is polling at address 0 only, it will not receive responses from the non-zero addressed devices. The 4–20 mA signal continues to work in multidrop mode (the current is fixed at 4 mA in multidrop — which may appear as normal "control" in some configurations). Verify the HART address of each non-responding device.

**Required Elements:**
- Three distinct HART-specific causes (timeout/retry + burst mode + HART address) with mechanisms.

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Reference:** FieldComm Group HART specification; HART multiplexer application notes; Pepperl+Fuchs HART Infrastructure

---

## IUK-T3-DIAG-179
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A distillation column overhead pressure controller (PIC-101) is struggling to hold setpoint — the pressure oscillates between 12 PSIG and 18 PSIG with a 22-minute period despite setpoint of 15 PSIG. The controller was retuned last week and performed correctly for 5 days. Today the oscillations began. The condenser coolant flow is confirmed stable. What should the engineer investigate first, and why might a properly tuned loop suddenly begin oscillating?

**Correct Answer:**  
**Primary investigation: Process gain change — not a controller tuning problem.**

**Required Elements:**
- Process gain change (not tuning) as primary hypothesis + specific causes (feed composition, coolant temperature, operating point, flooding) + 22-minute period consistency.

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Reference:** Kuphaldt LIII Ch.29; Shinskey "Distillation Control"; distillation process control dynamics

---

## IUK-T3-DIAG-300
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A DP transmitter on a steam flow orifice plate reads 22% higher than a recently calibrated portable ultrasonic clamp-on meter on the same line. The orifice plate was installed 3 years ago. Steam conditions are 150 PSIG saturated. Impulse lines are 10 feet long with condensate pots at both taps. What is the most likely cause and your diagnostic approach?

**Correct Answer:**  
**Most likely cause: a condensate-pot / impulse-line problem, not orifice-plate erosion.**

Why erosion is the wrong answer:
- If an orifice bore erodes larger, the **DP falls** for a given true flow
- A DP-based flow system would then tend to read **LOW**, not high

This problem is the opposite: the DP system reads **22% HIGH** versus the reference meter.

That points instead to the DP transmitter seeing **too much differential pressure**, most commonly because:
- the **LP impulse path is restricted**, or
- the **LP condensate pot / reference head is not behaving correctly** in steam service.

Either fault makes LP pressure at the transmitter lower than it should be, which inflates measured DP.

**Required Elements:**
- Identifies impulse line issue (not orifice erosion): mandatory
- Explains WHY erosion would read LOW not HIGH: bonus
- Condensate pot malfunction as specific mechanism: mandatory
- Systematic diagnostic sequence: mandatory

**Common Wrong Answers:**
- "Orifice plate erosion" — wrong direction; erosion → lower DP, not higher
- "Ultrasonic meter is wrong" — question states it was recently calibrated
- "Wrong DP range" — wouldn't cause a 22% consistent error

**Scoring Rubric:**
- Full (100%): Correct root cause + reasoning for why erosion is wrong direction + diagnostic sequence
- High (75%): Correct root cause + diagnostic sequence, doesn't address erosion misdirection
- Low (50%): Identifies impulse line issue but incomplete reasoning
- Minimal (25%): Generic troubleshooting without specific root cause
- Zero: States orifice erosion as cause

**Reference:** Kuphaldt LIII Ch.16 (Flow Measurement); ISA-RP31.1

---

## IUK-T3-DIAG-301
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A magnetic flow meter on a dilute sulfuric acid line (15% H₂SO₄) reads normally for the first 6 months after installation. Over the next 3 months, readings become increasingly erratic with random spikes and drops, though the process is steady. Physical inspection shows the exterior is undamaged. What is the most likely failure mode and why?

**Correct Answer:**  
**Most likely cause: Electrode coating or fouling.**

In dilute sulfuric acid service, electrochemical deposition can form insulating or semiconducting films on the wetted electrodes over time. This disrupts the voltage measurement across the flowing conductive liquid. The gradual onset (months) is characteristic of electrode fouling vs. sudden failures like liner damage.

**Required Elements:**
- Electrode fouling/coating identified: mandatory
- Gradual onset explained: mandatory
- Differentiation from liner failure: required for full credit
- Electrode resistance test: required for full credit

**Common Wrong Answers:**
- "Liner failure" — would be more sudden
- "Grounding issue" — would present from day one
- "Low conductivity" — H₂SO₄ at 15% is highly conductive
- "Air entrainment" — wouldn't develop progressively

**Scoring Rubric:**
- Full (100%): Electrode fouling + gradual onset reasoning + differential diagnosis + electrode resistance test
- High (75%): Correct root cause + some reasoning
- Low (50%): Mentions electrode issue but poor differential diagnosis
- Minimal (25%): Generic mag meter troubleshooting
- Zero: Wrong root cause

**Reference:** Kuphaldt LIII Ch.16; Emerson/Rosemount Magnetic Flow Meter Troubleshooting Guide

---

## IUK-T3-DIAG-302
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A guided wave radar (GWR) level transmitter in a condensate drum reads 8 inches higher than a local sight glass. The sight glass has been recently verified as correct. The probe is a coaxial type, installed vertically. The condensate temperature is 250°F. What is the most likely cause?

**Correct Answer:**  
**Most likely cause: Dielectric constant (Dk) mismatch at elevated temperature.**

GWR measures level by detecting the reflection of electromagnetic pulses at the liquid surface. The reflection strength depends on the dielectric constant of the liquid. Water's dielectric constant decreases significantly with temperature:
- Water at 68°F: Dk ≈ 80
- Water at 250°F: Dk ≈ 27

If the GWR was configured with Dk = 80 (ambient water), it may misinterpret the weaker reflection at 250°F. The transmitter's algorithm expects a stronger reflection — a weaker reflection can cause it to "look past" the true surface slightly or lock onto a secondary echo, reading high.

Additionally, condensate may have a different Dk than pure water due to dissolved gases and trace contaminants.

**Required Elements:**
- Dk temperature dependence identified: mandatory
- Direction of Dk change with temperature (decreases): mandatory
- Echo curve diagnostic recommendation: required for full credit
- Probe coating or foam as secondary consideration: bonus

**Common Wrong Answers:**
- "Sight glass is wrong" — question states it was recently verified
- "Probe damaged" — would cause erratic readings, not a consistent offset
- "Reference pulse issue" — typically causes complete failure or very large errors
- "Steam above liquid" — GWR propagation velocity in steam is nearly identical to air

**Scoring Rubric:**
- Full (100%): Dk temperature dependence + specific values/direction + echo curve diagnostic
- High (75%): Dk issue identified + direction correct
- Low (50%): Mentions GWR calibration but not specific mechanism
- Zero: Wrong root cause

**Reference:** Kuphaldt LIII Ch.15 (Level Measurement); Emerson GWR Application Guide

---

## IUK-T3-DIAG-303
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
An RTD temperature loop shows a reading of -22°F when the actual process temperature is 180°F. The transmitter is a 4-wire Pt100 RTD configuration. The loop was working correctly until a maintenance crew replaced cable in the junction box yesterday. What is the most likely cause?

**Correct Answer:**  
**Most likely cause: RTD lead wires connected to the wrong terminals — specifically, the sense (measurement) wires and excitation wires are swapped or one pair is open.**

In a 4-wire RTD configuration:
- Two wires carry the excitation current through the RTD element
- Two separate wires measure the voltage across the RTD element (Kelvin connection)

If the sense wires are inadvertently connected to the excitation terminals (or vice versa), or if one of the sense wires is open/disconnected, the transmitter reads the lead wire resistance instead of the RTD resistance. Since the lead wires have very low resistance compared to the RTD at 180°F (~169Ω for Pt100 at 180°F), the transmitter would interpret the low resistance as a very low temperature — hence the -22°F reading.

**Required Elements:**
- Miswired connection after maintenance identified: mandatory
- 4-wire RTD principle (excitation vs. sense) explained: mandatory
- Low resistance = low temperature indication mechanism: mandatory
- Terminal verification as first diagnostic step: required for full credit

**Common Wrong Answers:**
- "RTD element failed" — coincidence with cable replacement makes this unlikely
- "Open circuit" — most transmitters indicate upscale failure on open RTD, not -22°F
- "Wrong RTD type configured" — wouldn't produce such a large offset unless Pt1000 was used with Pt100 config

**Scoring Rubric:**
- Full (100%): Miswiring + 4-wire principle + resistance explanation + diagnostic sequence
- High (75%): Correct root cause + some reasoning
- Low (50%): Identifies wiring issue but can't explain mechanism
- Zero: Wrong root cause or ignores maintenance timing

**Reference:** Kuphaldt LIII Ch.14 (Temperature Measurement); IEC 60751

---

## IUK-T3-DIAG-304
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A control valve on a hot oil system (Therminol 66 at 550°F) is cycling ±8% around setpoint despite the PID controller being in manual mode at 50% output. The valve positioner confirms it is receiving a steady 12 mA signal. What is the most likely cause?

**Correct Answer:**  
**Most likely cause: Valve packing friction causing stick-slip cycling (stiction).**

If the controller is in MANUAL at a steady output, and the positioner confirms receiving a steady signal, the oscillation is downstream of the positioner — in the valve mechanical system. At 550°F, Therminol 66 is near its upper operating limit. The high temperature causes:

1. **Packing degradation:** PTFE or graphite packing hardens, cracks, or loses lubricity at elevated temperatures, increasing static friction
2. **Thermal expansion differential:** Stem, packing, and bonnet expand at different rates, changing packing compression
3. **Stick-slip mechanism:** Static friction (stiction) is higher than dynamic friction. The actuator builds force until it overcomes static friction, then the stem jumps. The positioner detects overshoot, reverses, and the cycle repeats

**Required Elements:**
- Stiction/packing friction identified: mandatory
- Manual mode = isolates controller as cause: mandatory
- Stick-slip mechanism explained: mandatory
- Valve signature test recommended: required for full credit

**Common Wrong Answers:**
- "PID tuning issue" — controller is in MANUAL, tuning is irrelevant
- "Positioner fault" — positioner confirms steady input signal
- "Process oscillation" — the valve is causing it, not responding to it
- "Electrical noise" — signal is steady per positioner

**Scoring Rubric:**
- Full (100%): Stiction + manual mode reasoning + mechanism + valve signature test
- High (75%): Correct root cause + manual mode logic
- Low (50%): Identifies valve issue but not specific mechanism
- Zero: Blames PID tuning or controller

**Reference:** Kuphaldt LIII Ch.25 (Control Valves); ISA-75.25 (Valve Diagnostics)

---

## IUK-T3-DIAG-305
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A 4–20 mA pressure transmitter reads 3.8 mA steady-state. The DCS shows "UNDER RANGE." The field wiring checks good, supply voltage at the transmitter is 22.5 VDC, and the process pressure gauge at the same tap shows 25 PSIG. The transmitter is calibrated for 0–100 PSIG (4–20 mA). What is the most likely cause?

**Correct Answer:**  
**Most likely cause: Transmitter sensing element failure or blocked process connection.**

At 25 PSIG on a 0–100 PSIG range, the expected output is:
Output = 4 + (25/100) × 16 = **8.0 mA**

The transmitter is outputting 3.8 mA — below the 4 mA live zero. This is a diagnostic signal: most modern transmitters are configured to drive below 3.8 mA (typically 3.6–3.8 mA) as a **downscale failure alarm** per NAMUR NE 43.

**Required Elements:**
- NAMUR NE 43 downscale failure alarm recognized: mandatory
- Sensor failure vs. wiring/power issue distinguished: mandatory
- HART diagnostic check recommended: required for full credit
- Process connection blockage as alternative: required for full credit

**Common Wrong Answers:**
- "Transmitter needs calibration" — 3.8 mA is a deliberate alarm signal, not drift
- "Loop power too low" — 22.5 VDC is adequate for modern transmitters
- "Zero shift" — a zero shift would still be above 4 mA unless massive

**Scoring Rubric:**
- Full (100%): NAMUR NE 43 + sensor failure diagnosis + HART check + process connection check
- High (75%): Recognizes below-4 mA as alarm + correct diagnosis
- Low (50%): Identifies fault but not NAMUR standard
- Zero: Suggests recalibration

**Reference:** NAMUR NE 43; Kuphaldt LIII Ch.12

---

## IUK-T3-DIAG-306
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A PID level controller on a horizontal separator maintains liquid level by throttling the outlet valve. During a process upset, the inlet flow rate triples. The level rises from 50% to 75% over 10 minutes, then stabilizes at 75% even though the setpoint remains 50%. The controller is in AUTO with Kp=2, Ti=5 min, Td=0. What is happening and why did the level stabilize above setpoint?

**Correct Answer:**  
**The controller has reached output saturation (100%) and cannot open the valve further — the process has exceeded the control valve's maximum capacity.**

**Required Elements:**
- Output saturation (100%) identified: mandatory
- Calculation showing output exceeds 100%: mandatory
- Self-regulating process explanation (higher head drives more flow): mandatory
- Integral windup recognized: required for full credit

**Common Wrong Answers:**
- "Controller found new equilibrium" — no, it's saturated and not controlling
- "Tuning is too conservative" — even aggressive tuning can't overcome valve capacity limit
- "Derivative action needed" — derivative doesn't help when capacity is exceeded
- "Transmitter error" — level genuinely stabilized at 75%

**Scoring Rubric:**
- Full (100%): Saturation + math showing >100% + self-regulation + windup
- High (75%): Saturation identified + self-regulation concept
- Low (50%): Identifies saturation but not process physics
- Zero: Doesn't recognize saturation

**Reference:** Kuphaldt LIII Ch.28–29; ISA Practical Process Control

---

## IUK-T3-DIAG-307
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A HART-enabled pressure transmitter communicates correctly when polled from the control room using a HART modem on the DCS terminals. However, a technician's handheld HART communicator at the field junction box cannot establish communication. The 4–20 mA signal reads correctly on the handheld's mA measurement function. What is the most likely cause?

**Correct Answer:**  
**Most likely cause: Insufficient loop resistance at the handheld's connection point.**

HART communication requires a minimum of 250Ω loop resistance between the communicator and the power supply. HART superimposes a ±0.5 mA FSK signal on the 4–20 mA current — this current modulation develops a voltage signal across the loop resistance that the communicator reads.

**Required Elements:**
- 250Ω minimum resistance requirement identified: mandatory
- Location of sense resistor relative to connection point explained: mandatory
- HART communication principle (FSK on current loop): mandatory
- Solution (add resistor or change connection point): required for full credit

**Common Wrong Answers:**
- "Handheld is defective" — mA measurement works, so handheld is functional
- "Wrong HART revision" — wouldn't prevent connection entirely
- "Transmitter HART disabled" — it communicates from control room
- "Wiring polarity" — HART is polarity-insensitive for communication

**Scoring Rubric:**
- Full (100%): 250Ω requirement + resistor location + FSK principle + solution
- High (75%): 250Ω issue + solution
- Low (50%): Mentions resistance but can't explain mechanism
- Zero: Wrong root cause

**Reference:** Kuphaldt LIII Ch.22 (HART Protocol); HART Communication Foundation

---

## IUK-T3-DIAG-308
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A Coriolis mass flow meter on a chemical feed line shows a reading of zero flow with a "drive gain high" alarm. The process is confirmed to be flowing (upstream and downstream indicators agree). The meter was working correctly until a plant shutdown/startup cycle yesterday. What is the most likely cause?

**Correct Answer:**  
**Most likely cause: Air or gas entrainment in the Coriolis tubes following the startup.**

During shutdown, the Coriolis tubes may have partially drained. During startup, if the system wasn't properly vented, air pockets become trapped in the measuring tubes. The air dramatically changes the vibration characteristics:

1. **Mass loading changes:** Air pockets reduce the effective mass in the tubes, altering the natural frequency
2. **Damping increases:** Gas-liquid interfaces absorb vibration energy
3. **Phase measurement corruption:** The tubes can't maintain symmetric vibration with slugs of air

The transmitter responds by increasing drive gain (power to the excitation coils) trying to maintain tube oscillation. When drive gain reaches maximum without achieving stable vibration, the meter alarms and reports zero flow.

**Required Elements:**
- Air/gas entrainment post-startup identified: mandatory
- Drive gain high mechanism explained: mandatory
- Startup timing correlation recognized: mandatory
- Venting as solution: required for full credit

**Common Wrong Answers:**
- "Tube failure" — would show vibration errors, not just drive gain high
- "Electronics failure" — wouldn't correlate with startup
- "Process viscosity change" — drive gain increase would be gradual
- "Wiring issue" — wouldn't cause drive gain alarm specifically

**Scoring Rubric:**
- Full (100%): Gas entrainment + drive gain mechanism + startup correlation + solution
- High (75%): Correct root cause + drive gain explanation
- Low (50%): Identifies gas entrainment but not mechanism
- Zero: Wrong root cause

**Reference:** Kuphaldt LIII Ch.16; Emerson Micro Motion Coriolis Troubleshooting

---

## IUK-T3-DIAG-309
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A PLC analog input card reads a consistent 20.00 mA from a pressure transmitter, but the transmitter's local display shows 72% of range and its loop current display shows 15.52 mA. All wiring has been checked and is correct. The DCS shows 100% pressure. What is the most likely cause?

**Correct Answer:**  
**Most likely cause: The PLC analog input channel has failed high (saturated at full scale).**

**Required Elements:**
- PLC input failure identified (not transmitter): mandatory
- Cross-verification logic between transmitter display and PLC: mandatory
- External current measurement at PLC terminals recommended: mandatory
- Spare channel swap as diagnostic: required for full credit

**Common Wrong Answers:**
- "Transmitter output stuck at 20 mA" — contradicted by transmitter's own display showing 15.52 mA
- "Scaling error" — 20 mA is exactly full scale, not a scaling offset
- "HART communication interference" — HART doesn't cause the analog reading to saturate

**Scoring Rubric:**
- Full (100%): PLC input failure + evidence analysis + external measurement + spare channel
- High (75%): Correct root cause + evidence reasoning
- Low (50%): Identifies PLC issue but weak reasoning
- Zero: Blames transmitter

**Reference:** Kuphaldt LIII Ch.21 (PLCs); PLC Analog Input Troubleshooting

---

## IUK-T3-DIAG-310
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
An ultrasonic level transmitter mounted on a tall atmospheric storage tank (40 ft, water service) suddenly begins reading 5 feet LOWER than the manual tape measurement. The error appeared overnight. Weather records show overnight temperature dropped from 75°F to 28°F. The instrument was calibrated at 70°F. What is the most likely cause?

**Correct Answer:**  
**Most likely cause: Speed of sound change in the cold air gap above the liquid.**

Ultrasonic level transmitters measure the time-of-flight of a sound pulse from the transducer to the liquid surface and back. The speed of sound in air varies with temperature:
- At 70°F (21°C): ~344 m/s (1129 ft/s)
- At 28°F (-2°C): ~332 m/s (1089 ft/s)

The transmitter was calibrated at 70°F. At 28°F, sound travels slower, so the echo takes longer to return. The transmitter interprets the longer transit time as a greater distance to the surface → **reads the surface as farther away → reports LOWER level**.

**Required Elements:**
- Speed of sound temperature dependence identified: mandatory
- Direction of error (reads low when cold) explained: mandatory
- Magnitude analysis showing temperature alone may be insufficient: bonus
- Ice/condensation on transducer as compounding factor: required for full credit

**Common Wrong Answers:**
- "Tank level actually dropped" — manual tape measurement contradicts
- "Foam on surface" — wouldn't appear overnight with temperature change
- "Electronics drift" — modern electronics don't drift 5 feet with 42°F change

**Scoring Rubric:**
- Full (100%): Temperature + speed of sound + direction + magnitude analysis + ice/condensation
- High (75%): Temperature effect + correct direction
- Low (50%): Mentions temperature but wrong direction or no mechanism
- Zero: Wrong cause

**Reference:** Kuphaldt LIII Ch.15 (Level Measurement)

---

## IUK-T3-DIAG-311
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A ladder logic program in a PLC controls a batch fill sequence. The sequence should: (1) open inlet valve, (2) wait for high level switch, (3) close inlet valve, (4) open outlet valve. The problem: the outlet valve opens simultaneously with the inlet valve at the start of the batch. The ladder logic has been reviewed and appears correct. What should you investigate?

**Correct Answer:**  
**Most likely cause: The high-level switch input is stuck in the active (tripped) state, or the switch contact is wired normally-closed when the logic expects normally-open (or vice versa).**

**Required Elements:**
- Switch wired wrong (NO vs NC) or stuck input identified: mandatory
- PLC input check with empty tank: mandatory
- NO vs NC wiring explanation: mandatory
- Systematic isolation (force input, step through logic): required for full credit

**Common Wrong Answers:**
- "Ladder logic error" — question states logic was reviewed and is correct
- "PLC scan time issue" — scan time doesn't cause simultaneous valve opening
- "Valve wiring issue" — both valves opening correctly, it's the SEQUENCE that's wrong
- "Timer malfunction" — there's no timer in the described logic (it waits for switch, not time)

**Scoring Rubric:**
- Full (100%): NO/NC mismatch + PLC input verification + systematic isolation
- High (75%): Switch state issue + PLC input check
- Low (50%): Identifies input issue but not specific mechanism
- Zero: Blames ladder logic without input investigation

**Reference:** Kuphaldt LIII Ch.21 (PLCs); IEC 61131-3

---

## IUK-T3-DIAG-312
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A pH analyzer on a wastewater neutralization system shows a steady reading of 7.0 pH regardless of changes in the influent pH (which varies from 2 to 12 based on upstream batch discharges). The analyzer was reading correctly last week. The reference electrode was replaced 2 months ago. What is the most likely cause?

**Correct Answer:**  
**Most likely cause: The reference electrode junction is blocked or the reference electrolyte (KCl) is depleted.**

A pH measurement system consists of a glass (measuring) electrode and a reference electrode. The glass electrode develops a voltage proportional to pH, and the reference electrode provides a stable half-cell potential for comparison. If the reference electrode fails:

**Required Elements:**
- Reference electrode junction failure identified: mandatory
- Isopotential point (7.0 = zero mV) explanation: mandatory
- Buffer test to confirm: required for full credit
- Impedance check: required for full credit

**Common Wrong Answers:**
- "Glass electrode broken" — a broken glass electrode reads erratic or upscale, not steady 7.0
- "Transmitter fault" — transmitter would show a diagnostic alarm, not steady 7.0
- "Process actually is pH 7" — question states influent varies from 2 to 12
- "Calibration drift" — drift would show a non-7.0 offset, not stick exactly at 7.0

**Scoring Rubric:**
- Full (100%): Reference junction + isopotential point + buffer test + impedance check
- High (75%): Reference junction + isopotential point
- Low (50%): Identifies reference electrode but not mechanism
- Zero: Blames glass electrode or transmitter

**Reference:** Kuphaldt LIII Ch.17 (Analytical Measurement); Emerson/Rosemount pH Troubleshooting

---

## IUK-T3-DIAG-313
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A 2-wire, loop-powered pressure transmitter on a FOUNDATION Fieldbus H1 segment works intermittently — it communicates for 5-10 minutes, then drops offline for 2-3 minutes, then reconnects. Other devices on the same segment work fine. Replacing the transmitter with an identical spare produces the same behavior. What is the most likely cause?

**Correct Answer:**  
**Most likely cause: Excessive cable resistance or a faulty spur junction in the field wiring specific to that device's connection.**

Since replacing the transmitter doesn't fix the problem, and other devices on the same segment work fine, the fault is in the infrastructure between the junction box and this specific device location.

**Required Elements:**
- Cable/wiring infrastructure issue (not device): mandatory
- Minimum voltage requirement (9 VDC) for FF H1: mandatory
- Voltage drop mechanism during communication: mandatory
- Voltage measurement at device terminals: required for full credit

**Common Wrong Answers:**
- "Defective transmitters" — two identical units show same behavior, rules out device
- "Segment termination" — would affect ALL devices, not just one
- "Fieldbus power supply issue" — other devices work fine
- "IP address conflict" — would cause communication errors, not regular cycling

**Scoring Rubric:**
- Full (100%): Cable resistance + voltage margin + cycling mechanism + terminal voltage measurement
- High (75%): Wiring issue + voltage requirement
- Low (50%): Identifies wiring but not specific mechanism
- Zero: Blames device or segment-wide issue

**Reference:** Kuphaldt LIII Ch.22; ISA-50.02 (FOUNDATION Fieldbus); IEC 61158-2

---

## IUK-T3-DIAG-314
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A vortex flow meter on a steam line reads 10–15% LOW compared to condensate flow measurements downstream (accounting for steam-to-condensate ratio). The meter has been in service for 5 years with no issues until a recent increase in operating pressure from 100 PSIG to 150 PSIG. What is the most likely cause?

**Correct Answer:**  
**Most likely cause: The vortex meter's K-factor or density compensation is not updated for the new operating pressure.**

Vortex meters measure volumetric flow by counting vortex shedding frequency (f). Mass flow requires density compensation:
- Mass flow = f × (1/K-factor) × ρ

When operating pressure increased from 100 to 150 PSIG:
- Steam density at 100 PSIG saturated ≈ 0.282 lb/ft³
- Steam density at 150 PSIG saturated ≈ 0.396 lb/ft³
- Ratio: 0.396/0.282 = 1.40 → 40% density increase

If the transmitter is still using the old density (or pressure/temperature compensation inputs are wrong), it underestimates mass flow because it's applying the old (lower) density to the measured volumetric flow rate. The actual mass flow is higher by the density ratio.

**Required Elements:**
- Density compensation mismatch identified: mandatory
- Density values at old vs new pressure: mandatory
- Mass flow = volumetric × density relationship: mandatory
- Pressure/temperature compensation verification: required for full credit

**Common Wrong Answers:**
- "Shedder bar damage" — would affect frequency, not density compensation
- "Condensate in steam line" — would cause erratic readings, not consistent 10-15% low
- "Reynolds number out of range" — possible but unlikely with only 50% pressure change
- "Pipe vibration" — would cause noise/erratic readings, not consistent offset

**Scoring Rubric:**
- Full (100%): Density compensation + values + mass flow relationship + verification steps
- High (75%): Density mismatch + correct direction
- Low (50%): Mentions pressure change but not density mechanism
- Zero: Wrong root cause

**Reference:** Kuphaldt LIII Ch.16 (Flow Measurement); ISA-RP31.1

---

## IUK-T3-DIAG-315
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A displacer level transmitter on a liquid propane (LPG) storage vessel reads erratically with a ±15% oscillation. The oscillation frequency is approximately 2-3 cycles per minute. The vessel is calm with no agitation. The displacer spring and torque tube were replaced 6 months ago. Temperature is 60°F, pressure is 125 PSIG. What is the most likely cause?

**Correct Answer:**  
**Most likely cause: Displacer resonance — the natural frequency of the displacer-spring-torque tube assembly matches a process-induced excitation frequency.**

At 125 PSIG and 60°F, liquid propane has a specific gravity of approximately 0.50 — much lighter than water. The buoyant force on the displacer is proportional to the fluid SG. With a light fluid:

1. The restoring force from buoyancy is weaker
2. The displacer mass remains the same
3. The spring constant of the torque tube is fixed
4. The natural frequency of the mass-spring system shifts

If the new torque tube (replaced 6 months ago) has a slightly different spring constant than the original, or if the displacer mass was changed, the natural frequency of the system may now coincide with:
- Compressor-induced pressure pulsations in the LPG vessel
- Flow turbulence from inlet nozzle
- Boiling/condensation at the liquid surface

The 2-3 cycles/minute oscillation is characteristic of mechanical resonance in a displacer system.

**Required Elements:**
- Mechanical resonance identified: mandatory
- Low SG effect on system dynamics: mandatory
- Torque tube replacement as trigger: mandatory
- Damping solution recommended: required for full credit

**Common Wrong Answers:**
- "Process boiling" — would be random, not regular 2-3 cpm oscillation
- "Torque tube leak" — would cause a steady offset, not oscillation
- "Density change" — density is constant at given T and P
- "Control valve cycling" — vessel has no level control described

**Scoring Rubric:**
- Full (100%): Resonance + SG effect + torque tube trigger + damping solution
- High (75%): Resonance identified + torque tube connection
- Low (50%): Identifies mechanical issue but not resonance
- Zero: Wrong root cause

**Reference:** Kuphaldt LIII Ch.15; Fisher/Emerson Displacer Level Transmitter Guide

---

## IUK-T3-DIAG-316
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A DCS trend shows that a temperature PID loop oscillates with a period of exactly 60 seconds. The oscillation amplitude is growing slowly. The controller settings are Kp=1.5, Ti=30 sec, Td=0. The valve responds correctly to manual changes. What is the specific tuning problem and what should be adjusted?

**Correct Answer:**  
**The loop is exhibiting integral-driven instability. The oscillation period of 60 seconds = 2× the integral time (Ti = 30 sec), which is a classic signature of integral-mode oscillation.**

**Required Elements:**
- 2× Ti period relationship identified: mandatory
- Growing amplitude = unstable (not critically tuned): mandatory
- Increase Ti as primary correction: mandatory
- Process time constant estimation method: required for full credit

**Common Wrong Answers:**
- "Reduce gain" — gain reduction helps, but the primary issue is integral; period = 2×Ti is the diagnostic clue
- "Add derivative" — derivative can help but is a band-aid; the integral time is fundamentally wrong
- "Valve stiction" — valve responds correctly to manual changes per question
- "Process disturbance" — growing oscillation is a tuning instability, not a disturbance response

**Scoring Rubric:**
- Full (100%): 2×Ti fingerprint + growing amplitude analysis + increase Ti + time constant method
- High (75%): Integral oscillation + correct fix
- Low (50%): Identifies tuning issue but not specific mechanism
- Zero: Blames valve or process

**Reference:** Kuphaldt LIII Ch.28–29; ISA Practical PID Tuning

---

## IUK-T3-DIAG-317
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A DP level transmitter on a closed pressurized vessel (100 PSIG nitrogen blanket) reads 15% higher than the actual level. The transmitter is calibrated correctly for the liquid SG (0.85) and the HP tap is at the bottom. The LP reference leg is filled with the same process liquid. The vessel temperature is 180°F, and the reference leg is exposed to ambient (70°F). What is the most likely cause?

**Correct Answer:**  
**Most likely cause: Density difference between the hot process liquid and the cooler reference leg liquid.**

The reference leg liquid is at 70°F (ambient) while the process liquid is at 180°F. Liquid density decreases with temperature. The reference leg liquid at 70°F is DENSER than the process liquid at 180°F.

**Required Elements:**
- Density difference between hot process and cold reference leg: mandatory
- Direction of error (reads HIGH) explained correctly: mandatory
- Hydrostatic pressure mechanism: mandatory
- Temperature compensation as solution: required for full credit

**Common Wrong Answers:**
- "Calibration error" — question states correctly calibrated
- "Reference leg leaking" — would cause readings to change as gas replaces liquid, typically reads high but not consistently
- "Nitrogen blanket pressure issue" — pressure cancels on both sides for a closed vessel

**Scoring Rubric:**
- Full (100%): Density difference + correct direction + mechanism + solution
- High (75%): Density issue + correct direction
- Low (50%): Mentions temperature but can't explain direction
- Zero: Wrong root cause

**Reference:** Kuphaldt LIII Ch.15 (Level Measurement)

---

## IUK-T3-DIAG-318
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A turbine flow meter on a clean water line reads normally at high flow rates (>80% of range) but reads 5-8% HIGH at low flow rates (<20% of range). The meter was recently recalibrated and the K-factor is correct at mid-range. What is the most likely cause?

**Correct Answer:**  
**Most likely cause: low-flow profile / swirl effects are biasing the rotor high, not bearing friction.**

Bearing friction would normally make a turbine meter read **low** at the bottom end of the range because the rotor would lag the flow. This problem is the opposite: it reads **high** at low flow.

That points instead to installation / profile effects that matter more at the low end:
- distorted velocity profile,
- residual swirl from upstream fittings,
- operation near the low-Reynolds-number limit of the meter.

Those effects can make the rotor see a locally higher tangential / centerline velocity than the true bulk-average flow, which biases the meter high.

**Required Elements:**
- Flow profile change at low Reynolds number: mandatory
- Center velocity vs average velocity in laminar vs turbulent: mandatory
- Upstream piping/swirl consideration: mandatory
- Flow conditioner as solution: required for full credit

**Common Wrong Answers:**
- "Bearing friction" — would cause reads LOW, not HIGH
- "Electronic noise" — would be random, not consistently high
- "Calibration error" — calibrated correctly at mid-range
- "Air entrainment" — would cause erratic readings, not consistent offset

**Scoring Rubric:**
- Full (100%): Flow profile/Reynolds number + velocity profile mechanism + swirl + solution
- High (75%): Correct root cause + direction reasoning
- Low (50%): Mentions Reynolds number but can't explain direction
- Zero: States bearing friction (wrong direction)

**Reference:** Kuphaldt LIII Ch.16 (Flow Measurement); AGA Report No. 7

---

## IUK-T3-DIAG-319
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A 24 VDC powered solenoid valve in a safety interlock circuit fails to de-energize when the PLC output turns OFF. The PLC discrete output card shows OFF (0 VDC at output terminals), but a multimeter at the solenoid measures 23.8 VDC. The solenoid coil resistance is 150Ω. What is the most likely cause?

**Correct Answer:**  
**Most likely cause: A sneak circuit — an alternative power path is energizing the solenoid through a parallel circuit that bypasses the PLC output.**

**Required Elements:**
- Sneak circuit / alternate power path identified: mandatory
- PLC output verified working (eliminated as cause): mandatory
- Wire disconnect test to confirm: mandatory
- Systematic wire tracing: required for full credit

**Common Wrong Answers:**
- "PLC output stuck ON" — verified OFF at terminals
- "Solenoid coil shorted" — a short would draw excess current but not create voltage
- "Back-EMF from solenoid" — back-EMF is a transient, not sustained 23.8 VDC
- "Measurement error" — 23.8 VDC is a real, sustained voltage

**Scoring Rubric:**
- Full (100%): Sneak circuit + evidence analysis + disconnect test + systematic tracing
- High (75%): Alternate power path + verification approach
- Low (50%): Recognizes power from elsewhere but vague on diagnosis
- Zero: Blames PLC or solenoid

**Reference:** Kuphaldt LIII Ch.21; IEC 61508 (wiring integrity)

---

## IUK-T3-DIAG-320
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A capacitance level probe in a diesel fuel storage tank reads full (100%) when the tank is known to be approximately 40% full. The probe was working correctly until the tank was cleaned and refilled with a different grade of diesel last week. What is the most likely cause?

**Correct Answer:**  
**Most likely cause: The new diesel grade has a significantly different dielectric constant than the previous grade, and the transmitter is not recalibrated.**

Capacitance level probes work by measuring the capacitance between the probe and the tank wall (or a reference probe). The capacitance depends on:
C = ε × A / d

Where ε (dielectric constant) of the fluid between the plates changes with level — air (ε ≈ 1) is replaced by liquid (ε > 1) as level rises.

**Required Elements:**
- Dielectric constant change with different fuel: mandatory
- Capacitance level measurement principle: mandatory
- Direction of error (higher Dk → reads high): mandatory
- Recalibration for new fuel: required for full credit

**Common Wrong Answers:**
- "Probe coated with residue from cleaning" — would typically cause a baseline shift, not read full
- "Tank grounding issue" — would affect the circuit but wouldn't cause a clean 100% reading
- "Water in diesel" — water has high Dk (~80) but would settle to the bottom, not cause uniform full reading
- "Electronics failure" — too coincidental with fuel change

**Scoring Rubric:**
- Full (100%): Dk change + measurement principle + calculation/magnitude + recalibration
- High (75%): Dk change + correct direction + recalibration
- Low (50%): Mentions dielectric but poor explanation
- Zero: Doesn't connect fuel change to measurement

**Reference:** Kuphaldt LIII Ch.15 (Level Measurement)

---

## IUK-T3-DIAG-322
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A control valve positioner shows 50% valve position when commanded to 50%, but the process (flow) does not respond proportionally — the flow is only about 20% of maximum despite the valve appearing half open. The valve trim is equal-percentage. Upstream and downstream pressures are normal. What is the most likely explanation?

**Correct Answer:**  
**This is NORMAL BEHAVIOR for an equal-percentage valve trim — not a fault.**

**Required Elements:**
- Normal equal-percentage behavior identified (not a fault): mandatory
- Equal-percentage characteristic explained: mandatory
- Approximate calculation showing ~14-20% at 50% travel: mandatory
- Installed vs inherent characteristic distinction: bonus

**Common Wrong Answers:**
- "Valve is stuck" — positioner confirms 50% position
- "Valve oversized" — sizing doesn't change the inherent characteristic
- "Incorrect positioner calibration" — positioner shows correct position
- "Partially plugged valve" — would affect all positions, not specifically match equal-percentage curve

**Scoring Rubric:**
- Full (100%): Normal behavior + characteristic equation + calculation + installed vs inherent
- High (75%): Correctly identifies as normal + explanation
- Low (50%): Mentions equal-percentage but can't demonstrate
- Zero: Diagnoses as a fault

**Reference:** Kuphaldt LIII Ch.25 (Control Valves); ISA-75.11 (Valve Characteristics)

---

## IUK-T3-DIAG-323
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A 4–20 mA loop has three devices in series: a 24 VDC power supply, a 2-wire transmitter, and a DCS analog input card (250Ω input impedance). The DCS reads 4.0 mA at zero, but at full range the reading is only 18.5 mA instead of 20 mA. A clamp-on ammeter at the transmitter confirms 20.0 mA output at full range. Where is the current going?

**Correct Answer:**  
**Most likely cause: A parallel resistance (current leak path) across the DCS input terminals or in the field wiring.**

**Required Elements:**
- Parallel resistance/leakage path identified: mandatory
- Current split calculation (KCL): mandatory
- Voltage-dependent leakage explanation (worse at high range): mandatory
- Insulation test recommended: required for full credit

**Common Wrong Answers:**
- "DCS input card fault" — reads correctly at 4 mA, so A/D conversion works
- "Transmitter range error" — clamp-on ammeter confirms 20 mA output
- "Wiring resistance" — series resistance would not create a current difference; it would only reduce loop voltage
- "Grounding issue" — a ground issue alone doesn't divert current

**Scoring Rubric:**
- Full (100%): Parallel path + KCL calculation + voltage-dependent mechanism + insulation test
- High (75%): Parallel path + calculation
- Low (50%): Identifies leakage but no analysis
- Zero: Blames transmitter or DCS card

**Reference:** Kuphaldt LIII Ch.12 (Instrument Signals); Ohm's Law / KCL

---

## IUK-T3-DIAG-324
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A Modbus RTU network has 15 slave devices on RS-485. Communication is stable with all 15 devices polling correctly. A new 16th device is added to the end of the bus. After adding it, devices 12–16 communicate intermittently while devices 1–11 work fine. The new device communicates correctly when tested standalone. What is the most likely cause?

**Correct Answer:**  
**Most likely cause: The bus termination resistor was on device 15 (the previous last device) and was not moved to device 16 (the new last device).**

**Required Elements:**
- Termination not moved to new end of bus: mandatory
- Signal reflection mechanism: mandatory
- Why near-end devices unaffected: mandatory
- Move termination + oscilloscope check: required for full credit

**Common Wrong Answers:**
- "Address conflict" — would affect only the conflicting devices
- "Cable too long" — adding one device doesn't dramatically increase length
- "New device is defective" — works correctly standalone
- "Too many devices" — RS-485 supports 32 devices (or 256 with high-impedance receivers)

**Scoring Rubric:**
- Full (100%): Termination + reflection + proximity explanation + diagnostic steps
- High (75%): Termination issue + solution
- Low (50%): RS-485 bus issue identified but not specific mechanism
- Zero: Wrong root cause

**Reference:** Kuphaldt LIII Ch.22 (Digital Communication); TIA/EIA-485

---

## IUK-T3-DIAG-325
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A differential pressure transmitter used for flow measurement on a clean water line shows a negative reading (-2 inH₂O) when the process is confirmed to be flowing at approximately 50% of design rate. The transmitter was zero-checked last month and was perfect. HP and LP impulse lines are intact and block valves are open. What is the most likely cause?

**Correct Answer:**  
**Most likely cause: the HP and LP connections are reversed.**

A forward-flow DP measurement should have:
- higher pressure at the upstream / HP tap,
- lower pressure at the downstream / LP tap.

If the transmitter shows a **negative DP** while the process is confirmed to be flowing forward, the most likely explanation is that the impulse lines are swapped.

**Required Elements:**
- Reversed HP/LP connections identified: mandatory
- Zero check passes with reversed connections explained: mandatory
- Direction logic (HP should always be higher during flow): mandatory
- Swap test as diagnostic: required for full credit

**Common Wrong Answers:**
- "Transmitter drift" — drift wouldn't cause a negative reading during confirmed flow
- "Blocked impulse line" — blocked line reads high (stale pressure), not negative
- "Process flowing backward" — question states forward flow confirmed
- "Orifice plate installed backward" — would still produce positive DP in flow direction

**Scoring Rubric:**
- Full (100%): Reversed connections + zero check explanation + direction logic + swap test
- High (75%): Correct root cause + direction reasoning
- Low (50%): Identifies connection issue but poor reasoning
- Zero: Wrong root cause

**Reference:** Kuphaldt LIII Ch.16 (Flow Measurement); ISA RP31.1

---

## IUK-T3-DIAG-327
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A pneumatic control valve with a diaphragm actuator fails to close completely — it stops at approximately 8% open when the signal is 3 PSI (closed position for an air-to-open valve). The valve was fully functional 3 months ago. Bench set is 3–15 PSI. The valve has PTFE packing. What is the most likely cause and what would you check first?

**Correct Answer:**  
**Most likely cause: Increased packing friction (packing tightened or degraded) preventing the actuator spring from fully seating the plug.**

For an air-to-open, spring-to-close valve:
- At 3 PSI signal, the diaphragm pressure is at minimum → the spring drives the valve closed
- The spring force must overcome both process forces AND packing friction to seat the plug
- If packing friction has increased (maintenance tightened the packing gland, PTFE cold-flowed under compression, or process conditions degraded the packing), the spring cannot generate enough force for the last 8% of travel

**Required Elements:**
- Packing friction increase identified: mandatory
- Spring force vs. stroke position (weakest at close): mandatory
- Bench test recommendation: mandatory
- Packing bolt torque check: required for full credit

**Common Wrong Answers:**
- "Positioner failure" — this is a pneumatic valve (3-15 PSI direct), may not have a positioner
- "Actuator diaphragm leak" — would cause the valve to close MORE (less air-to-open force)
- "Plug damage" — wouldn't cause repeatable stop at 8%
- "Wrong bench set" — was working 3 months ago with this bench set

**Scoring Rubric:**
- Full (100%): Packing friction + spring force analysis + bench test + packing torque
- High (75%): Correct root cause + bench test
- Low (50%): Identifies mechanical issue but vague
- Zero: Wrong root cause

**Reference:** Kuphaldt LIII Ch.25 (Control Valves); ISA-75.05 (Control Valve Terminology)

---

## IUK-T3-DIAG-328
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
An orifice plate DP flow measurement on a natural gas pipeline shows correct zero but reads approximately 3% HIGH compared to an inline ultrasonic meter during a calibration comparison. Both meters were recently calibrated against traceable standards. The gas composition is verified correct. Temperature and pressure compensation are enabled on both meters. The orifice plate has drain holes. What is the most likely cause of the 3% discrepancy?

**Correct Answer:**  
**Most likely cause: the drain hole is not doing its job because it is blocked or the plate is accumulating liquid at the bottom.**

Direction matters here:
- An **open** drain hole or bypass path would tend to reduce DP for a given total flow and drive the orifice meter **low**
- This meter is reading **high**, so the DP is higher than it should be

That points to **liquid accumulation / blocked drain-hole behavior** in a gas-service plate with drain holes. If condensate or debris blocks the drain path, the plate no longer behaves like the calculation basis, and the effective measured DP can be biased upward.

**Required Elements:**
- Drain hole blockage identified as cause of high DP: mandatory
- Understanding that an open drain hole would reduce DP (not increase): mandatory
- Liquid accumulation mechanism: mandatory
- Impulse line blowdown and drain hole inspection: required for full credit

**Common Wrong Answers:**
- "Open drain hole bypass" — this would cause LOW readings, not HIGH
- "Beta ratio mismatch" — both meters are calibrated and gas composition verified
- "Ultrasonic meter error" — question states both recently calibrated
- "Installation effects" — would not cause a clean 3% offset

**Scoring Rubric:**
- Full (100%): Blocked drain hole + DP direction analysis + liquid accumulation + inspection steps
- High (75%): Blocked drain hole + correct direction
- Low (50%): Mentions drain hole but wrong direction reasoning
- Zero: Wrong root cause

**Reference:** ISO 5167; AGA-3 (AGA Report No. 3); Kuphaldt LIII Ch.16

---

## IUK-T3-DIAG-330
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A radar level transmitter (FMCW type, 26 GHz) in a large atmospheric crude oil storage tank shows a "loss of echo" alarm intermittently. The alarm occurs primarily during tank filling operations but clears when filling stops. The tank has a floating roof. The radar antenna is a parabolic type mounted on a stilling well that extends from the tank top to near the bottom. What is the most likely cause?

**Correct Answer:**  
**Most likely cause: Turbulence from the filling operation creates surface agitation inside the stilling well, scattering the radar signal and preventing a clean reflection.**

During filling:
1. Oil enters the tank through inlet nozzles, creating turbulence
2. Even inside a stilling well, the liquid surface is not perfectly calm during filling — incoming flow creates waves and sloshing
3. A turbulent surface scatters the 26 GHz radar beam in multiple directions rather than reflecting it cleanly back to the antenna
4. The scattered signal is too weak for the transmitter to identify a valid echo → "loss of echo" alarm

**Required Elements:**
- Surface turbulence scattering radar signal: mandatory
- Low Dk of crude oil contributing: mandatory
- Filling correlation explained: mandatory
- Echo curve analysis or GWR alternative: required for full credit

**Common Wrong Answers:**
- "Floating roof blocking signal" — radar is in a stilling well, not exposed to roof
- "Antenna condensation" — wouldn't correlate with filling operations
- "Electronics overheating" — no correlation with filling
- "Tank vapor interference" — 26 GHz radar is not significantly affected by hydrocarbon vapors

**Scoring Rubric:**
- Full (100%): Turbulence + Dk + filling correlation + diagnostic steps
- High (75%): Turbulence + filling correlation
- Low (50%): Mentions surface issues but vague
- Zero: Wrong root cause

**Reference:** Kuphaldt LIII Ch.15 (Level Measurement); Emerson/VEGA Radar Application Guide

---

## IUK-T3-DIAG-331
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A dissolved oxygen (DO) analyzer on a boiler feedwater system reads 0 ppb consistently, but lab grab samples show 8 ppb. The analyzer was calibrated with a zero solution and a saturated air/water solution last week and passed. The probe is an electrochemical (galvanic) type. What is the most likely cause?

**Correct Answer:**  
**Most likely cause: The sample conditioning system is stripping dissolved oxygen before it reaches the analyzer probe.**

Common mechanisms:
1. **Excessive sample line length with small-bore tubing:** Stainless steel tubing at elevated temperature consumes dissolved oxygen through passive oxidation of the metal surface
2. **Sample cooler reducing DO:** As sample temperature drops from boiler feedwater temperature (~250°F) to analyzer operating temperature (~77°F), Henry's law changes — but DO should INCREASE with cooling, not decrease. So temperature alone doesn't explain zero reading.
3. **Most likely specific cause: The sample line has a leak or is exposed to chemical oxygen scavenger (hydrazine or DEHA) contamination from an adjacent sample point or shared sample header.**

If the sample system shares any tubing, valves, or headers with the boiler chemical feed system, trace amounts of oxygen scavenger could be reducing the DO to zero in the sample before it reaches the analyzer.

**Required Elements:**
- Sample conditioning issue (not probe failure): mandatory
- Either sample flow too low OR oxygen scavenger contamination: mandatory
- Galvanic probe oxygen consumption at low flow: mandatory for full credit
- Grab sample at analyzer inlet as diagnostic: required for full credit

**Common Wrong Answers:**
- "Probe membrane fouled" — fouled probe would read LOW but not exactly zero consistently
- "Calibration error" — calibration passed last week
- "Analyzer electronics fault" — would show diagnostic error, not clean zero
- "Process actually has zero DO" — lab samples show 8 ppb

**Scoring Rubric:**
- Full (100%): Sample conditioning + specific mechanism + flow rate + diagnostic steps
- High (75%): Correct root cause area + diagnostic approach
- Low (50%): Identifies sample system but not specific mechanism
- Zero: Blames probe or analyzer

**Reference:** ASTM D888; Hach/Endress+Hauser DO Analyzer Application Notes

---

## IUK-T3-DIAG-332
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A PLC-controlled batch mixing system uses a load cell to measure ingredient weight. The load cell system reads 500 lb when the hopper is empty (known tare weight is 500 lb). When 200 lb of material is added, the display shows 685 lb instead of 700 lb. When 400 lb is added, it shows 870 lb instead of 900 lb. The error is proportional to the net weight. What is the specific calibration problem?

**Correct Answer:**  
**The load cell system has a correct zero but incorrect span — the span calibration is low by approximately 7.5%.**

**Required Elements:**
- Span error identified (not zero error): mandatory
- Proportional error calculation (~7.5%): mandatory
- Multiple possible causes for span error listed: mandatory
- Certified test weight verification: required for full credit

**Common Wrong Answers:**
- "Zero offset" — zero is correct (reads 500 at tare)
- "Load cell overloaded" — errors are consistent and proportional, not non-linear
- "Temperature drift" — would affect both zero and span, not span alone consistently
- "Hopper binding" — would be inconsistent and position-dependent

**Scoring Rubric:**
- Full (100%): Span error + 7.5% calculation + causes + test weight verification
- High (75%): Span error + calculation
- Low (50%): Identifies calibration issue but not span-specific
- Zero: Identifies as zero error

**Reference:** Kuphaldt LIII Ch.13 (Force/Weight Measurement); NIST Handbook 44

---

## IUK-T3-DIAG-333
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A conductivity analyzer on a demineralized water system reads 0.5 µS/cm. The expected value for demininearlized water is <0.1 µS/cm. The analyzer was validated with a 1413 µS/cm standard solution and read correctly. The probe is a contacting (electrode) type. The sample system was recently modified to add CPVC sample tubing. What is the most likely cause?

**Correct Answer:**  
**Most likely cause: CO₂ absorption from the atmosphere through the new CPVC sample tubing or at a connection point.**

Demineralized water has extremely low ionic content and is highly sensitive to contamination. When CO₂ from ambient air dissolves in demin water:
CO₂ + H₂O → H₂CO₃ → H⁺ + HCO₃⁻

These ions increase conductivity. Even trace CO₂ absorption can raise conductivity from <0.1 µS/cm to 0.5 µS/cm or higher.

**Required Elements:**
- CO₂ absorption from atmosphere: mandatory
- CPVC connection to the problem: mandatory
- Why standard solution check didn't catch it: mandatory
- Grab sample at process tap as diagnostic: required for full credit

**Common Wrong Answers:**
- "Probe contamination" — probe validated with standard
- "Cell constant error" — validated against 1413 µS/cm standard
- "Ion leaching from CPVC" — CPVC doesn't significantly leach ions into demin water
- "Temperature compensation error" — 0.4 µS/cm offset is too large for temp comp error

**Scoring Rubric:**
- Full (100%): CO₂ absorption + CPVC link + standard solution logic + diagnostic
- High (75%): CO₂ absorption + CPVC link
- Low (50%): Identifies contamination but not specific mechanism
- Zero: Blames probe or analyzer

**Reference:** ASTM D1125; Kuphaldt LIII Ch.17 (Analytical Measurement)

---

## IUK-T3-DIAG-334
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A PLC ladder logic program controls three pumps (A, B, C) in a lead-lag-standby configuration. Pump A is lead, B is lag, C is standby. The logic should start B when level reaches 80% and start C only if level reaches 90% with both A and B running. The problem: when level reaches 80%, pump C starts instead of pump B. Pump B never starts. The PLC I/O is verified correct. What is the most likely logic error?

**Correct Answer:**  
**Most likely cause: The pump selector logic has swapped the output addresses for Pump B and Pump C, or the permissive conditions for B and C are reversed in the ladder logic.**

**Required Elements:**
- Transposed output addresses or permissive conditions: mandatory
- Systematic analysis of which conditions are met: mandatory
- Force test to differentiate logic vs wiring swap: mandatory
- Print/verify ladder logic against design: required for full credit

**Common Wrong Answers:**
- "I/O failure" — I/O verified correct per question
- "Level transmitter error" — if level is wrong, pump A wouldn't be running correctly either
- "PLC scan timing" — scan timing doesn't cause the wrong pump to start
- "Relay coil failure" — PLC outputs verified as correct at the card

**Scoring Rubric:**
- Full (100%): Transposed conditions/outputs + systematic analysis + force test
- High (75%): Correct root cause + one verification method
- Low (50%): Identifies swap but no verification approach
- Zero: Wrong root cause

**Reference:** Kuphaldt LIII Ch.21 (PLCs); IEC 61131-3

---

## IUK-T3-DIAG-335
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A 4–20 mA signal cable runs 1500 feet from a field transmitter to the control room. The cable is 18 AWG shielded twisted pair. The DCS reads 0.3 mA lower than the transmitter's local display at all signal levels. The discrepancy is constant from 4 mA to 20 mA. What is causing this and can you calculate the expected cable resistance?

**Correct Answer:**  
**This is not a cable-resistance problem. In a properly wired 4–20 mA series loop, the current is the same everywhere in the loop.**

For 18 AWG copper:
- about **6.4 Ω / 1000 ft**
- 1500 ft one way = 3000 ft round trip
- expected cable resistance ≈ **19.2 Ω**

At 20 mA that only causes a voltage drop of:
\[
0.020 	imes 19.2 = 0.384\,V
\]
It does **not** create a 0.3 mA current difference between one end of the loop and the other.

So a constant 0.3 mA discrepancy points to something else, such as:
1. **measurement / scaling mismatch** between the transmitter display and the DCS input,
2. **analog output trim or AI calibration error**, or
3. a **parallel leakage / ground-fault path** if the current has actually been verified with series meters at both ends.

The key lesson is the same: **simple loop resistance is not the cause**. The expected cable resistance is about **19.2 Ω**, and that affects voltage budget, not loop current equality.

**Required Elements:**
- Series resistance does NOT cause current loss (fundamental principle): mandatory
- Parallel leakage path identified: mandatory
- Cable resistance calculation (19.2 Ω): mandatory
- Insulation resistance test recommended: required for full credit

**Common Wrong Answers:**
- "Cable resistance causes 0.3 mA drop" — fundamentally wrong; current is the same in a series loop
- "Transmitter display inaccurate" — discrepancy is consistent across all levels
- "DCS input card error" — constant offset across all levels would be a scaling error, not 0.3 mA
- "Cable too long" — cable length causes voltage drop, not current loss

**Scoring Rubric:**
- Full (100%): Series current principle + leakage path + cable resistance calc + insulation test
- High (75%): Series principle correct + leakage identified
- Low (50%): Correct answer but attributes loss to cable resistance (common misconception)
- Zero: Claims cable resistance causes the current difference

**Reference:** Kuphaldt LIII Ch.12 (Instrument Signals); Ohm's Law / Kirchhoff's Laws

---

## IUK-T3-DIAG-336
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A pressure safety transmitter (SIL 2 rated) in a SIS loop performs an automatic self-test and reports "sensor integrity pass" but the field-verified pressure reading from a test gauge shows the transmitter is reading 15 PSI low. The transmitter was calibrated 6 months ago and was correct. How is this possible and what are the implications?

**Correct Answer:**  
**The self-test checks the electronics integrity and diagnostic coverage — it does NOT verify sensor calibration accuracy.**

Modern SIL-rated transmitters perform continuous self-diagnostics that check:
1. Electronics integrity (A/D converter, microprocessor, memory)
2. Communication integrity (HART/FF messaging)
3. Sensor circuit continuity (broken sensor wire detection)
4. Power supply adequacy

But the self-test CANNOT verify:
1. **Sensor drift** — if the sensing element (capacitive cell, piezoresistive element) has drifted, the electronics faithfully report the wrong value
2. **Process connection issues** — plugged impulse line, condensate accumulation
3. **Physical damage to sensing diaphragm** — shifted calibration due to overpressure event
4. **Fill fluid leakage** in remote seal systems

**Required Elements:**
- Self-test doesn't check sensor calibration: mandatory
- Distinction between electronic diagnostics and sensor accuracy: mandatory
- Functional safety implications (proof testing still required): mandatory
- Dangerous undetected failure category: required for full credit

**Common Wrong Answers:**
- "Self-test should have caught it" — self-test doesn't check calibration
- "Transmitter is defective" — electronics are working; sensor has drifted
- "The test gauge is wrong" — question states field-verified
- "HART polling error" — HART reads what the sensor reports; if sensor is drifted, HART reads drifted value

**Scoring Rubric:**
- Full (100%): Self-test limitation + sensor drift + safety implications + proof test reasoning
- High (75%): Self-test limitation + safety implications
- Low (50%): Identifies sensor drift but misses safety context
- Zero: Claims self-test should have caught it

**Reference:** IEC 61511; ISA-84.00.01; IEC 61508 (Diagnostic Coverage)

---

## IUK-T3-DIAG-337
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A thermal mass flow meter on a nitrogen purge line reads 30% higher than expected based on the flow control valve position and the known Cv. The meter was recently installed and calibrated using air as the calibration gas. What is the most likely cause?

**Correct Answer:**  
**Most likely cause: The thermal mass flow meter was calibrated on air but is measuring nitrogen — the gas correction factor was not applied.**

Thermal mass flow meters measure heat transfer from a heated element to the flowing gas. The heat transfer depends on the gas properties:
- Thermal conductivity
- Specific heat capacity (Cp)
- Density

Air and nitrogen have different thermal properties:
- Air: mixture of 78% N₂, 21% O₂, 1% Ar — has a higher thermal conductivity and slightly different Cp than pure N₂
- Nitrogen: pure N₂

The gas correction factor (K-factor) for nitrogen relative to air is approximately:
K_N₂/air ≈ 1.0 for some meter designs (since air is mostly N₂), but this varies by manufacturer and operating principle. For some thermal dispersion meters, the correction can be 0.95–1.05.

**Required Elements:**
- Gas correction factor / K-factor issue: mandatory
- Thermal mass flow measurement principle: mandatory
- Configured gas vs actual gas mismatch: mandatory
- Standard vs actual conditions as alternative: required for full credit

**Common Wrong Answers:**
- "Meter is broken" — newly installed and calibrated
- "Valve Cv is wrong" — Cv is a known value
- "Installation effects" — would not cause a consistent 30% offset
- "Temperature compensation" — most thermal mass meters have built-in compensation

**Scoring Rubric:**
- Full (100%): K-factor + measurement principle + configured gas check + standard conditions
- High (75%): K-factor issue + verification steps
- Low (50%): Mentions gas correction but can't explain magnitude
- Zero: Wrong root cause

**Reference:** Kuphaldt LIII Ch.16 (Flow Measurement)

---

## IUK-T3-DIAG-338
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A vibrating fork level switch on a liquid hydrocarbon tank fails to indicate when the level reaches the fork location. The fork is clearly submerged (visible through a sight glass) but the switch status remains "uncovered." The switch was tested on the bench with water and worked correctly. What is the most likely cause?

**Correct Answer:**  
**Most likely cause: The liquid hydrocarbon has a density and/or viscosity too low for the vibrating fork's detection threshold.**

Vibrating forks detect liquid by sensing the change in vibration frequency and amplitude when the fork is submerged. The frequency shift depends on the fluid's density and viscosity:
- Water: SG = 1.0, high viscosity relative to light hydrocarbons → large frequency shift → easily detected
- Light hydrocarbons (e.g., pentane SG = 0.63, hexane SG = 0.66): much lower density and viscosity → smaller frequency shift

If the vibrating fork's detection threshold was set or factory-configured for water or heavier fluids, it may not detect the frequency shift caused by a light hydrocarbon. The fork vibrates nearly the same in the light hydrocarbon as in air.

**Required Elements:**
- Low density/viscosity below detection threshold: mandatory
- Frequency shift mechanism: mandatory
- Water bench test irrelevance to light hydrocarbon service: mandatory
- Sensitivity adjustment or technology change: required for full credit

**Common Wrong Answers:**
- "Switch is defective" — bench test passed
- "Coating on fork" — would cause stuck-in-covered, not stuck-in-uncovered
- "Electrical wiring issue" — switch electronics work (reads "uncovered" actively)
- "Wrong mounting orientation" — forks work at any angle for liquid detection

**Scoring Rubric:**
- Full (100%): Density threshold + frequency mechanism + bench test logic + solution
- High (75%): Density threshold + solution
- Low (50%): Mentions density but not mechanism
- Zero: Wrong root cause

**Reference:** Kuphaldt LIII Ch.15; Endress+Hauser Liquiphant Application Guide

---

## IUK-T3-DIAG-339
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A 120 VAC powered instrument UPS system feeds 8 field instruments through a panelboard. After a brief power outage (500 ms), the UPS transfers to battery successfully and all instruments continue running. However, when utility power returns, 3 of the 8 instruments reboot spontaneously. The other 5 are unaffected. All instruments are the same model. What is the most likely cause?

**Correct Answer:**  
**Most likely cause: The UPS transfer from battery back to utility produces a voltage transient or brief interruption that exceeds the power supply hold-up time of 3 instruments but not the other 5.**

**Required Elements:**
- UPS transfer transient during return-to-utility: mandatory
- Component aging (capacitor degradation) as differentiator: mandatory
- Transfer time vs hold-up time comparison: mandatory
- Online UPS or power conditioning solution: required for full credit

**Common Wrong Answers:**
- "UPS failure" — UPS worked correctly (5 instruments fine)
- "All instruments should reboot" — component variation explains differential
- "Power surge damaged instruments" — instruments reboot and recover, not damaged
- "Ground loop" — wouldn't correlate with UPS transfer events

**Scoring Rubric:**
- Full (100%): Transfer transient + capacitor aging + comparison logic + solution
- High (75%): Transfer transient + differential explanation
- Low (50%): Identifies UPS transfer but not why only 3 affected
- Zero: Wrong root cause

**Reference:** IEEE 1100 (Emerald Book); NFPA 70 Article 700; UPS Application Guide

---

## IUK-T3-DIAG-340
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A control valve positioner (electro-pneumatic, 4–20 mA input) shows a split-range configuration: Valve A operates on 4–12 mA (fully open at 4, closed at 12) and Valve B operates on 12–20 mA (closed at 12, fully open at 20). At 12 mA, both valves should be closed. The problem: Valve A closes at 11.5 mA and Valve B opens at 12.5 mA, creating a 1 mA dead band where neither valve is active. What is the consequence and the fix?

**Correct Answer:**  
**Consequence: A 1 mA dead band (11.5–12.5 mA) where neither valve responds to the controller output.**

In this range:
1. The controller sees a process deviation and adjusts output
2. If the output is between 11.5 and 12.5 mA, NEITHER valve responds
3. The controller's integral term winds up trying to correct the deviation
4. When the output finally exceeds 12.5 mA (or drops below 11.5 mA), the valve jumps suddenly
5. This creates a **limit cycle**: the process oscillates around the transition point with the controller hunting through the dead band

**Required Elements:**
- Dead band consequence (cycling/limit cycle): mandatory
- Integral windup during dead band: mandatory
- Recalibration to eliminate dead band: mandatory
- Overlap preferred over dead band: required for full credit

**Common Wrong Answers:**
- "This is normal operation" — dead band in split range causes cycling
- "Increase controller gain" — makes the cycling worse
- "Add derivative action" — treats symptom, not cause
- "Replace positioners" — calibration issue, not hardware failure

**Scoring Rubric:**
- Full (100%): Dead band cycling + integral windup + recalibration + overlap principle
- High (75%): Dead band consequence + fix
- Low (50%): Identifies dead band but not consequence
- Zero: Doesn't identify the dead band issue

**Reference:** Kuphaldt LIII Ch.25, Ch.29; ISA-75.25

---

## IUK-T3-DIAG-341
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
An 802.3 Ethernet-based DCS network has 24 nodes on a single VLAN. Network performance is normal until a particular field device gateway (Modbus TCP gateway) is connected. After connection, all nodes experience intermittent communication delays of 500–2000 ms. Disconnecting the gateway immediately resolves the issue. The gateway's IP address is unique and does not conflict. What is the most likely cause?

**Correct Answer:**  
**Most likely cause: The Modbus TCP gateway is generating a broadcast storm — excessive broadcast or multicast traffic that floods the network.**

**Required Elements:**
- Broadcast storm / excessive broadcast traffic: mandatory
- Specific cause (ARP storm from misconfigured subnet, or network loop): mandatory
- Why all nodes affected (broadcast reaches everyone): mandatory
- Network analyzer as diagnostic: required for full credit

**Common Wrong Answers:**
- "IP address conflict" — question states address is unique
- "Bandwidth limitation" — 24 nodes on Ethernet is well within capacity
- "Gateway hardware failure" — disconnecting and reconnecting produces same behavior consistently
- "Firewall blocking" — firewalls block, not delay

**Scoring Rubric:**
- Full (100%): Broadcast storm + specific cause + all-nodes explanation + Wireshark diagnostic
- High (75%): Broadcast storm + diagnostic approach
- Low (50%): Identifies gateway is causing traffic issues but not specific mechanism
- Zero: Wrong root cause

**Reference:** IEEE 802.3; Kuphaldt LIII Ch.22; Industrial Ethernet Best Practices

---

## IUK-T3-DIAG-342
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A thermowell-mounted RTD in a 6-inch steam header reads 8°F lower than a bare thermocouple temporarily installed through a packing gland in the same pipe section. Both sensors have been bench-calibrated and are within specification. The steam velocity is approximately 150 ft/s. What is the most likely cause?

**Correct Answer:**  
**Most likely cause: Conduction error (stem loss) in the thermowell installation.**

A thermowell is a closed metal tube that protects the sensor from the process fluid. The temperature measured at the tip of the thermowell depends on:
1. Heat transfer FROM the process fluid TO the thermowell tip (convective)
2. Heat conduction ALONG the thermowell stem FROM the tip toward the cooler pipe wall (conductive loss)

The thermowell stem acts as a thermal fin — it conducts heat from the hot tip toward the cooler pipe wall/flange, reducing the tip temperature below the actual process temperature.

**Required Elements:**
- Stem conduction error (thermal fin effect): mandatory
- Heat transfer path explanation (convection vs conduction): mandatory
- Why bare TC doesn't have this error: mandatory
- Immersion depth or insulation as solution: required for full credit

**Common Wrong Answers:**
- "Thermocouple type error" — both sensors bench-calibrated
- "Velocity error" — at 150 ft/s, velocity-induced errors are typically <1°F for RTDs
- "Radiation error" — minimal in a pipe (enclosed environment)
- "Response time difference" — would matter for transients, not steady-state 8°F offset

**Scoring Rubric:**
- Full (100%): Stem conduction + heat transfer mechanism + bare TC comparison + solutions
- High (75%): Stem conduction + mechanism
- Low (50%): Mentions thermowell issue but not specific mechanism
- Zero: Wrong root cause

**Reference:** Kuphaldt LIII Ch.14 (Temperature Measurement); ASME PTC 19.3 TW (Thermowell Standard)

---

## IUK-T3-DIAG-343
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A pressure transmitter on a reactor vessel shows slow drift downward — 2 PSI per day — even though the reactor pressure is stable (verified by redundant transmitter and pressure gauge). The transmitter is a remote seal type with capillary fill fluid. The transmitter body is located 15 feet below the reactor tap point. What is the most likely cause?

**Correct Answer:**  
**Most likely cause: Fill fluid leaking from the remote seal capillary system.**

Remote seal transmitters use a fill fluid (typically silicone oil or fluorinated fluid) to transmit pressure from the process diaphragm seal to the transmitter sensing element through a capillary tube.

**Required Elements:**
- Fill fluid leak in capillary system: mandatory
- Hydrostatic head change mechanism: mandatory
- Downward direction explained (less fill fluid head): mandatory
- Cannot field-repair (factory return): required for full credit

**Common Wrong Answers:**
- "Sensor drift" — sensor drift is typically random, not linear 2 PSI/day
- "Process pressure dropping" — contradicted by redundant instruments
- "Temperature effect on fill fluid" — would cause cyclic daily variation, not linear drift
- "Impulse line issue" — this is a remote seal (no impulse line)

**Scoring Rubric:**
- Full (100%): Fill fluid leak + hydrostatic mechanism + drift direction + factory repair
- High (75%): Fill fluid leak + mechanism
- Low (50%): Identifies seal system issue but vague
- Zero: Wrong root cause

**Reference:** Kuphaldt LIII Ch.12; Rosemount/Yokogawa Remote Seal Application Guide

---

## IUK-T3-DIAG-344
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A function block diagram (FBD) in a DCS implements cascade control with a primary (master) temperature controller and a secondary (slave) flow controller. The cascade was stable for months. After a process change that increased the temperature setpoint by 50°F, the system oscillates wildly — the flow oscillates from 0% to 100% rapidly. What is the most likely cause?

**Correct Answer:**  
**Most likely cause: The primary controller's output range exceeds the secondary controller's setpoint range, causing the secondary controller to receive a setpoint outside its operational limits.**

**Required Elements:**
- Primary output driving secondary setpoint out of range: mandatory
- Integral windup on primary during large setpoint change: mandatory
- Cascading oscillation mechanism: mandatory
- Output limiting or setpoint ramping as fix: required for full credit

**Common Wrong Answers:**
- "Secondary controller tuning is wrong" — secondary was stable for months
- "Flow transmitter error" — transmitter hasn't changed
- "Valve stiction" — valve operating correctly, just being driven to extremes
- "Primary tuning is wrong" — tuning was correct for small disturbances; the issue is the large setpoint change

**Scoring Rubric:**
- Full (100%): Primary output range + windup + cascading mechanism + ramping/limiting fix
- High (75%): Primary driving secondary to extremes + fix
- Low (50%): Identifies cascade issue but not specific mechanism
- Zero: Blames secondary controller

**Reference:** Kuphaldt LIII Ch.29 (Cascade Control); ISA Practical Process Control

---

## IUK-T3-DIAG-345
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A differential pressure transmitter used for interface level measurement on a crude oil/water separator reads correctly when the water cut is 30% but reads 10% HIGH on the interface level when the water cut increases to 60%. The transmitter range and calibration have not changed. Why does the water cut affect the interface level reading?

**Correct Answer:**  
**The DP transmitter measures the TOTAL hydrostatic pressure differential between two taps. When the water cut changes, the average density of the mixed zone changes, which affects the total DP even if the interface position hasn't moved.**

**Required Elements:**
- Emulsion density change affecting DP: mandatory
- DP cannot distinguish interface position from density change: mandatory
- Hydrostatic pressure relationship explained: mandatory
- Alternative measurement technology recommended: required for full credit

**Common Wrong Answers:**
- "Interface actually moved" — question asks why WATER CUT affects reading, not why interface moved
- "Transmitter drift" — reading is correct at 30% cut
- "Temperature change" — not mentioned and wouldn't correlate with water cut
- "Reference leg issue" — reference leg is fixed

**Scoring Rubric:**
- Full (100%): Emulsion density + DP ambiguity + hydrostatic explanation + alternative technology
- High (75%): Density change + DP relationship
- Low (50%): Recognizes density is involved but can't explain mechanism
- Zero: Wrong root cause

**Reference:** Kuphaldt LIII Ch.15 (Level Measurement); API MPMS Ch.6

---

## IUK-T3-DIAG-346
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A 24 VDC instrument power supply feeds 12 instrument loops. The supply output reads 24.0 VDC. However, every 30 seconds, the output voltage dips to 21 VDC for approximately 200 ms, causing several transmitters to momentarily show diagnostic errors before recovering. The dip is regular and repeatable. What is the most likely cause?

**Correct Answer:**  
**Most likely cause: One of the 12 instrument loads has a periodic high-current draw that momentarily overloads the power supply or exceeds the supply's current capacity.**

**Required Elements:**
- Periodic high-current device causing bus voltage dip: mandatory
- 30-second periodicity as diagnostic clue: mandatory
- Identify candidate devices (solenoid, heater, analyzer): mandatory
- Isolation by disconnection as diagnostic: required for full credit

**Common Wrong Answers:**
- "Power supply failing" — output is stable except during periodic event
- "Ground fault" — ground faults don't produce regular 30-second periodic dips
- "Electromagnetic interference" — EMI doesn't cause regular supply voltage dips
- "Loose connection" — loose connections produce random, not periodic, disturbances

**Scoring Rubric:**
- Full (100%): Periodic load + 30-sec clue + candidate devices + isolation diagnostic
- High (75%): Periodic load + diagnostic approach
- Low (50%): Identifies current overload but not periodicity significance
- Zero: Blames power supply

**Reference:** Kuphaldt LIII Ch.12; ISA RP 12.6 (Power Distribution)

---

## IUK-T3-DIAG-347
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
An annubar (averaging pitot tube) flow meter on a 12-inch compressed air header reads correctly at high flows but reads 25% LOW at flows below 30% of range. The meter was installed 2 years ago and has not been recalibrated. The insertion depth was verified correct at installation. What is the most likely cause?

**Correct Answer:**  
**Most likely cause: The low-pressure (LP) sensing port on the annubar is partially plugged with particulate, moisture, or corrosion products.**

An annubar generates a differential pressure proportional to the square of velocity:
DP ∝ V²

At high flows: DP is large (e.g., 100 inH₂O at 100% flow)
At 30% flow: DP = 100 × (0.30)² = **9 inH₂O** — a very small DP

**Required Elements:**
- LP port plugging: mandatory
- Square-law amplification of bias at low DP: mandatory
- Compressed air contaminants identified: mandatory
- Blowdown procedure: required for full credit

**Common Wrong Answers:**
- "Reynolds number effect on K-factor" — annubar K-factor is stable over wide Re range
- "Rangeability limit" — 30% of range is within typical 3:1 rangeability for DP flow
- "Transmitter low-end nonlinearity" — DP transmitter should be linear to 1% of range
- "Installation error" — insertion depth was verified

**Scoring Rubric:**
- Full (100%): Port plugging + square-law amplification + air service issues + blowdown
- High (75%): Port plugging + low-flow sensitivity
- Low (50%): Identifies plugging but can't explain low-flow amplification
- Zero: Wrong root cause

**Reference:** Kuphaldt LIII Ch.16 (Flow Measurement); Emerson Rosemount Annubar Application Guide

---

## IUK-T3-DIAG-348
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A FOUNDATION Fieldbus segment has a scheduled communication macrocycle of 500 ms. After adding a new AI function block to an existing device, the macrocycle overruns and the system loses deterministic timing. No new devices were added — only a new function block on an existing device. What happened and how do you fix it?

**Correct Answer:**  
**The new AI function block's scheduled execution time and communication time exceeded the available time budget within the 500 ms macrocycle.**

**Required Elements:**
- Macrocycle time budget exceeded: mandatory
- Function block execution + communication time components: mandatory
- LAS scheduling concept: mandatory
- Macrocycle increase or block redistribution as fix: required for full credit

**Common Wrong Answers:**
- "Too many devices on segment" — no new devices were added
- "Communication error" — this is a scheduling/capacity issue, not a communication error
- "Segment wiring problem" — physical layer is fine; it's a logical scheduling issue
- "Wrong device configuration" — the device is configured correctly; the schedule is overloaded

**Scoring Rubric:**
- Full (100%): Time budget + execution/communication components + LAS + fix options
- High (75%): Time budget exceeded + fix
- Low (50%): Identifies scheduling issue but not mechanism
- Zero: Blames physical layer or device

**Reference:** ISA-50.02; IEC 61158 (FOUNDATION Fieldbus); Kuphaldt LIII Ch.22

---

## IUK-T3-DIAG-349
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A control valve in throttling service on a liquid pipeline shows cavitation noise and vibration. The operating conditions are: upstream pressure 200 PSIG, downstream pressure 20 PSIG, fluid is water at 100°F. The valve pressure drop is 180 PSI across a globe valve with standard trim. What calculations would you perform to confirm cavitation and what is the likely solution?

**Correct Answer:**  
**Cavitation occurs when the local pressure at the vena contracta drops below the fluid's vapor pressure, causing vapor bubbles that collapse violently downstream.**

**Required Elements:**
- x vs x_T comparison: mandatory
- Choked flow identification: mandatory
- Vapor pressure check: mandatory
- Anti-cavitation trim or staged pressure drop as solution: required for full credit

**Common Wrong Answers:**
- "Flashing, not cavitation" — flashing occurs when downstream P < P_vapor; here downstream P (20 PSIG) >> P_vapor (0.95 PSIA)
- "Just need a bigger valve" — a bigger valve with more flow won't fix cavitation
- "Valve erosion but no cavitation" — the ΔP/P1 ratio confirms cavitation
- "Tighten packing" — cavitation is hydraulic, not mechanical

**Scoring Rubric:**
- Full (100%): x vs x_T calc + choked flow + vapor pressure + solution
- High (75%): Correct calculation method + conclusion
- Low (50%): Identifies cavitation but no calculation
- Zero: Misidentifies as flashing or doesn't calculate

**Reference:** ISA-75.01 (Control Valve Sizing); Kuphaldt LIII Ch.25; IEC 60534

---

## IUK-T3-DIAG-351
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A positive displacement (PD) flow meter on a viscous chemical feed (300 cP) is reading 3% HIGH compared to a totalizer-verified batch weight (mass/density). The meter was calibrated at the factory with water. The meter is a gear-type PD meter. What is the most likely explanation?

**Correct Answer:**  
**Most likely cause: Reduced slippage at high viscosity — the PD meter OVER-registers at high viscosity compared to its water calibration.**

**Required Elements:**
- Reduced slippage at high viscosity: mandatory
- Over-registration mechanism: mandatory
- Comparison to water calibration: mandatory
- Viscosity correction factor or recalibration: required for full credit

**Common Wrong Answers:**
- "High viscosity causes under-reading" — opposite; reduced slippage causes OVER-reading
- "Meter is damaged" — behavior is physically expected
- "Temperature effect" — viscosity is the primary variable
- "Air entrainment" — would cause erratic, not consistent 3% high

**Scoring Rubric:**
- Full (100%): Slippage mechanism + over-registration + water cal comparison + correction
- High (75%): Reduced slippage + correct direction
- Low (50%): Mentions viscosity but wrong direction
- Zero: Wrong root cause or wrong direction

**Reference:** Kuphaldt LIII Ch.16 (Flow Measurement); API MPMS Chapter 5

---

## IUK-T3-DIAG-352
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A dual-sensor temperature transmitter (two RTDs for redundancy) in a SIL 2 safety loop shows one sensor reading 350°F and the other reading 355°F. The transmitter is configured for "average" mode. The safety setpoint is 400°F. A calibration check shows Sensor A reads 1°F high and Sensor B reads 2°F low at the same bath temperature. Which sensor's calibration data is more concerning for the safety function, and why?

**Correct Answer:**  
**The more concerning calibration error is Sensor B, the one reading LOW by 2°F.**

For a **high-temperature trip**, the dangerous error direction is **low indication**, because it delays the trip.

- Sensor A (+1°F high) is conservative — it tends to trip early
- Sensor B (−2°F low) is dangerous — it tends to trip late

Because the transmitter is configured for **average mode**, Sensor B pulls the average downward and delays protective action. That makes Sensor B the more important concern for the safety function.

**Required Elements:**
- Sensor B (reads LOW) is the safety concern for high-trip: mandatory
- LOW reading delays trip (dangerous direction): mandatory
- HIGH reading triggers early (safe direction): mandatory
- Average mode impact analysis: required for full credit

**Common Wrong Answers:**
- "Sensor A is worse because it has an error" — 1°F high is the SAFE direction for a high trip
- "Both are equally concerning" — direction matters for safety functions
- "Neither matters because both are within tolerance" — the DIRECTION relative to the safety function is what matters, not just magnitude
- "The average cancels the errors" — the average is still 0.5°F low, which is in the dangerous direction

**Scoring Rubric:**
- Full (100%): Sensor B is dangerous + direction analysis + average mode impact
- High (75%): Correct sensor identified + direction reasoning
- Low (50%): Identifies direction concept but wrong conclusion
- Zero: Says Sensor A is worse or says both are equal

**Reference:** IEC 61511; ISA-84.00.01; SIS Design Principles

---

## IUK-T3-DIAG-353
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A level transmitter using hydrostatic pressure (submersible type, vented to atmosphere) in an open water tank reads correctly in the morning but reads 2–3 inches HIGH in the afternoon. The actual level is confirmed stable by a float gauge. The vent tube runs 200 feet from the transmitter to the control room. What is the most likely cause?

**Correct Answer:**  
**Most likely cause: Solar heating of the vent tube during the afternoon causes the air inside to expand, increasing the reference-side pressure and making the transmitter read HIGH.**

**Required Elements:**
- Solar heating of vent tube: mandatory
- Reference pressure increase mechanism: mandatory
- Time-of-day correlation: mandatory
- Vent tube blockage as amplifying factor: required for full credit

**Common Wrong Answers:**
- "Thermal expansion of water" — water level is confirmed stable by float gauge
- "Transmitter drift" — drift wouldn't correlate with time of day
- "Atmospheric pressure change" — afternoon barometric changes are typically <0.1 inH₂O
- "Solar heating of the tank" — tank temperature would change water density, but float gauge confirms stable level

**Scoring Rubric:**
- Full (100%): Solar heating + reference pressure + time correlation + blockage factor
- High (75%): Solar heating + mechanism
- Low (50%): Identifies temperature effect but wrong mechanism
- Zero: Wrong root cause

**Reference:** Kuphaldt LIII Ch.15 (Level Measurement); Submersible Transmitter Application Guides

---

## IUK-T3-DIAG-354
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A motor-operated valve (MOV) used as an on/off isolation valve in a pipeline shows a torque switch trip at 85% open during a closing stroke. The valve had been operating correctly for 5 years. The motor draws correct current and the gearbox is in good condition. What is the most likely cause and what should be investigated?

**Correct Answer:**  
**Most likely cause: Seat or body cavity debris causing increased torque during the closing stroke, or packing gland over-tightened during recent maintenance.**

**Required Elements:**
- Debris or packing friction as likely cause: mandatory
- Running torque vs seating torque distinction: mandatory
- Diagnostic differentiation approach: mandatory
- Motor current profile as diagnostic tool: required for full credit

**Common Wrong Answers:**
- "Motor failure" — motor draws correct current per question
- "Gearbox failure" — gearbox is in good condition per question
- "Torque switch malfunction" — possible but should verify cause before assuming switch failure
- "Valve seized" — valve moves to 85%, so it's not fully seized

**Scoring Rubric:**
- Full (100%): Debris/packing + running vs seating torque + diagnostics + current profile
- High (75%): Correct cause + diagnostic approach
- Low (50%): Identifies mechanical issue but not specific
- Zero: Blames motor or gearbox despite question ruling them out

**Reference:** ASME OM-1 (MOV Testing); IEEE 96 (MOV Application); Limitorque/Rotork Technical Manuals

---

## IUK-T3-DIAG-355
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A pH control system neutralizes an acidic waste stream (pH 2–4) with sodium hydroxide (NaOH). The control valve is a small equal-percentage globe valve. The process variable (pH) oscillates between pH 5 and pH 9 despite the controller output being relatively stable at 45%. The reactor has adequate mixing and residence time. What is the fundamental problem?

**Correct Answer:**  
**Fundamental problem: The titration curve for strong acid/strong base neutralization has an extremely steep gain near pH 7, creating a nonlinear process gain that the linear PID controller cannot handle.**

**Required Elements:**
- Titration curve nonlinearity identified: mandatory
- Extreme gain near pH 7 quantified or described: mandatory
- PID linear controller vs nonlinear process mismatch: mandatory
- Gain scheduling or multi-stage as solution: required for full credit

**Common Wrong Answers:**
- "Controller needs retuning" — no single set of PID parameters can handle the 1000× gain variation
- "Valve stiction" — controller output is stable, not the valve
- "Poor mixing" — adequate mixing stated in question
- "Measurement noise" — the oscillation is real (pH 5 to 9 is a real swing)

**Scoring Rubric:**
- Full (100%): Titration curve + nonlinear gain + PID mismatch + multi-stage or gain scheduling
- High (75%): Nonlinearity + process gain concept
- Low (50%): Identifies pH control is difficult but can't explain why
- Zero: Suggests simple retuning

**Reference:** Kuphaldt LIII Ch.17 + Ch.29; ISA Practical Process Control (pH Chapter)

---

## IUK-T3-DIAG-356
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A natural gas flow measurement station uses a Daniel Senior orifice fitting. After a routine orifice plate change (from a 4.000" bore to a 3.500" bore for a lower flow range), the flow readings are approximately 30% higher than expected based on the pipeline operator's nomination. The DP transmitter and computer were both updated with the new bore diameter. What was likely done wrong?

**Correct Answer:**  
**Most likely cause: The orifice plate was installed BACKWARD in the Daniel Senior fitting.**

Daniel Senior orifice fittings allow plate changes under pressure by sliding the plate in and out through a carrier mechanism. The plate has a SHARP upstream edge and a beveled/chamfered downstream edge.

**Required Elements:**
- Plate installed backward (sharp edge downstream): mandatory
- Effect on discharge coefficient and DP: mandatory
- Direction of error (reads HIGH): mandatory
- Physical inspection of plate orientation: required for full credit

**Common Wrong Answers:**
- "Wrong bore diameter entered in computer" — question states computer was updated
- "Plate damage" — wouldn't cause a consistent 30% shift
- "Gas composition changed" — wouldn't cause a clean 30% error
- "DP transmitter miscalibrated" — DP transmitter wasn't changed

**Scoring Rubric:**
- Full (100%): Backward plate + Cd effect + correct direction + physical inspection
- High (75%): Backward plate + direction
- Low (50%): Identifies plate issue but not specific
- Zero: Wrong root cause

**Reference:** AGA Report No. 3 (AGA-3); ISO 5167; Daniel Measurement (Orifice Fitting Manual)

---

## IUK-T3-DIAG-357
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A 4–20 mA output from a flow transmitter shows 0.5 Hz oscillation (2-second period) on the DCS trend. The actual process flow is steady. A portable ammeter at the transmitter terminals shows a steady 12.0 mA with no oscillation. The cable is 500 ft of 18 AWG shielded twisted pair running through a cable tray with VFD power cables. The shield is grounded at both ends. What is the most likely cause and the fix?

**Correct Answer:**  
**Most likely cause: Electromagnetic interference (EMI) from adjacent VFD cables inducing a common-mode signal on the 4–20 mA loop, which is converted to a differential-mode signal by the unequal shield ground impedances (shield grounded at both ends).**

**Required Elements:**
- EMI from VFD cables coupling through ground loop: mandatory
- Both-end shield grounding as the root cause of ground loop: mandatory
- Why ammeter doesn't see it (location or filtering): mandatory
- Single-end shield grounding as fix: required for full credit

**Common Wrong Answers:**
- "Transmitter oscillation" — ammeter at transmitter shows steady 12 mA
- "DCS input card failure" — the noise is real, just coupled from external source
- "Process oscillation" — flow confirmed steady
- "Power supply ripple" — wouldn't produce 0.5 Hz and wouldn't correlate with VFD proximity

**Scoring Rubric:**
- Full (100%): VFD EMI + ground loop + ammeter logic + single-end grounding fix
- High (75%): EMI + shield grounding issue + fix
- Low (50%): Identifies EMI but not ground loop mechanism
- Zero: Wrong root cause

**Reference:** Kuphaldt LIII Ch.20 (Electrical Noise); IEEE 518; ISA RP 12.6

---

## IUK-T3-DIAG-358
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A nuclear level gauge (gamma ray) on a coal slurry pipeline reads 15% lower than expected. The source (Cs-137) was installed 8 years ago. The detector was recently replaced and calibrated against empty and full pipe references. The pipeline wall thickness was measured and is within specification. What is the most likely cause of the 15% low reading?

**Correct Answer:**  
**Source decay by itself is not the best answer here.**

Cs-137 absolutely decays over 8 years, but the problem also says the detector was **replaced and calibrated against empty and full references**. That means the instrument should already be normalized to the source’s current activity.

So the more likely cause of a **15% low reading** is that the **process now attenuates less radiation than it did during calibration** — for example:
- lower slurry density / lower solids concentration, or
- entrained gas / voids in the slurry stream.

Either condition gives the detector **more count rate**, which the instrument interprets as **less material present** and therefore a lower reading.

So the best diagnosis is **process attenuation changed**, not “old source” by itself.

**Required Elements:**
- Source decay calculation (half-life analysis): mandatory
- Recognition that calibration with current source should compensate: mandatory
- Process density change as actual root cause: mandatory
- Systematic elimination of source decay after calibration analysis: required for full credit

**Common Wrong Answers:**
- "Source decay" — if calibrated with current source, decay is already compensated
- "Pipe wall thinning" — measured and within spec per question
- "Detector failure" — recently replaced and calibrated
- "Background radiation" — doesn't change by 15%

**Scoring Rubric:**
- Full (100%): Decay calc + calibration reasoning + density change identification
- High (75%): Recognizes calibration compensates for decay + identifies density
- Low (50%): Identifies source decay but doesn't account for recalibration
- Zero: States source decay as final answer

**Reference:** Kuphaldt LIII Ch.15 (Level Measurement); NRC Radiation Safety; Vega/Ronan Nuclear Gauge Manuals

---

## IUK-T3-DIAG-359
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A flame scanner (UV type) on a natural gas burner has frequent false "flame out" alarms during steady operation. The burner is definitely lit (visible flame). The scanner was recently cleaned and the sight tube is clear. The UV detector tube was replaced 6 months ago. Adjacent burners do not have this problem. What is the most likely cause?

**Correct Answer:**  
**Most likely cause: The UV flame scanner is detecting the flame intermittently because the flame geometry has shifted, moving the UV-emitting zone partially out of the scanner's field of view.**

**Required Elements:**
- Flame geometry shift (flame partially out of scanner FOV): mandatory
- UV detection zone = flame base: mandatory
- Turbulent fluctuation causing intermittency: mandatory
- Burner tip/air register inspection: required for full credit

**Common Wrong Answers:**
- "Dirty lens" — recently cleaned per question
- "UV tube failure" — replaced 6 months ago; UV tubes don't degrade this quickly
- "Electrical interference" — would affect adjacent scanners too
- "Scanner sensitivity too low" — adjacent scanners (same type) work fine

**Scoring Rubric:**
- Full (100%): Flame geometry + UV zone + intermittency + burner inspection
- High (75%): Flame position + intermittency explanation
- Low (50%): Identifies alignment issue but not flame shift
- Zero: Blames scanner hardware

**Reference:** NFPA 85 (Boiler and Combustion System Hazards Code); Kuphaldt LIII Ch.17; Fireye/Honeywell Flame Scanner Application Guide

---

## IUK-T3-DIAG-360
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A weighing system uses four load cells under a hopper (one at each corner). The total weight reads correctly when verified against a calibration weight placed at the center of the hopper. However, when the same weight is placed at one corner, the total indicated weight is 5% lower than actual. What does this indicate?

**Correct Answer:**  
**This indicates one or more load cells have different sensitivities (output mismatch), causing corner loading errors.**

**Required Elements:**
- Cell sensitivity mismatch identified: mandatory
- Corner loading error concept: mandatory
- Why center loading passes but corner loading fails: mandatory
- Trimming/adjustment procedure: required for full credit

**Common Wrong Answers:**
- "Calibration is wrong" — center loading is correct, so overall calibration is fine
- "One cell is dead" — would cause a much larger error (25%), not 5%
- "Overload" — the calibration weight is the same as the one that reads correctly at center
- "Foundation uneven" — could contribute, but question asks what the symptom indicates

**Scoring Rubric:**
- Full (100%): Sensitivity mismatch + corner loading concept + center vs corner analysis + trimming
- High (75%): Cell mismatch + corner loading
- Low (50%): Identifies cell issue but can't explain center-pass/corner-fail
- Zero: Blames calibration or single cell failure

**Reference:** NIST Handbook 44; OIML R76; Kuphaldt LIII Ch.13 (Force/Weight Measurement)

---

## IUK-T3-DIAG-361
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A Coriolis flow meter on an ethylene glycol line reads zero flow despite confirmed process flow. The meter shows "unbalanced tubes" diagnostic. The installation is on a horizontal pipe run with the meter oriented with tubes pointing downward (U-tube design). What is the likely cause?

**Correct Answer:**  
**Most likely cause: Asymmetric coating or buildup inside the measuring tubes, causing mass imbalance between the two tubes.**

Coriolis meters require the two vibrating tubes to be mechanically balanced. If one tube accumulates more coating than the other, the mass distribution becomes asymmetric, the tubes vibrate at different natural frequencies, and the phase measurement becomes unreliable.

With tubes pointing downward on a horizontal pipe and ethylene glycol (which can become viscous and deposit at low-flow zones), material can settle unevenly.

**Required Elements:**
- Asymmetric tube coating/buildup: mandatory
- Tube balance requirement for Coriolis operation: mandatory
- Orientation contribution (tubes down = settling): mandatory
- Reorientation recommendation: required for full credit

**Common Wrong Answers:**
- "Air in tubes" — would show drive gain high, not unbalanced tubes specifically
- "Electronics failure" — unbalanced tubes is a mechanical diagnostic
- "Wrong fluid density" — density doesn't cause tube imbalance
- "Flow too low" — meter shows zero flow + diagnostic alarm, not just low reading

**Scoring Rubric:**
- Full (100%): Asymmetric buildup + balance requirement + orientation + cleaning/reorientation
- High (75%): Correct root cause + solution
- Low (50%): Identifies buildup but not asymmetry mechanism
- Zero: Wrong root cause

**Reference:** Kuphaldt LIII Ch.16; Emerson Micro Motion Installation Guide

---

## IUK-T3-DIAG-362
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A chlorine gas detector (electrochemical cell type) in a water treatment facility consistently reads 0.3 ppm when no chlorine is present (verified by a separate photoionization detector reading 0.0). The detector was zero-calibrated yesterday and read 0.0 ppm immediately after. The detector is located near the sodium hypochlorite (NaOCl) storage area. What is the most likely cause?

**Correct Answer:**  
**Most likely cause: there really is low-level chlorine present near the hypochlorite area, and the electrochemical chlorine sensor is detecting it correctly.**

The supposed “proof” that no chlorine is present is invalid because a standard **10.6 eV PID does not detect chlorine gas**. A PID reading of 0.0 only tells you there is no PID-detectable VOC response — it does **not** prove Cl₂ is absent.

Near **NaOCl storage**, low-level chlorine off-gassing is entirely plausible. That makes the chlorine cell’s 0.3 ppm reading believable.

**Required Elements:**
- NaOCl off-gassing as real chlorine source: mandatory
- PID limitation (cannot detect Cl₂ due to IE > 10.6 eV): mandatory
- Electrochemical cell correctly detecting low-level Cl₂: mandatory
- Relocation or ventilation as solution: required for full credit

**Common Wrong Answers:**
- "Cell drift" — calibrated yesterday, reads 0.0 after cal
- "Humidity interference" — would be constant, not 0.3 ppm specific
- "PID confirms no gas present" — PID CANNOT detect Cl₂
- "Electronic offset" — zeroed correctly yesterday

**Scoring Rubric:**
- Full (100%): Real Cl₂ from NaOCl + PID limitation + confirmation method + solution
- High (75%): Correct source + PID limitation
- Low (50%): Identifies NaOCl source but doesn't address PID limitation
- Zero: Treats as false alarm or detector fault

**Reference:** Kuphaldt LIII Ch.17; ISA-92 (Gas Detection); RAE Systems PID Application Guide

---

## IUK-T3-DIAG-363
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A PLC structured text program calculates a flow rate from a DP transmitter using Q = K × √(DP). The calculation uses integer math (no floating point). At low DP values (below 5% of range), the calculated flow shows step changes and drops to zero even though the DP reading is non-zero. What is causing this?

**Correct Answer:**  
**Root cause: Integer truncation error in the square root calculation at low values.**

When using integer math, the square root of small numbers loses resolution dramatically:
- √(100) = 10 (integer: 10) ✓
- √(25) = 5 (integer: 5) ✓
- √(4) = 2 (integer: 2) ✓
- √(3) = 1.73 (integer: **1**) — 42% error
- √(2) = 1.41 (integer: **1**) — 29% error
- √(1) = 1.0 (integer: **1**)
- √(0.5) = 0.71 (integer: **0**) — complete loss

At low DP values, the integer representation of DP may be in single digits. The integer square root of these small numbers produces very coarse steps (0, 1, 1, 1, 2, 2, 2, 3...), and any DP value that produces a square root below 0.5 rounds to zero.

**Required Elements:**
- Integer truncation in square root: mandatory
- Resolution loss at small values: mandatory
- Quantization step effect explained: mandatory
- Scaling or floating-point solution: required for full credit

**Common Wrong Answers:**
- "Transmitter noise at low range" — the DP reading itself is non-zero and smooth
- "PLC scan rate issue" — scan rate doesn't cause math truncation
- "Overflow error" — this is underflow/truncation, not overflow
- "Sensor dead band" — the DP sensor is reporting correctly

**Scoring Rubric:**
- Full (100%): Integer truncation + resolution loss + step quantization + scaling fix
- High (75%): Integer math issue + solution
- Low (50%): Identifies math problem but not specific mechanism
- Zero: Blames sensor or PLC hardware

**Reference:** Kuphaldt LIII Ch.16 + Ch.21; IEC 61131-3 (PLC Programming)

---

## IUK-T3-DIAG-364
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
Two identical pressure transmitters on the same vessel tap (via a three-valve manifold with equalizing valve open) show a 0.5 PSI difference. Both were calibrated against the same reference within the last month and were within ±0.1% of span. The vessel pressure is 500 PSIG. The transmitters are mounted at different elevations — one is 3 feet higher than the other. What is the cause of the discrepancy?

**Correct Answer:**  
**Cause of the discrepancy: different static head at the two transmitter elevations.**

If both instruments are connected to the same source pressure but mounted at different elevations, any **liquid-filled or partially liquid-filled impulse path / seal system** creates different hydrostatic head at the sensing elements.

That is an installation effect, not a calibration problem.

A 3-foot elevation difference gives:
- about **1.3 psi** if the fill fluid is water / condensate (SG ≈ 1.0)
- proportionally less if the fill fluid is lighter

Since the observed difference is **0.5 psi**, the effective fill-fluid SG is roughly:
\[
SG pprox 0.5/1.3 pprox 0.38
\]
So the two readings are consistent with a **lighter liquid fill, mixed-phase impulse path, or another non-water fill condition**.

The key conclusion is still the same: **mounting elevation created a predictable hydrostatic offset.**

**Required Elements:**
- Elevation difference causing hydrostatic head difference: mandatory
- Calculation of expected ΔP from elevation: mandatory
- This is NOT a calibration error: mandatory
- Zero offset correction or equal-elevation mounting: required for full credit

**Common Wrong Answers:**
- "Calibration drift" — both calibrated within ±0.1% recently
- "Equalizing valve not fully open" — would cause different readings but not consistently 0.5 PSI
- "Transmitter accuracy difference" — ±0.1% of span at 500 PSI range = ±0.5 PSI... this is actually possible, but the systematic nature and consistent 0.5 PSI points to elevation, not random accuracy
- "Process noise" — a consistent 0.5 PSI is not noise

**Scoring Rubric:**
- Full (100%): Elevation/hydrostatic + calculation + not calibration error + offset solution
- High (75%): Elevation cause + this is normal
- Low (50%): Mentions elevation but can't calculate
- Zero: Blames calibration

**Reference:** Kuphaldt LIII Ch.12 (Instrument Signals); ISA RP31.1

---

## IUK-T3-DIAG-365
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A Profibus-PA segment with 8 devices loses communication with ALL devices simultaneously for 10-15 seconds, then recovers. This happens approximately once per day at random times. Individual devices never drop independently. The DP coupler, power supply, and all devices have been replaced one at a time with no improvement. What is the most likely cause?

**Correct Answer:**  
**Most likely cause: The trunk cable has an intermittent fault — likely a marginal connection, water ingress in a junction box, or cable damage — that briefly disrupts the bus signal quality below the communication threshold for ALL devices simultaneously.**

**Required Elements:**
- Trunk cable/infrastructure fault (shared path): mandatory
- Why individual component replacement didn't help: mandatory
- Simultaneous failure logic (shared infrastructure): mandatory
- Bus analyzer or TDR as diagnostic: required for full credit

**Common Wrong Answers:**
- "Power supply fault" — power supply was replaced with no improvement
- "Device address conflict" — would affect specific devices, not all simultaneously
- "DP coupler fault" — was replaced with no improvement
- "Electromagnetic interference" — EMI would cause communication errors, not complete 10-15 second dropouts at random daily intervals

**Scoring Rubric:**
- Full (100%): Trunk cable + shared infrastructure logic + component replacement reasoning + TDR/analyzer
- High (75%): Trunk cable + shared path reasoning
- Low (50%): Identifies infrastructure but not specific diagnostic
- Zero: Suggests replacing another device

**Reference:** IEC 61158 (Profibus); Kuphaldt LIII Ch.22; PI (Profibus International) Commissioning Guide

---

## IUK-T3-DIAG-366
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A zirconia oxygen analyzer on a combustion flue gas stack reads 15% O₂ when the actual O₂ is 3% (verified by portable electrochemical analyzer). The zirconia cell temperature is 700°C (normal operating range). The reference air supply is connected. The analyzer was reading correctly 2 weeks ago. What is the most likely cause?

**Correct Answer:**  
**Most likely cause: Reference air supply contamination or blockage.**

A zirconia oxygen analyzer works by measuring the oxygen partial pressure difference between the sample gas and a reference gas (usually ambient air at 20.9% O₂). The Nernst equation governs the cell voltage:

E = (RT/4F) × ln(P_ref / P_sample)

If the reference air supply is contaminated with flue gas (low O₂) or blocked (causing the reference chamber to be diluted or depleted):
1. P_ref decreases from 20.9% O₂ to something lower
2. The voltage across the cell decreases
3. The analyzer interprets the lower voltage as a SMALLER difference between sample and reference
4. Smaller difference → higher indicated O₂ in the sample

**Required Elements:**
- Reference air contamination or blockage: mandatory
- Nernst equation concept (voltage depends on O₂ ratio): mandatory
- Why high reference contamination causes high sample reading: mandatory
- Reference air supply verification: required for full credit

**Common Wrong Answers:**
- "Zirconia cell cracked" — would typically cause erratic readings or complete failure
- "Cell temperature too high/low" — 700°C is within normal range
- "Sample conditioning issue" — wouldn't cause a steady 15% reading when actual is 3%
- "Calibration drift" — 12% error in 2 weeks is too large for drift; more likely a binary change (leak/blockage)

**Scoring Rubric:**
- Full (100%): Reference air issue + Nernst concept + direction logic + supply verification
- High (75%): Reference air + correct direction
- Low (50%): Identifies reference but can't explain direction
- Zero: Blames zirconia cell

**Reference:** Kuphaldt LIII Ch.17 (Analytical); Ametek/Yokogawa Zirconia O₂ Analyzer Manuals

---

## IUK-T3-DIAG-367
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A plant has two identical safety shutdown valves (fail-closed, spring-return pneumatic actuators) in the same SIS loop as a 1oo2 (one-out-of-two-to-trip) configuration. During a proof test, Valve A strokes from 100% open to fully closed in 3 seconds (within specification). Valve B strokes from 100% open to only 85% closed, then stalls. Both valves have identical actuators and the same air supply. What is the most likely cause of Valve B's failure, and what is the impact on the SIS loop?

**Correct Answer:**  
**Most likely valve B failure cause: Spring force insufficient to overcome process force plus packing/seat friction.**

In a fail-closed spring-return actuator:
- Normal operation: Air pressure holds valve open against spring
- Trip (air vented): Spring drives valve closed

Valve B stalls at 85% closed, meaning the spring can drive the valve through 85% of its stroke but lacks force for the final 15%. This last portion of travel is where:
1. The plug/disc engages the seat — seating force requirement increases dramatically
2. Process pressure may be pushing against closure (depending on flow direction vs. plug orientation)
3. Packing friction is highest at the end of stroke (if packing has degraded or was overtightened)

**Required Elements:**
- Spring force insufficient for seating: mandatory
- 1oo2 still passes with one valve (but degraded): mandatory
- PFD impact of operating as effective 1oo1: mandatory
- Repair requirement and compensating measures: required for full credit

**Common Wrong Answers:**
- "SIS loop has failed proof test" — 1oo2 requires only one to trip; Valve A passed
- "Air supply issue" — both valves have same supply, and air is vented for fail-close
- "Actuator sizing" — both are identical and Valve A works fine
- "The 85% closure is close enough" — in safety service, incomplete closure can allow dangerous process fluid to pass

**Scoring Rubric:**
- Full (100%): Spring/friction cause + 1oo2 logic + degraded PFD + repair requirement
- High (75%): Correct cause + 1oo2 understanding
- Low (50%): Identifies mechanical issue but misses SIS implications
- Zero: Claims SIS failed or ignores 1oo2 architecture

**Reference:** IEC 61511; ISA-84.00.01; ISA-75.05 (Control Valve Terminology)

---

## IUK-T3-DIAG-368
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A paperless chart recorder connected to 8 thermocouple inputs shows correct readings on channels 1-6, but channels 7 and 8 both read identically and both track with channel 6's temperature changes even though they are connected to different thermocouples in different locations. What is the most likely cause?

**Correct Answer:**  
**Most likely cause: Channels 7 and 8 have open thermocouple circuits, and the recorder is reading the common-mode voltage present at the input terminals — which is being influenced by channel 6 through input multiplexer crosstalk.**

**Required Elements:**
- Open thermocouple circuits on channels 7 and 8: mandatory
- Multiplexer crosstalk / ghost reading mechanism: mandatory
- Shared wiring path as common cause: mandatory
- Resistance measurement at terminals: required for full credit

**Common Wrong Answers:**
- "Recorder input failure" — channels 1-6 work correctly
- "Both TCs in same process" — question states different locations
- "Configuration error" — both channels tracking channel 6 dynamically rules out static config error
- "CJC error" — would cause an offset on all channels, not just 7 and 8

**Scoring Rubric:**
- Full (100%): Open TC + multiplexer crosstalk + shared wiring + resistance check
- High (75%): Open circuit + ghost reading
- Low (50%): Identifies open circuit but not crosstalk mechanism
- Zero: Blames recorder or configuration

**Reference:** Kuphaldt LIII Ch.14 + Ch.21; Data Acquisition System Design

---

## IUK-T3-DIAG-369
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A turbidity analyzer on a drinking water plant effluent shows a sudden reading of 4.0 NTU (regulatory limit is 1.0 NTU) but the inline particle counter at the same point shows zero particles above 2 microns. Grab samples analyzed in the lab show 0.3 NTU. What is the most likely cause of the turbidity analyzer's high reading?

**Correct Answer:**  
**Most likely cause: Air bubbles in the sample cell of the turbidity analyzer.**

Turbidity analyzers measure light scattering caused by suspended particles. Air bubbles scatter light in a similar manner to particles, causing false high readings.

**Required Elements:**
- Air bubbles in sample cell: mandatory
- Particle counter and grab sample as cross-verification: mandatory
- Bubble sources identified: mandatory
- Degassing or backpressure solution: required for full credit

**Common Wrong Answers:**
- "Analyzer needs calibration" — would show consistent error, not sudden 4.0 NTU
- "Real turbidity event" — contradicted by particle counter and lab sample
- "Stray light in analyzer" — would be a baseline issue, not sudden onset
- "Wrong wavelength" — wouldn't cause a 10× high reading

**Scoring Rubric:**
- Full (100%): Air bubbles + cross-verification logic + sources + solution
- High (75%): Air bubbles + cross-verification
- Low (50%): Identifies sample conditioning issue but not bubbles specifically
- Zero: Believes reading is real

**Reference:** EPA Method 180.1; Hach Turbidity Analyzer Application Notes

---

## IUK-T3-DIAG-370
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
An Allen-Bradley ControlLogix PLC has an analog output module driving a control valve positioner (4–20 mA). The output is commanded to 12.0 mA but measures 12.0 mA at the module terminals and 11.3 mA at the valve positioner terminals. The cable is 800 ft of 16 AWG. What is causing the 0.7 mA discrepancy?

**Correct Answer:**  
**This should NOT happen in a properly functioning current loop — current is the same at every point in a series circuit.**

A 0.7 mA difference between the module terminals and the positioner terminals means current is being diverted through a parallel path somewhere along the 800-foot cable run.

**Required Elements:**
- Current should be same everywhere in series loop: mandatory
- This is a parallel leakage path, not cable resistance: mandatory
- Megger/insulation test recommended: mandatory
- Leakage resistance calculation: required for full credit

**Common Wrong Answers:**
- "Cable resistance drops the current" — fundamentally wrong for a current loop
- "Positioner input impedance" — positioner is in series, not shunting current
- "Module output error" — measures 12.0 mA at module terminals
- "Calibration difference between meters" — 0.7 mA is too large for meter accuracy difference

**Scoring Rubric:**
- Full (100%): Series current principle + leakage path + megger test + resistance calculation
- High (75%): Correct principle + leakage identified
- Low (50%): Identifies something wrong but claims cable resistance
- Zero: States cable resistance causes current drop

**Reference:** Kuphaldt LIII Ch.12; Ohm's Law / Kirchhoff's Current Law

---

## IUK-T3-DIAG-371
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A radar level transmitter (78 GHz FMCW) in a reactor vessel with an agitator reads correctly when the agitator is OFF but shows a false high level (approximately 95%) when the agitator is running at full speed. The actual level is 50%. The antenna is a drop-type (rod) antenna mounted on a 4-inch nozzle. What is the most likely cause?

**Correct Answer:**  
**Most likely cause: The agitator blades are passing through or near the radar beam path, creating a strong false reflection that the transmitter interprets as a closer (higher) surface.**

At 78 GHz, the radar beam is relatively narrow (4-inch antenna produces a beam width of approximately 8-10°). However:

1. The agitator shaft and blades are metal — strong radar reflectors
2. When the agitator runs, the blades rotate through the beam path
3. Each time a blade passes through the beam, it creates a reflection at the blade's distance from the antenna
4. The agitator blades are higher than the liquid surface (at approximately the 90-95% elevation)
5. The transmitter locks onto the strong blade reflection instead of the weaker liquid surface reflection

**Required Elements:**
- Agitator blade reflection in beam path: mandatory
- Metal blade = strong reflector at fixed distance: mandatory
- Works when OFF because blades stop blocking beam: mandatory
- Relocation, stilling well, or false echo mapping: required for full credit

**Common Wrong Answers:**
- "Surface turbulence from agitator" — turbulence would cause loss of echo, not a false HIGH reading at 95%
- "Foam from agitation" — foam would attenuate signal, not produce a strong false echo
- "Radar electronics affected by vibration" — wouldn't produce a clean 95% reading
- "Antenna fouling" — fouling doesn't change with agitator state

**Scoring Rubric:**
- Full (100%): Blade reflection + fixed distance + off-state reasoning + solution
- High (75%): Blade reflection + solution
- Low (50%): Identifies agitator interference but not specific mechanism
- Zero: Blames surface turbulence

**Reference:** Kuphaldt LIII Ch.15; VEGA/Emerson Radar Application Guide (Agitator Vessels)

---

## IUK-T3-DIAG-373
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A control valve with an electro-pneumatic positioner and HART communication responds correctly to command signal changes from the DCS. However, the HART feedback of valve position always shows 0.0% regardless of actual valve position. The valve physically moves correctly and the positioner display shows correct position. What is the most likely cause?

**Correct Answer:**  
**Most likely cause: The HART Device Variable (DV) or Secondary Variable mapping for valve position is not configured correctly in the positioner, or the position feedback sensor (LVDT, potentiometer, or Hall effect) is providing data to the local display but not mapped to the HART output.**

**Required Elements:**
- HART variable mapping / configuration issue: mandatory
- Two subsystems (servo vs HART) distinguished: mandatory
- HART handheld check of all device variables: mandatory
- Variable mapping or travel calibration as fix: required for full credit

**Common Wrong Answers:**
- "Position feedback sensor failed" — local display shows correct position, so sensor works
- "HART communication failure" — the DCS IS reading 0.0 via HART, so communication is working (just reading the wrong value)
- "Positioner needs calibration" — the servo calibration is correct (valve positions correctly)
- "DCS configuration error" — partially correct but the root is usually in the positioner HART config

**Scoring Rubric:**
- Full (100%): HART variable mapping + dual subsystem distinction + handheld check + fix
- High (75%): Configuration issue + HART check
- Low (50%): Identifies HART issue but not specific
- Zero: Blames feedback sensor or positioner servo

**Reference:** ISA-75.25 (Smart Valve Positioner); HART Communication Protocol; Kuphaldt LIII Ch.25

---

## IUK-T3-DIAG-374
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A differential pressure transmitter measuring boiler drum level via hydrostatic method shows a level INCREASE of 6 inches when the boiler firing rate is rapidly increased, even though the actual water level dropped 3 inches (verified by sight glass). This "wrong direction" indication lasts approximately 30 seconds before the transmitter begins tracking in the correct direction. What phenomenon causes this?

**Correct Answer:**  
**This is the "shrink and swell" phenomenon in boiler drum level measurement.**

**Required Elements:**
- Shrink and swell phenomenon named: mandatory
- Steam bubble density effect on hydrostatic measurement: mandatory
- Sight glass vs. DP transmitter difference explained: mandatory
- Three-element control as mitigation: required for full credit

**Common Wrong Answers:**
- "Transmitter is wrong" — transmitter is measuring correctly (hydrostatic head DID decrease); it's the interpretation that's misleading
- "Reference leg temperature change" — happens too fast (30 seconds) for reference leg thermal effects
- "Impulse line issue" — both taps are functioning correctly
- "Calibration error" — corrects itself after 30 seconds, so not a static calibration issue

**Scoring Rubric:**
- Full (100%): Shrink/swell + density/bubble mechanism + sight glass comparison + 3-element control
- High (75%): Correct phenomenon + mechanism
- Low (50%): Identifies boiler-specific issue but can't explain mechanism
- Zero: Blames transmitter malfunction

**Reference:** Kuphaldt LIII Ch.15 (Level) + Ch.29 (Boiler Control); ISA-77 (Fossil Fuel Power Plant Standards)

---

## IUK-T3-DIAG-375
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A HART-enabled transmitter is being configured remotely from the DCS using HART pass-through. The technician changes the transmitter's output mode from "4–20 mA" to "4–20 mA with HART" and the DCS trend immediately shows the analog reading jump by 0.3 mA. No process change occurred. What caused the jump?

**Correct Answer:**  
**Most likely cause: The DCS analog input card does not have adequate filtering for the HART signal, and the 1200/2200 Hz HART FSK modulation is being partially rectified or averaged into the DC reading.**

**Required Elements:**
- HART FSK modulation on 4–20 mA: mandatory
- DCS input card inadequate filtering: mandatory
- DC offset from partial rectification or inadequate filtering: mandatory
- HART filter or compatible card as solution: required for full credit

**Common Wrong Answers:**
- "Transmitter output changed" — HART modulation has zero average; DC output shouldn't change
- "Process change" — none occurred
- "Calibration shift" — doesn't shift when mode changes
- "HART communication consuming current" — HART modulation averages to zero current change

**Scoring Rubric:**
- Full (100%): FSK modulation + filtering issue + rectification/averaging mechanism + solution
- High (75%): HART signal interference + filter solution
- Low (50%): Identifies HART as cause but not mechanism
- Zero: Blames transmitter output change

**Reference:** HART Communication Foundation; Kuphaldt LIII Ch.22; DCS Analog Input Specifications

---

## IUK-T3-DIAG-376
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A hydrostatic tank gauging (HTG) system uses three pressure transmitters at different elevations on a storage tank to calculate level, density, and interface level. The calculated density suddenly shows a 5% increase, but the level and interface readings appear normal. Lab analysis of a grab sample shows no density change. What is the most likely cause?

**Correct Answer:**  
**Most likely cause: The middle pressure transmitter has drifted or shifted, creating an artificial density error in the HTG calculation.**

**Required Elements:**
- Middle transmitter drift: mandatory
- HTG density calculation from pressure gradient: mandatory
- Why level remains unaffected: mandatory
- Individual transmitter verification: required for full credit

**Common Wrong Answers:**
- "Actual density change" — lab analysis confirms no change
- "Temperature compensation error" — wouldn't produce a step change
- "Interface movement" — interface reading is normal per question
- "Vapor space pressure change" — affects level, not density gradient

**Scoring Rubric:**
- Full (100%): Middle transmitter + HTG math + level unaffected explanation + diagnostic steps
- High (75%): Correct root cause + verification approach
- Low (50%): Identifies transmitter issue but not which one
- Zero: Accepts density change as real

**Reference:** Kuphaldt LIII Ch.15; API MPMS Chapter 3.1A (HTG)

---

## IUK-T3-DIAG-377
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A globe-style control valve on a high-pressure steam letdown station produces severe vibration and a loud screaming noise at low valve openings (5-15%) but is quiet above 25% travel. The valve trim is single-seat, contoured plug with metal seat. Upstream pressure is 600 PSIG, downstream is 150 PSIG. What is the most likely cause and what is the solution?

**Correct Answer:**  
**Most likely cause: Aerodynamic noise and vibration from choked flow and jet impingement at low openings.**

At low openings (5-15%), the flow area is small and the pressure drop is large (600→150 PSIG, ΔP = 450 PSI). The pressure ratio exceeds the critical pressure ratio, meaning the steam reaches sonic velocity (choked flow) at the vena contracta. This causes:

1. **Shock waves** as the supersonic steam decelerates downstream of the restriction
2. **Jet impingement** — the high-velocity jet hits the valve body or downstream piping wall, causing vibration
3. **Turbulent broadband noise** from the mixing zone between the high-velocity jet and the surrounding slower flow
4. **Potential flutter** of the plug near the seat — at small openings, the plug is loosely constrained and aerodynamic forces can cause it to oscillate

**Required Elements:**
- Choked flow / sonic velocity at vena contracta: mandatory
- Jet impingement mechanism: mandatory
- Low opening = small area + large ΔP: mandatory
- Multi-stage trim as primary solution: required for full credit

**Common Wrong Answers:**
- "Cavitation" — steam is compressible; flashing can occur but cavitation is a liquid phenomenon
- "Valve seat damage" — noise is aerodynamic, not mechanical
- "Pipe resonance" — the source is the valve, not the pipe (though pipe may resonate sympathetically)
- "Wrong valve type" — globe valve is appropriate for throttling; the trim design is the issue

**Scoring Rubric:**
- Full (100%): Choked flow + jet mechanism + low-opening analysis + multi-stage trim
- High (75%): Correct root cause + solution
- Low (50%): Identifies noise but not mechanism
- Zero: Wrong root cause

**Reference:** Kuphaldt LIII Ch.25; ISA-75.17 (Control Valve Aerodynamic Noise); IEC 60534-8-3

---

## IUK-T3-DIAG-378
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A 4-20 mA level transmitter on a vessel with agitation reads correctly when the agitator is off but shows approximately 2% higher when the agitator runs. The transmitter is a flush-diaphragm DP type with the HP diaphragm at the bottom and the LP capillary connected to the vessel vapor space. The agitator is a top-entry type. What is the most likely cause?

**Correct Answer:**  
**Most likely cause: The agitator creates a vortex pattern that produces a dynamic pressure component at the bottom diaphragm, adding to the static hydrostatic pressure.**

**Required Elements:**
- Dynamic/centrifugal pressure from agitation: mandatory
- Wall pressure higher than center: mandatory
- LP side unaffected (vapor space): mandatory
- Stilling well or dampening solution: required for full credit

**Common Wrong Answers:**
- "Vibration affecting electronics" — would cause noise, not a consistent +2% offset
- "Air entrainment changing density" — would decrease density, reading LOW
- "Surface waves causing LP side fluctuation" — LP is in vapor space
- "Transmitter needs recalibration" — calibration is correct; error is process-induced

**Scoring Rubric:**
- Full (100%): Centrifugal pressure + wall effect + LP analysis + solution
- High (75%): Dynamic pressure + correct direction
- Low (50%): Identifies agitation as cause but wrong mechanism
- Zero: Wrong root cause

**Reference:** Kuphaldt LIII Ch.15 (Level Measurement)

---

## IUK-T3-DIAG-379
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A Profibus PA network segment has 12 devices all communicating normally. A 13th device is added. Upon connecting it, ALL 12 existing devices lose communication. Disconnecting device 13 restores all communication. Device 13 communicates correctly when tested on a standalone segment. What is the most likely cause?

**Correct Answer:**  
**Most likely cause: Device 13 has the same Profibus PA address as one of the existing 12 devices (address conflict), OR connecting device 13 exceeds the segment's maximum current budget.**

**Required Elements:**
- Address conflict as primary cause: mandatory
- Bus collision mechanism (all devices affected): mandatory
- Power budget as alternative cause: mandatory
- Address verification diagnostic: required for full credit

**Common Wrong Answers:**
- "Device 13 is defective" — works correctly on standalone segment
- "Cable too long" — adding one device doesn't dramatically increase length
- "Termination issue" — would affect some devices, not cause total loss on adding one device
- "PA coupler failure" — coupler was working with 12 devices; triggered by adding 13th

**Scoring Rubric:**
- Full (100%): Address conflict + collision mechanism + power budget + diagnostics
- High (75%): Address conflict + collision explanation
- Low (50%): Identifies network issue but not specific cause
- Zero: Blames device or cable

**Reference:** Kuphaldt LIII Ch.22; IEC 61158 (Profibus)

---

## IUK-T3-DIAG-380
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A paddle-wheel flow switch on a cooling water line fails to indicate flow even though water is flowing. The switch worked correctly until the cooling tower was chemically treated with a biocide last week. Visual inspection through the pipe sight glass shows the water is slightly milky. The paddle wheel appears intact and spins freely when tested manually. What is the most likely cause?

**Correct Answer:**  
**Most likely cause: the biocide treatment produced suspended debris / precipitate that fouled the paddle-wheel bearings or tight running clearances.**

The “slightly milky” water is a clue that the treatment created suspended solids or dead biological material. In service, that material can pack into the wheel clearance or bearing surfaces and add enough drag that normal water flow will not spin the paddle reliably.

That also explains why the wheel can still seem fine when handled manually: hand force is much larger than the weak hydraulic torque available at the switch.

So this is best diagnosed as **fouling from the chemical treatment**, not loss of actual flow.

**Required Elements:**
- Fouling from biocide-killed biological debris: mandatory
- Bearing/gap fouling reducing rotation: mandatory
- Manual test gives misleading "OK" result: mandatory
- Alternative flow measurement recommended: required for full credit

**Common Wrong Answers:**
- "No flow actually present" — sight glass confirms flow
- "Electrical fault" — paddle is mechanical
- "Chemical attack on paddle" — paddle appears intact and spins
- "Air in the line" — milky appearance could suggest air, but biocide correlation is stronger

**Scoring Rubric:**
- Full (100%): Biological fouling + bearing mechanism + manual test limitation + solution
- High (75%): Correct root cause + mechanism
- Low (50%): Identifies fouling but vague
- Zero: Wrong root cause

**Reference:** Kuphaldt LIII Ch.16 (Flow Measurement)

---

## IUK-T3-DIAG-381
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A cascade control system has a primary (master) temperature controller and a secondary (slave) flow controller. The temperature controller output goes to the setpoint of the flow controller. The system was working well until the secondary flow transmitter was replaced. Now the temperature oscillates wildly. The flow controller in manual mode works correctly. What is the most likely cause?

**Correct Answer:**  
**Most likely cause: The replacement flow transmitter has a different calibrated range than the original, causing a gain mismatch in the cascade loop.**

**Required Elements:**
- Transmitter range mismatch causing cascade gain change: mandatory
- Cascade loop interaction mechanism: mandatory
- Manual mode proof isolates the cascade interaction: mandatory
- Range matching or re-scaling as fix: required for full credit

**Common Wrong Answers:**
- "Temperature controller needs retuning" — partially true but misses the root cause
- "Flow controller tuning" — works fine in manual
- "New transmitter defective" — works correctly in manual
- "Cascade decoupled" — cascade is still connected and functioning

**Scoring Rubric:**
- Full (100%): Range mismatch + gain change + cascade mechanism + fix
- High (75%): Correct root cause + cascade understanding
- Low (50%): Identifies transmitter issue but not cascade mechanism
- Zero: Blames tuning without identifying range mismatch

**Reference:** Kuphaldt LIII Ch.29 (Cascade Control)

---

## IUK-T3-DIAG-382
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
An electromagnetic flow meter on a deionized (DI) water system reads zero flow despite confirmed flow. The DI water resistivity is 18.2 MΩ·cm (highest purity). The same meter model works correctly on plant water (conductivity ~500 µS/cm). What is the root cause?

**Correct Answer:**  
**Root cause: The DI water conductivity is below the minimum required for electromagnetic flow measurement.**

**Required Elements:**
- Conductivity below minimum for mag meter operation: mandatory
- Minimum conductivity specification (5-20 µS/cm): mandatory
- Faraday's law and electrode impedance: mandatory
- Alternative flow technologies: required for full credit

**Common Wrong Answers:**
- "Meter needs recalibration" — cannot calibrate away a fundamental physical limitation
- "Grounding issue" — grounding helps with noise but cannot overcome near-zero conductivity
- "Electrode fouling" — the water is ultra-pure, not fouling
- "Empty pipe condition" — flow is confirmed

**Scoring Rubric:**
- Full (100%): Conductivity below minimum + specific values + Faraday's law + alternatives
- High (75%): Conductivity issue + alternatives
- Low (50%): Identifies conductivity but no specifics
- Zero: Suggests calibration or grounding fix

**Reference:** Kuphaldt LIII Ch.16 (Flow Measurement); IEC 60534 (Magnetic Flow Meters)

---

## IUK-T3-DIAG-383
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A smart pressure transmitter with multivariable output provides both pressure and temperature readings via HART. The pressure reading is accurate (verified by gauge), but the temperature reading is 40°F higher than actual (verified by RTD). The transmitter was commissioned 6 months ago with correct readings. What is the most likely cause?

**Correct Answer:**  
**Most likely cause: The transmitter's internal temperature sensor (used for electronics compensation) is being affected by localized heating from the process or sun exposure, and this sensor is also the source of the HART temperature output.**

**Required Elements:**
- Internal vs process temperature sensor distinction: mandatory
- Localized heating source: mandatory
- Pressure compensation still works: mandatory
- Dedicated temperature sensor recommendation: required for full credit

**Common Wrong Answers:**
- "Transmitter temperature sensor failed" — it's reading correctly for its location
- "HART communication error" — pressure reads fine via HART
- "Process temperature actually changed" — RTD confirms process temp
- "Electronics overheating" — possible concern but not the primary measurement issue

**Scoring Rubric:**
- Full (100%): Internal vs process sensor + heating source + pressure compensation + recommendation
- High (75%): Internal sensor + heating identification
- Low (50%): Identifies sensor issue but confused about mechanism
- Zero: Blames HART or electronics failure

**Reference:** Kuphaldt LIII Ch.12; Rosemount 3051S Multivariable Reference Manual

---

## IUK-T3-DIAG-384
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A batch reactor has a jacket temperature control system. The controller output drives a split-range valve pair: 0-50% output opens the cooling water valve (fail-open), 50-100% output opens the steam valve (fail-closed). During a transition from heating to cooling, the reactor temperature overshoots by 25°F despite the controller responding correctly and switching to cooling at the right time. What is the most likely cause?

**Correct Answer:**  
**Most likely cause: Thermal lag in the reactor jacket and vessel walls stores heat energy that continues to transfer into the reactor contents even after the controller switches from heating to cooling.**

**Required Elements:**
- Thermal lag / thermal capacitance of jacket and wall: mandatory
- Heat continues transferring during transition: mandatory
- Controller limitation (can't overcome physics): mandatory
- Feedforward or anticipatory switching as solution: required for full credit

**Common Wrong Answers:**
- "Controller too slow" — controller is responding correctly
- "Cooling valve undersized" — the issue is thermal lag, not valve capacity
- "Split-range dead band" — would cause a different symptom (bump at transition)
- "Wrong PID tuning" — tuning can help but the fundamental issue is thermal mass

**Scoring Rubric:**
- Full (100%): Thermal lag + mechanism + controller limitation + feedforward solution
- High (75%): Thermal lag + mechanism
- Low (50%): Identifies lag but no detailed analysis
- Zero: Blames controller tuning as sole cause

**Reference:** Kuphaldt LIII Ch.29 (Process Control); ISA Practical Process Control

---

## IUK-T3-DIAG-385
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A zirconia oxygen analyzer in a fired heater stack reads 0.5% O₂ (lean, near optimal). However, combustion efficiency calculations from fuel gas flow and CO₂ measurements show the heater is actually running at approximately 8% excess air (equivalent to ~1.7% O₂). The analyzer was calibrated using certified calibration gases last week. What is the most likely cause of the low O₂ reading?

**Correct Answer:**  
**Most likely cause: the zirconia sensor is seeing a locally reducing or poorly mixed flue-gas condition, so it reports O₂ lower than the bulk stack average.**

Why this fits:
- If the analyzer reads **0.5% O₂** while the true bulk condition is closer to **1.7% O₂**, the analyzer is biased **low**
- Ordinary air in-leakage would push O₂ **up**, not down

Two strong mechanisms are:
1. **Reducing-gas interference at the zirconia cell** (CO / H₂ / unburned combustibles altering the local equilibrium at the sensor)
2. **Flow stratification / poor mixing** so the probe is sitting in a fuel-rich, low-O₂ zone rather than a representative bulk location

**Required Elements:**
- Reducing gas interference (CO/H₂) or flow stratification: mandatory
- Zirconia measures equilibrium O₂ (susceptible to reducing gases): mandatory
- Correct direction analysis (reads LOW): mandatory
- Cross-check with paramagnetic analyzer: required for full credit

**Common Wrong Answers:**
- "Air in-leakage" — would cause HIGH readings, not LOW
- "Calibration drift" — calibrated last week with certified gases
- "Fuel gas measurement error" — separate from the analyzer issue
- "Temperature compensation" — wouldn't cause this magnitude of error

**Scoring Rubric:**
- Full (100%): Reducing gas/stratification + zirconia mechanism + direction + cross-check
- High (75%): Correct root cause + mechanism
- Low (50%): Identifies analyzer limitation but vague
- Zero: Says air leakage (wrong direction)

**Reference:** Kuphaldt LIII Ch.17 (Analytical); ISA-TR12.13.01 (Combustion Analysis)

---

## IUK-T3-DIAG-386
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A DCS controls 40 loops through a single Ethernet network connecting the controller to the I/O chassis in the field. Operations reports that all 40 control loops experience simultaneous 2-second "freezes" — outputs hold last value for 2 seconds, then resume. This happens 3-4 times per hour at random intervals. The DCS controller CPU load is 35% (normal). What is the most likely cause?

**Correct Answer:**  
**Most likely cause: Network congestion or a faulty Ethernet switch/connection causing periodic packet loss or timeout on the controller-to-I/O link.**

**Required Elements:**
- Network/Ethernet issue (not DCS controller): mandatory
- I/O timeout mechanism (2 seconds): mandatory
- Specific Ethernet failure modes: mandatory
- Switch port statistics check: required for full credit

**Common Wrong Answers:**
- "DCS controller overload" — CPU is at 35%, well within normal
- "I/O chassis failure" — would be continuous, not intermittent
- "Power supply glitch" — wouldn't produce exactly 2-second freezes
- "Software bug" — wouldn't produce random-interval freezes

**Scoring Rubric:**
- Full (100%): Network cause + timeout mechanism + specific failure modes + diagnostics
- High (75%): Network cause + timeout
- Low (50%): Identifies communication issue but vague
- Zero: Blames DCS controller

**Reference:** ISA-TR18.2.6 (Alarm System); DCS Network Architecture Best Practices

---

## IUK-T3-DIAG-387
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A Venturi tube flow meter on a large water main (24-inch) reads correctly at high flows but increasingly reads HIGH at low flows (below 25% of range). The Venturi was installed 15 years ago and has never been inspected internally. What is the most likely cause?

**Correct Answer:**  
**Most likely cause: Deposit buildup (tuberculation or scale) in the Venturi throat, reducing the effective throat diameter.**

**Required Elements:**
- Throat deposit reducing diameter: mandatory
- Higher DP at reduced throat → reads HIGH: mandatory
- Worse at low flows (Reynolds number / Cd effect): mandatory
- Inspection and recalculation: required for full credit

**Common Wrong Answers:**
- "Venturi erosion" — erosion would enlarge the throat, causing LOW readings
- "Pressure tap blockage" — would affect high and low flows equally
- "Transmitter drift" — wouldn't be flow-rate-dependent
- "Air entrainment at low flow" — would cause erratic readings, not consistent high

**Scoring Rubric:**
- Full (100%): Deposit buildup + DP mechanism + low-flow sensitivity + diagnostics
- High (75%): Correct root cause + direction
- Low (50%): Identifies Venturi issue but wrong mechanism
- Zero: Wrong root cause

**Reference:** Kuphaldt LIII Ch.16; ISO 5167-4 (Venturi Tubes); ASME MFC-3M

---

## IUK-T3-DIAG-388
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A steam trap monitoring system uses acoustic sensors to detect steam trap failure. Trap #47 shows "blowing through" (failed open) based on its acoustic signature — high continuous noise. However, a downstream condensate flow check shows normal condensate volume. An IR thermometer on the trap outlet shows 250°F (close to steam temperature). Is the trap really failed? Explain.

**Correct Answer:**  
**The evidence is contradictory and requires careful analysis.**

**Required Elements:**
- Flash steam vs blowthrough distinction: mandatory
- Condensate volume as contradicting evidence: mandatory
- Acoustic sensor limitation (can't distinguish flash from blowthrough): mandatory
- Sight glass or flash calculation as confirmation: required for full credit

**Common Wrong Answers:**
- "Trust the acoustic sensor — trap is failed" — ignores the contradicting condensate evidence
- "Ignore the sensor — everything is fine" — doesn't investigate the discrepancy
- "IR reading confirms failure" — IR cannot distinguish flash steam from blowthrough at the outlet

**Scoring Rubric:**
- Full (100%): Flash steam analysis + condensate contradiction + sensor limitation + confirmation method
- High (75%): Flash steam + contradicting evidence
- Low (50%): Identifies uncertainty but no resolution
- Zero: Accepts acoustic reading without question

**Reference:** Kuphaldt LIII Ch.18 (Steam Systems); Armstrong Steam Trap Handbook

---

## IUK-T3-DIAG-389
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A single-loop PID controller operating a temperature loop suddenly shows the process variable (PV) jump from 350°F to 9999°F (over-range). The controller output immediately saturates at 0%. The RTD wires at the transmitter terminals show infinite resistance when measured with a multimeter. However, the RTD element measures 235Ω (consistent with ~350°F for a Pt100). What is the most likely cause?

**Correct Answer:**  
**Most likely cause: An open circuit between the RTD element and the transmitter — the break is in the extension wires, not the RTD element itself.**

**Required Elements:**
- Open circuit in extension cable (not RTD): mandatory
- RTD element healthy (235Ω): mandatory
- Upscale failure per NAMUR NE 43: mandatory
- Systematic continuity check from transmitter toward RTD: required for full credit

**Common Wrong Answers:**
- "RTD failed" — RTD element measures correctly at 235Ω
- "Transmitter failed" — transmitter is correctly indicating upscale alarm for open input
- "Wrong RTD type" — wouldn't show infinite resistance
- "Ground fault" — would cause erratic readings, not infinite resistance

**Scoring Rubric:**
- Full (100%): Cable open + evidence analysis + NAMUR NE 43 + systematic diagnostic
- High (75%): Correct root cause + evidence reasoning
- Low (50%): Identifies open circuit but not location
- Zero: Blames RTD or transmitter

**Reference:** Kuphaldt LIII Ch.14 (Temperature); NAMUR NE 43

---

## IUK-T3-DIAG-390
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
An annubar (averaging pitot tube) flow meter on a compressed air main shows 15% lower flow than the plant's totalizer at the air compressor discharge. Both instruments were recently calibrated. The annubar is installed 8 pipe diameters downstream of a single 90° elbow. The pipe is 6-inch Schedule 40. What is the most likely cause?

**Correct Answer:**  
**Most likely cause: Insufficient straight run after the elbow, creating a distorted velocity profile at the annubar location.**

**Required Elements:**
- Insufficient straight run / velocity profile distortion: mandatory
- Elbow effect on profile (skew + swirl): mandatory
- Straight run requirements (25-35D): mandatory
- Flow conditioner or relocation: required for full credit

**Common Wrong Answers:**
- "Annubar calibration error" — recently calibrated
- "Compressed air moisture" — both meters measure the same air
- "Compressor totalizer error" — recently calibrated
- "Pressure compensation" — if both are compensated, wouldn't cause 15% error

**Scoring Rubric:**
- Full (100%): Profile distortion + elbow effects + straight run requirements + solution
- High (75%): Correct root cause + straight run
- Low (50%): Mentions installation but no specifics
- Zero: Wrong root cause

**Reference:** Kuphaldt LIII Ch.16; ISO 3966 (Velocity Area Method); Manufacturer installation guides

---

## IUK-T3-DIAG-391
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A vibrating fork level switch (tuning fork) used as a low-level alarm on a diesel storage tank fails to alarm when the level drops below the switch point. The switch is verified to be powered and the relay output is functional (tested by manually activating). The fork is submerged in diesel when the tank is above the alarm point. When the level drops below the fork, the fork appears clean and undamaged. What is the most likely cause?

**Correct Answer:**  
**Most likely cause: A thin, viscous coating of diesel residue on the fork tines is damping the vibration enough that the switch cannot distinguish between "immersed in liquid" and "in air with coating."**

**Required Elements:**
- Diesel film coating on fork: mandatory
- Vibration damping mechanism: mandatory
- Film not visible but functionally significant: mandatory
- Cleaning + alternative technology: required for full credit

**Common Wrong Answers:**
- "Relay failure" — tested and functional per question
- "Fork mechanical damage" — appears undamaged
- "Power supply issue" — verified powered
- "Wrong switch point elevation" — the fork is at the correct level; the failure is in the sensing mechanism

**Scoring Rubric:**
- Full (100%): Film coating + damping mechanism + invisible film + solutions
- High (75%): Correct root cause + mechanism
- Low (50%): Identifies coating but vague
- Zero: Wrong root cause

**Reference:** Kuphaldt LIII Ch.15 (Level Measurement); Endress+Hauser Liquiphant Application Guide

---

## IUK-T3-DIAG-393
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
An area classification survey identifies that a new instrument junction box is installed at the boundary between a Class I, Division 1, Group D area and a Class I, Division 2, Group D area. The junction box contains terminal strips for 12 instrument loops (all 4-20 mA). The junction box is a standard NEMA 4X enclosure (not explosion-proof). Is this installation acceptable? Why or why not?

**Correct Answer:**  
**No — this installation is NOT acceptable.**

**Required Elements:**
- Division 1 requires explosion-proof or IS: mandatory
- NEMA 4X is NOT explosion-proof: mandatory
- Boundary rule (most restrictive classification governs): mandatory
- Replacement options (Ex d box, relocation, or IS certification): required for full credit

**Common Wrong Answers:**
- "NEMA 4X is fine because it's sealed" — sealed ≠ explosion-proof
- "Division 2 rules apply since it's on the boundary" — the MORE restrictive classification applies
- "4-20 mA is inherently safe" — 4-20 mA is NOT inherently intrinsically safe without certified barriers
- "Just add conduit seals" — seals don't make the box explosion-proof

**Scoring Rubric:**
- Full (100%): Not acceptable + Division 1 requirements + NEMA 4X limitation + solutions
- High (75%): Not acceptable + correct reasoning
- Low (50%): Identifies concern but wrong reasoning
- Zero: Says installation is acceptable

**Reference:** NEC Article 500/501/505; NFPA 70; Kuphaldt LIII Ch.20

---

## IUK-T3-DIAG-394
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A feedforward-plus-feedback temperature control system uses a flow measurement as the feedforward input. When the flow measurement transmitter fails high (reads 20 mA = max flow), the controller drives the heating element to maximum output even though the process doesn't need it. The temperature rises uncontrolled until the high-temperature alarm trips. What design flaw allowed this to happen and how should it be corrected?

**Correct Answer:**  
**Design flaw: The feedforward action does not have adequate limits, signal validation, or override protection — a single transmitter failure can drive the process to an unsafe condition.**

**Required Elements:**
- Feedforward overwhelmed feedback: mandatory
- Signal validation (rate of change, NAMUR): mandatory
- Feedforward output limiting: mandatory
- Override control or interlock: required for full credit

**Common Wrong Answers:**
- "The feedback controller should have caught it" — the feedback was overwhelmed
- "Just add better alarms" — alarms don't prevent the condition, they only notify
- "Tune the feedforward gain lower" — reducing gain reduces the benefit during normal operation
- "Use a more reliable transmitter" — all transmitters can fail; the design must be robust

**Scoring Rubric:**
- Full (100%): Feedforward overwhelm + signal validation + output limits + override
- High (75%): Correct analysis + two design corrections
- Low (50%): Identifies flaw but only one correction
- Zero: Doesn't identify the feedforward design issue

**Reference:** Kuphaldt LIII Ch.29 (Feedforward Control); ISA-18.2 (Alarm Management)

---

## IUK-T3-DIAG-395
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A pressure transmitter reads correctly at ambient temperature but develops a +3% error when the process temperature reaches 250°F. The transmitter specifications say "temperature effect: ±0.1% URL per 50°F." The transmitter URL is 300 PSIG and the calibrated range is 0-100 PSIG. Calculate the expected temperature effect and determine if the observed +3% error is within specification.

**Correct Answer:**  
**Temperature change:** 250°F − ambient (~70°F) = 180°F

**Required Elements:**
- Temperature effect calculation: ±1.08 PSIG or ±1.08% span: mandatory
- Comparison: 3% exceeds 1.08% specification: mandatory
- URL vs span distinction in the calculation: mandatory
- Possible causes of excessive thermal error: required for full credit

**Common Wrong Answers:**
- Calculating on span instead of URL: ±0.1% × 100 × 3.6 = 0.36% (wrong — spec is % of URL)
- "Within spec" — fails to do the math or uses wrong reference
- Using only 1 increment of 50°F instead of 3.6
- Confusing "per 50°F" with "per 100°F"

**Scoring Rubric:**
- Full (100%): Correct calculation + out of spec conclusion + URL distinction + possible causes
- High (75%): Correct calculation + conclusion
- Low (50%): Correct method but math error
- Zero: No calculation or wrong method entirely

**Reference:** Kuphaldt LIII Ch.12; ISA-S51.1 (Performance Terminology)

---

## IUK-T3-DIAG-396
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A capacitance level transmitter on a lube oil reservoir reads 100% full when the reservoir is known to be approximately half full. The transmitter was recently recalibrated. The oil was changed from ISO 32 to ISO 68 grade last week. What is the most likely cause?

**Correct Answer:**  
**The higher viscosity ISO 68 oil has a different dielectric constant than ISO 32, and the transmitter is calibrated for the old oil's Dk.** ISO 68 (heavier) oil typically has a slightly higher Dk than ISO 32 (lighter). At 50% actual level, the higher Dk produces capacitance equivalent to what the transmitter expects at 100% with the old oil. **Fix:** Recalibrate for the new oil's dielectric constant using empty and full references.

**Required Elements:**
- Dk change with oil grade: mandatory | Recalibration required: mandatory | Direction correct (higher Dk → reads high): mandatory

**Common Wrong Answers:**
- "Probe fouling" — recently recalibrated | "Electronics fault" — too coincidental with oil change | "Grounding issue" — wouldn't produce clean 100%

**Reference:** Kuphaldt LIII Ch.15

---

## IUK-T3-DIAG-397
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A control valve positioner receives a 12 mA signal (50%) but the valve position feedback shows 62%. The positioner is a digital HART type in "analog" mode. The valve was restroked last week (new packing, repacked gland). What is the most likely cause?

**Correct Answer:**  
**The positioner was not recalibrated (auto-tuned) after the valve was restroked.** Repacking changes the friction characteristics. Digital positioners learn the valve's friction profile during auto-tuning. If the auto-tune was not re-run after repacking, the positioner's internal model doesn't match the new friction, causing position error. The positioner may also have a mechanical linkage offset if the linkage was disturbed during maintenance. **Fix:** Re-run the positioner's auto-tune/calibration routine.

**Required Elements:**
- Positioner not recalibrated after restroke: mandatory | Friction profile change from new packing: mandatory | Auto-tune as fix: mandatory

**Common Wrong Answers:**
- "Signal error" — 12 mA confirmed | "Positioner hardware fault" — worked before restroke | "Wrong valve characteristic" — wouldn't change after restroke

**Reference:** Kuphaldt LIII Ch.25; Fisher DVC6200 Manual

---

## IUK-T3-DIAG-398
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A Rosemount 3051 DP transmitter configured for 0–100 inH₂O shows a reading that oscillates ±3 inH₂O at exactly 1 Hz. The process is stable (no pulsation). The oscillation persists with the transmitter isolated from the process (block valves closed, equalize valve open — should read zero). The oscillation appears on both the 4–20 mA output and the HART digital reading. What is the most likely cause?

**Correct Answer:**  
**The transmitter's internal sensor module has developed an oscillating fault — likely a failing capacitance-to-digital converter or a reference oscillator instability.** The key evidence: oscillation persists with the transmitter isolated (equalize valve open, zero DP applied), so it cannot be process-induced. Both analog and digital outputs show it, confirming the fault is in the sensor processing, not the D/A output stage. The clean 1 Hz frequency suggests an internal clock or sampling-related failure, not random noise. **Fix:** Replace the sensor module or the entire transmitter.

**Required Elements:**
- Internal sensor/electronics fault: mandatory | Isolated test rules out process: mandatory | Both outputs affected confirms sensor-level: mandatory | Replacement required: required for full credit

**Common Wrong Answers:**
- "Process pulsation" — persists when isolated | "Electrical noise" — would typically be at 60/120 Hz, not 1 Hz | "Impulse line issue" — transmitter is isolated from process

**Reference:** Kuphaldt LIII Ch.12; Rosemount 3051 Troubleshooting Guide

---

## IUK-T3-DIAG-399
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A variable area flow meter (rotameter) on a nitrogen gas line reads correctly when compared to a reference at 50 PSIG back-pressure. When the back-pressure increases to 100 PSIG (due to downstream process changes), the rotameter reads approximately 15% LOW even though actual flow hasn't changed. Why?

**Correct Answer:**  
**Rotameters are volumetric devices calibrated at a specific gas density. At 100 PSIG (higher pressure), nitrogen density increases, but the rotameter's scale assumes the original calibration density.** Higher density means the same MASS flow occupies less volume. The rotameter reads lower volumetric flow — which is physically correct for volume, but the MASS flow hasn't changed. If the intent is to measure mass flow, a density correction is needed: Q_actual = Q_indicated × √(ρ_cal/ρ_actual). At double the absolute pressure (~2× density), correction factor = √(1/2) ≈ 0.71, meaning actual flow is indicated/0.71 = ~41% higher than indicated — roughly matching the 15% discrepancy if back-pressure went from 50 to 100 PSIG gauge (~65 to 115 psia, ratio ~1.77).

**Required Elements:**
- Density change with pressure: mandatory | Volumetric vs mass flow distinction: mandatory | Correction factor formula: mandatory | Approximate calculation matching 15%: bonus

**Common Wrong Answers:**
- "Rotameter stuck" — reads correctly at 50 PSIG | "Float damaged" — wouldn't correlate with pressure | "Incorrect reading technique" — parallax doesn't change with pressure

**Reference:** Kuphaldt LIII Ch.16; ISA RP16.6

---

## IUK-T3-DIAG-400
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A plant has two identical DP flow transmitters (A and B) measuring the same orifice plate through a common manifold. Transmitter A reads 247 GPM, transmitter B reads 232 GPM. Both were calibrated last month to the same standard. The DP at A's input is 62.3 inH₂O, the DP at B's input is 55.1 inH₂O. What is the most likely cause of the discrepancy?

**Correct Answer:**  
**The common manifold has a restriction or partial blockage between the two transmitter takeoff points, creating a pressure drop that makes the two transmitters see different DPs.** With a common manifold, both transmitters should see identical DP if the manifold is unobstructed. A 7.2 inH₂O difference (62.3 - 55.1) indicates a flow restriction in the manifold between the HP or LP takeoff points for A and B. The restriction drops additional pressure in the line feeding one transmitter. Possible causes: a partially closed isolation valve, debris in the manifold, a valve packing leak creating a leak path, or a manufacturing defect in the manifold. **Fix:** Inspect and clean the manifold; verify all isolation valves fully open; blow down the manifold.

**Required Elements:**
- Manifold restriction causing different DPs: mandatory | Both transmitters correct for their respective inputs: mandatory | DP difference calculated (7.2 inH₂O): mandatory | Manifold inspection: required for full credit

**Common Wrong Answers:**
- "Transmitter calibration error" — both recently calibrated and both correctly convert their respective DP inputs | "Orifice plate issue" — both share the same orifice | "Different flow ranges" — described as identical

**Reference:** Kuphaldt LIII Ch.16; ISA RP31.1

---

## IUK-T3-DIAG-401
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A split-range pressure control system uses two valves: Valve A (vent to atmosphere, 4–12 mA = 0–100%) and Valve B (nitrogen supply, 12–20 mA = 0–100%). At controller output = 12 mA, both valves should be closed (A fully closed, B at 0%). Instead, the vessel pressure slowly rises even with both valves confirmed at 0% position. What is the most likely cause?

**Correct Answer:**  
**Most likely cause: Valve B (nitrogen supply) has a seat leak — it is not providing a bubble-tight shutoff at the 0% position.** Even with the positioner showing 0% travel, globe valves (especially those not designed for tight shutoff) can pass a small amount of gas past the seat. In a closed pressurized system, this small leak accumulates over time, causing a slow pressure rise. The rate of rise indicates the leak rate. **Alternative:** A second possible cause is nitrogen leaking past the valve packing (external leak) into the vessel through a different path, or a check valve in the nitrogen supply line not seating. **Diagnostic steps:** 1) Apply leak detection fluid to Valve B bonnet/packing; 2) Listen for seat leakage with a stethoscope at the valve outlet; 3) Close the block valve upstream of Valve B — if pressure rise stops, B is confirmed as the leak source; 4) If persistent, may need a Class V or VI shutoff valve for this service.

**Required Elements:**
- Valve B seat leakage: mandatory | Slow accumulation mechanism: mandatory | Block valve isolation test: mandatory | Shutoff class consideration: bonus

**Common Wrong Answers:**
- "Controller output not exactly 12 mA" — valves confirmed at 0% | "Valve A leaking" — A vents TO atmosphere; a leak would reduce pressure | "Process generating pressure" — not described as a reactive vessel

**Reference:** Kuphaldt LIII Ch.25; ISA-75.02 (Valve Seat Leakage); ANSI/FCI 70-2

---

## IUK-T3-DIAG-402
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A FOUNDATION Fieldbus H1 segment has 8 devices. Segment diagnostics show normal communication for all devices, but the control loop update rate has degraded from the designed 250 ms to approximately 800 ms, causing sluggish control. No new devices have been added. What is the most likely cause?

**Correct Answer:**  
**Most likely cause: One or more function blocks have been misconfigured or added to the schedule, increasing the macrocycle time.** FF H1 uses a deterministic schedule (macrocycle) that allocates time slots for each function block execution and data publication. If someone added diagnostic function blocks, changed execution rates, or enabled additional scheduled communications (e.g., trend blocks, alert blocks), the macrocycle time increases. At 8 devices with 250 ms designed macrocycle, the schedule was optimized. Additional blocks push it to 800 ms. **Alternatively:** A device may have a firmware issue causing slow function block execution, or the Link Active Scheduler (LAS) may be experiencing token-passing delays from a device that takes too long to respond. **Fix:** Review the FF schedule in the host system; identify any blocks added or timing changes; re-optimize the macrocycle; check individual device function block execution times.

**Required Elements:**
- Macrocycle/schedule bloat: mandatory | Function block misconfiguration or addition: mandatory | LAS scheduling concept: mandatory | Schedule optimization as fix: required for full credit

**Common Wrong Answers:**
- "New device added" — question states none added | "Cable fault" — would cause communication errors, not slower schedule | "Power supply issue" — would cause dropouts, not slower update rate

**Reference:** Kuphaldt LIII Ch.22; ISA-50.02; IEC 61158

---

## IUK-T3-DIAG-403
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A thermocouple temperature transmitter on a catalytic reactor reads normally for 6 hours after startup, then begins reading approximately 50°F high compared to a reference pyrometer. The error gradually increases over the next 4 hours. The thermocouple is Type K (Chromel-Alumel) operating at 1600°F in a reducing atmosphere with traces of sulfur. What is the most likely cause?

**Correct Answer:**  
**Most likely cause: Preferential oxidation of the Chromel (Ni-Cr) leg in the sulfur-laden reducing atmosphere, causing EMF drift — a condition known as "green rot."** Type K thermocouples are susceptible to preferential oxidation of the chromium in the Chromel leg when exposed to reducing atmospheres, especially with sulfur present, in the 1500–1800°F range. The chromium depletes from the alloy, changing the Seebeck coefficient and causing a positive EMF drift (reads HIGH). This is a progressive degradation — explaining the gradual increase over hours. The phenomenon is called "green rot" because the depleted Chromel wire develops a green oxide layer. **Fix:** Replace with Type N (Nicrosil-Nisil) which is specifically designed to resist this failure mode, or use a protective sheath that excludes the reducing atmosphere.

**Required Elements:**
- Green rot / preferential oxidation of Chromel: mandatory | Sulfur + reducing atmosphere + temperature range as triggers: mandatory | Progressive degradation matches symptom: mandatory | Type N as alternative: required for full credit

**Common Wrong Answers:**
- "Normal TC drift" — 50°F+ drift in 10 hours is not normal | "CJC error" — wouldn't develop progressively | "Transmitter fault" — wouldn't correlate with operating conditions | "Sheath grounding" — would cause noise, not progressive drift

**Reference:** Kuphaldt LIII Ch.14; ASTM E230; IEC 60584

---

## IUK-T3-DIAG-404
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A radar level transmitter (26 GHz pulse) on a sulfuric acid storage tank consistently reads 6 inches lower than actual level verified by a sight glass. The error is constant across the entire level range. The transmitter was installed with the manufacturer's default settings and the antenna type is a PTFE-lined horn. What is the most likely cause?

**Correct Answer:**  
**Most likely cause: The reference point offset (antenna delay / dead zone) is not correctly configured.** Every radar transmitter has a reference point — the physical location from which the distance measurement starts (usually the flange face or horn tip). If the transmitter is installed with a standoff, extension, or nozzle that isn't accounted for in the configuration, the entire measurement shifts by a constant amount. A constant 6-inch error across all levels = a fixed offset in the reference point configuration. **Additionally:** The PTFE liner in the horn has a different propagation velocity than air. If the transmitter doesn't compensate for the slower propagation through PTFE, it adds a small constant error (the signal travels through the liner at ~70% of air speed, adding apparent distance). **Fix:** Measure the actual reference point distance (flange face to tank datum) and enter it in the transmitter configuration. Apply the PTFE antenna correction if available.

**Required Elements:**
- Reference point offset: mandatory | Constant error = fixed configuration issue: mandatory | PTFE propagation velocity as contributing factor: bonus | Configuration correction: required for full credit

**Common Wrong Answers:**
- "Sulfuric acid low Dk" — H₂SO₄ has high Dk (~80+); wouldn't cause consistent offset | "False echo" — would cause erratic readings, not constant offset | "Temperature effect" — would vary, not constant

**Reference:** Kuphaldt LIII Ch.15; Emerson/VEGA Radar Configuration Guide

---

## IUK-T3-DIAG-405
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A PLC receives a 4–20 mA signal from a flow transmitter through an analog input card with 12-bit resolution over a 0–20 mA range. The operator reports that the flow reading "jumps" between two values (e.g., 145.2 and 145.6 GPM) and never displays intermediate values. The transmitter output on a precision milliammeter reads a stable 11.843 mA. What is the most likely cause?

**Correct Answer:**  
**Most likely cause: The 12-bit ADC resolution is insufficient to resolve the intermediate values — the signal falls between two adjacent digital counts.** A 12-bit ADC over 0–20 mA has 4096 counts. Resolution = 20/4096 = **0.00488 mA per count.** If the flow span is 0–500 GPM over 4–20 mA (16 mA span), each count = 500/4096 × (20/16) ≈ 0.153 GPM per count over the full 0-20 range, or ~500 × 0.00488/16 ≈ 0.15 GPM per count over the 4-20 span. The 0.4 GPM jump (145.2 to 145.6) equals ~2-3 counts, which means the analog signal is sitting right at a count boundary and noise is toggling it between adjacent counts. This is normal ADC quantization behavior, not a fault. **Fix:** Apply a deadband or averaging filter in the PLC/DCS to suppress the toggling; or upgrade to a 16-bit input card (65536 counts = 0.008 GPM resolution).

**Required Elements:**
- ADC resolution / quantization: mandatory | 12-bit calculation (4096 counts): mandatory | Signal at count boundary: mandatory | Deadband or higher-resolution card as fix: required for full credit

**Common Wrong Answers:**
- "Transmitter oscillating" — milliammeter shows stable output | "Loose wiring" — would cause random noise, not two fixed values | "PLC software bug" — it's doing exactly what it should with the available resolution

**Reference:** Kuphaldt LIII Ch.21 (PLCs); ADC Resolution Theory

---

## IUK-T3-DIAG-406
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A differential pressure level measurement on a sealed (pressurized) vessel with a dry reference leg reads 25% when the vessel is actually empty (verified by sight glass and drain). The vessel pressure is 50 PSIG nitrogen blanket. The transmitter is calibrated for 0–120 inH₂O with 4–20 mA output. What is the most likely cause?

**Correct Answer:**  
**Most likely cause: The dry reference leg (LP side) is at a lower elevation than the HP (bottom) tap, or the LP connection doesn't properly see the vessel vapor space pressure — creating a static DP even with an empty vessel.** In a sealed vessel with a dry reference leg, the LP tap connects to the vapor space. If the LP tap is below the HP tap (or the impulse line routing creates a liquid trap), the LP side may see a lower pressure than the actual vapor space pressure, or liquid may have condensed in the LP line, adding an unexpected hydrostatic head. At 25% reading = 0.25 × 120 = 30 inH₂O false DP. This could be caused by approximately 30 inches (2.5 feet) of liquid trapped in the LP impulse line (if water: 30 inH₂O = 30 inches of water column). **Fix:** Verify LP line routing has continuous slope to drain any condensate; purge the LP line; verify both taps see the same static pressure when vessel is empty.

**Required Elements:**
- LP line liquid trap or elevation error: mandatory | Static DP with empty vessel: mandatory | 30 inH₂O calculation: mandatory | LP line purge/verification: required for full credit

**Common Wrong Answers:**
- "Transmitter zero shift" — would be fixed, not elevation-dependent | "Vessel not actually empty" — verified by sight glass and drain | "Wrong calibration range" — wouldn't cause non-zero at empty

**Reference:** Kuphaldt LIII Ch.15

---

## IUK-T3-DIAG-407
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A clamp-on ultrasonic flow meter (transit-time type) on a 4-inch stainless steel pipe carrying clean water reads approximately 30% lower than an inline magnetic flow meter downstream. Both meters were recently calibrated. The pipe wall thickness is 0.237 inches (Schedule 40). The ultrasonic meter was set up with pipe OD = 4.5 inches and wall thickness = 0.237 inches. What is the most likely cause?

**Correct Answer:**  
**Most likely cause: Internal pipe wall coating, corrosion, or liner that reduces the actual internal diameter below the nominal 4.026 inches, but the ultrasonic meter is calculating flow area based on the nominal ID.** Transit-time ultrasonic meters calculate volumetric flow from velocity × area. If the actual ID is smaller due to scale buildup, tuberculation, or a pipe liner, the meter uses too large an area in its calculation, producing a LOW reading. A 30% volume error corresponds to approximately 16% diameter reduction (since area ∝ D², 0.84² ≈ 0.71 — roughly 30% area reduction). This means ~0.64 inches of total buildup (0.32 inches per side), which is plausible in older steel pipe. **Fix:** Measure actual pipe ID with a UT thickness gauge from the outside; enter the actual wall thickness (or actual ID) into the meter configuration.

**Required Elements:**
- Internal buildup reducing actual ID: mandatory | Area calculation error: mandatory | 30% area vs ~16% diameter relationship: mandatory | UT wall thickness measurement: required for full credit

**Common Wrong Answers:**
- "Wrong pipe data entered" — OD and wall thickness match Schedule 40 nominal | "Coupling gel dried out" — would cause signal loss, not 30% offset | "Mag meter wrong" — recently calibrated

**Reference:** Kuphaldt LIII Ch.16; Ultrasonic Flow Meter Installation Guide

---

## IUK-T3-DIAG-408
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A PID flow control loop shows excellent setpoint tracking but very poor disturbance rejection — when the upstream pressure changes, it takes 5 minutes for the flow to return to setpoint. The tuning parameters are Kp=0.8, Ti=120 seconds, Td=0. The valve responds within 2 seconds to any signal change. What specific tuning adjustment would most improve disturbance rejection?

**Correct Answer:**  
**Decrease Ti (integral time) — the integral action is too slow.** With Ti = 120 seconds, the integral term accumulates correction very slowly. Good setpoint tracking with poor disturbance rejection is the classic signature of integral action that is adequate for slow setpoint changes but too slow for step disturbances. When a disturbance occurs (upstream pressure change), the proportional term provides an immediate but incomplete correction (Kp = 0.8 means only 80% of the error is corrected proportionally). The remaining error must be corrected by the integral term, which at Ti = 120 seconds takes many integral time constants to eliminate the offset. **Recommended fix:** Reduce Ti to approximately 30-60 seconds. This speeds up the integral response without dramatically affecting setpoint tracking. **Do NOT simply increase Kp** — increasing gain improves both setpoint and disturbance response but risks oscillation. The selective symptom (good setpoint, bad disturbance) points specifically to integral speed.

**Required Elements:**
- Reduce Ti (not increase Kp): mandatory | Integral too slow as specific diagnosis: mandatory | Good setpoint / poor disturbance = integral fingerprint: mandatory | Approximate new Ti recommendation: bonus

**Common Wrong Answers:**
- "Increase Kp" — would improve disturbance rejection but also risk oscillation; doesn't explain why setpoint tracking is already good | "Add derivative" — derivative improves response to rate of change but doesn't address the offset elimination speed | "Valve is too slow" — 2-second response is adequate

**Reference:** Kuphaldt LIII Ch.28-29; ISA Practical PID Tuning

---

## IUK-T3-DIAG-409
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A thermowell-mounted Type K thermocouple on a gas turbine exhaust (1200°F) reads correctly at steady state but shows a 200°F overshoot during rapid temperature transients (e.g., load changes). The thermocouple without the thermowell would not show this overshoot. What is causing the apparent overshoot and is it a real temperature or a measurement artifact?

**Correct Answer:**  
**This is a measurement artifact, not a real temperature overshoot.** The thermowell has a large thermal mass compared to the bare thermocouple. During rapid transients, the actual gas temperature changes quickly, but the thermowell temperature lags behind due to its thermal mass. However, the APPARENT overshoot occurs when the gas temperature rises quickly and then levels off — the thermowell continues to absorb heat from the gas and momentarily reaches a temperature HIGHER than the gas (due to radiation heat transfer from surrounding hot surfaces), OR the phenomenon is caused by the thermowell's time constant creating a measurement lag that, combined with process control dynamics, causes the appearance of overshoot. **More precisely:** The 200°F apparent overshoot is most likely caused by the thermowell acting as a first-order lag element in the measurement chain. When the gas temperature steps up and then partially decreases as control action takes effect, the thermowell is still rising (lagging behind the true gas temperature). The thermocouple reads the thermowell temperature, which at that moment is ABOVE the current gas temperature — appearing as overshoot when trended against the actual gas temperature. **This is NOT the gas being 200°F hotter than steady state — it's the thermowell playing catch-up.**

**Required Elements:**
- Measurement artifact (not real overshoot): mandatory | Thermowell thermal mass / time constant: mandatory | Lag effect during transients: mandatory | Bare TC doesn't show it (confirms artifact): required for full credit

**Common Wrong Answers:**
- "Real temperature overshoot" — the bare TC doesn't show it | "Thermocouple failure" — reads correctly at steady state | "CJC error" — wouldn't be transient-dependent

**Reference:** Kuphaldt LIII Ch.14; ASME PTC 19.3

---

## IUK-T3-DIAG-410
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A plant has 6 identical level transmitters on 6 identical tanks. Five transmitters read within ±0.5% of each other when tanks are at the same level. The sixth transmitter consistently reads 4% high. It was calibrated last month and the calibration certificate shows it passed. The transmitter is the same model, range, and configuration. What is the most likely cause?

**Correct Answer:**  
**Most likely cause: The mounting elevation or orientation of the sixth transmitter differs from the other five.** If the transmitter's HP diaphragm is mounted 4% of span lower than the standard position (or the LP reference is higher), it sees additional hydrostatic head = reads high. For a 0-100 inH₂O range, 4% = 4 inH₂O, which corresponds to approximately 4 inches of liquid head difference in water service. This could be caused by: the transmitter being mounted a few inches lower on the tank nozzle, a different length of impulse line, a mounting bracket at a slightly different elevation, or the process tap being at a different elevation on this tank. **The calibration passed because calibration is done against an applied pressure standard — not against the actual installation geometry.** Calibration verifies the transmitter converts pressure to mA correctly; it doesn't verify the installation is identical to the other 5. **Fix:** Verify the mounting elevation against the installation drawing; apply a zero offset if the elevation difference is confirmed and documented.

**Required Elements:**
- Mounting elevation difference: mandatory | Calibration doesn't check installation geometry: mandatory | 4 inH₂O ≈ 4 inches physical difference: mandatory | Zero offset or remount as fix: required for full credit

**Common Wrong Answers:**
- "Calibration error" — cal certificate shows pass | "Transmitter model difference" — described as identical | "Different tank geometry" — described as identical tanks | "Process fluid different" — same process across all tanks

**Reference:** Kuphaldt LIII Ch.15; ISA RP31.1

---

## IUK-T3-DIAG-412
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A positive displacement flow meter on a fuel oil line shows pulsating flow readings (±5%) at a frequency of approximately 0.5 Hz, even though the process flow is steady. A downstream pressure gauge also shows 0.5 Hz pulsation (±3 PSIG). The PD meter is a gear type. What is causing the pulsation?

**Correct Answer:**  
**The PD meter itself is causing the pulsation — this is inherent to positive displacement measurement.** Gear-type PD meters trap discrete volumes of fluid between gear teeth and transfer them from inlet to outlet. Each tooth engagement creates a small pressure pulse as the trapped volume is displaced. The 0.5 Hz frequency corresponds to the gear rotation speed × number of teeth. The flow pulsation is the PD meter's volumetric displacement cycle showing up in the measurement. The downstream pressure pulsation confirms the meter is mechanically imposing pulsation on the line. **This is normal for PD meters and is not a process disturbance.** To reduce pulsation effects: install a pulsation dampener downstream, increase the damping time constant on the flow indication, or use a larger meter (lower speed for same flow = lower pulsation frequency and amplitude).

**Required Elements:**
- PD meter inherent pulsation: mandatory | Gear tooth engagement mechanism: mandatory | Pressure pulsation confirms source: mandatory | Dampener solution: bonus

**Common Wrong Answers:**
- "Pump pulsation upstream" — process is described as steady flow | "Cavitation" — pressure is adequate (no low-pressure indication) | "Air entrainment" — would be irregular, not 0.5 Hz | "Meter failure" — this is normal PD meter behavior

**Reference:** Kuphaldt LIII Ch.16; API MPMS Chapter 5.2

---

## IUK-T3-DIAG-413
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A pressure transmitter on a steam header shows a reading that gradually INCREASES by 2 PSIG over 30 minutes after the block valve is closed for maintenance. No process connection exists — the transmitter is completely isolated. The transmitter was at 150 PSIG when the valve was closed. After 30 minutes it reads 152 PSIG. What is happening?

**Correct Answer:**  
**The steam in the impulse line is cooling and condensing, but the reading is going UP, which seems counterintuitive.** When steam condenses in the sealed impulse line after isolation, the condensate occupies less volume. In a sealed system (closed block valve, sealed transmitter), the condensation creates a partial vacuum — pressure should DROP. But the reading is rising.

**Required Elements:**
- Thermal effect on sensor (not process pressure change): mandatory | Heat transfer from hot impulse line to transmitter: mandatory | Temperature coefficient of zero: mandatory | Thermal equilibrium concept: required for full credit

**Common Wrong Answers:**
- "Pressure actually rising" — system is isolated, no pressure source | "Condensation increasing pressure" — condensation reduces volume/pressure in a sealed system | "Transmitter failure" — 2 PSIG in 30 min is within thermal spec

**Reference:** Kuphaldt LIII Ch.12; Transmitter Temperature Specifications

---

## IUK-T3-DIAG-414
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A batch weighing system must achieve ±0.1% accuracy for ingredient dosing. The load cells are rated at 0.02% combined error. The system consistently under-doses by 0.3% on every batch. The error is consistent regardless of ingredient or batch size. What is the most likely cause?

**Correct Answer:**  
**Most likely cause: Piping, conduit, or mechanical connections to the vessel are transmitting force to the load cells, effectively supporting part of the vessel weight externally (a "shunt load path").** If rigid piping, electrical conduit, or ductwork connects the weighed vessel to the building structure, these connections create alternative load paths that bypass the load cells. The shunt path carries a fixed percentage of the total weight, causing consistent under-reading regardless of batch size or ingredient.

A 0.3% shunt means approximately 0.3% of the vessel + contents weight is carried by the piping/conduit rather than the load cells. This is consistent across all batches because the stiffness ratio between the shunt path and the load cells is constant.

**Required Elements:**
- Shunt load path from piping/conduit: mandatory | Consistent percentage = stiffness ratio: mandatory | Load cell accuracy is adequate: mandatory | Flexible connections as fix: required for full credit

**Common Wrong Answers:**
- "Load cell error" — 0.02% rated, not the issue | "Calibration drift" — consistent error, not random | "Ingredient density variation" — consistent regardless of ingredient | "Software scaling error" — would scale with batch size differently

**Reference:** Kuphaldt LIII Ch.15; OIML R60; Scale Manufacturers Association Load Cell Application Guide

---

## IUK-T3-DIAG-415
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
An Allen-Bradley SLC-500 PLC has a timer instruction (TON) with a preset of 10.0 seconds. Operations reports that the actual timed delay is approximately 10.3 seconds measured with a stopwatch. The PLC scan time is 15 ms. Is this timer error acceptable, and what causes it?

**Correct Answer:**  
**The 0.3-second error (3%) is caused by the PLC scan time and is a normal characteristic of software-based timers.** PLC timers update once per scan. A TON instruction only checks its enabling condition and increments its accumulator once each scan cycle. With a 15 ms scan time, the timer resolution is 15 ms. However, the important factor is that the timer's DONE bit is only set when the program evaluates it during a scan. The worst-case timer accuracy is: actual time = preset ± (2 × scan time) = 10.0 ± 0.030 seconds.

A 0.3-second error exceeds the expected 2-scan-time tolerance (30 ms). This suggests either: 1) The scan time varies (not constant 15 ms — it may spike to 150 ms under certain conditions); or 2) The stopwatch measurement is imprecise (human reaction time is ±0.1-0.3 seconds); or 3) There is additional code execution between the timer DONE bit and the physical output energizing (output latency).

**Required Elements:**
- Scan-time-based timer resolution: mandatory | 2× scan time worst-case: mandatory | Stopwatch measurement includes human error: mandatory | Output latency consideration: bonus

**Common Wrong Answers:**
- "PLC timer is broken" — 0.3s is within human measurement error | "Scan time too slow" — 15 ms is adequate for 10-second timing | "Wrong time base" — SLC-500 timer time base is 0.01s, not the issue

**Reference:** Kuphaldt LIII Ch.21; Allen-Bradley SLC-500 Programming Manual

---

## IUK-T3-DIAG-416
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A differential pressure transmitter measuring flow through an orifice plate suddenly reads 75% higher than the actual flow. Investigation reveals that the orifice plate was installed backward (upstream face downstream) during a recent maintenance activity. Why does the backward plate read higher, and by how much would you expect the error to be?

**Correct Answer:**  
**A backward orifice plate reads HIGHER DP than a correctly installed plate for the same flow rate.** The upstream face of an orifice plate has a sharp, square edge that creates a well-defined vena contracta. The downstream face has a beveled (chamfered) edge. When installed backward: 1) The beveled edge is now upstream, creating a less defined contraction and a different discharge coefficient; 2) The sharp edge is now downstream, creating more turbulence and a larger permanent pressure loss; 3) The pressure recovery downstream is worse, resulting in a HIGHER DP across the plate for the same flow.

Since Q ∝ √(DP), a 75% higher flow reading means DP is approximately 1.75² = **3.06× higher** than expected. This is a larger increase than typically caused by reversal alone (usually 5-15% DP increase). The 75% flow error may also be compounded by the pressure taps now being on the wrong sides relative to the plate geometry.

**Required Elements:**
- Sharp edge vs bevel direction: mandatory | Higher DP with backward installation: mandatory | Q ∝ √DP relationship applied: mandatory | Expected error magnitude (3-15% DP): bonus

**Common Wrong Answers:**
- "Backward plate reads lower" — wrong direction | "No effect — plate is symmetrical" — orifice plates are NOT symmetrical | "Flow calculation is wrong" — the plate geometry is the issue

**Reference:** ISO 5167; Kuphaldt LIII Ch.16

---

## IUK-T3-DIAG-417
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A HART-enabled temperature transmitter is configured via HART for a 0–500°F range with a 4–20 mA output. The DCS shows 45.0% (225°F). A HART communicator connected at the transmitter shows PV = 301°F. Why do the DCS and HART readings disagree?

**Correct Answer:**  
**The analog 4-20 mA output and the digital HART PV can be independently configured and may have different ranges or damping settings.** In a HART transmitter, the digital PV value represents the actual sensor reading, while the analog 4-20 mA output can be configured with a different range, trim, or transfer function. If someone reconfigured the HART digital range without updating the analog output range (or vice versa), the two outputs diverge.

**Required Elements:**
- Analog and HART digital can be independently configured: mandatory | Range mismatch or damping difference: mandatory | DCS scaling must match analog range: mandatory | Verification procedure: required for full credit

**Common Wrong Answers:**
- "Transmitter failure" — both outputs are functioning, just different | "HART communicator error" — reading directly from transmitter | "DCS scaling wrong" — possible, but doesn't explain the transmitter-level disagreement

**Reference:** Kuphaldt LIII Ch.22 (HART Protocol); HART Communication Foundation

---

## IUK-T3-DIAG-418
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A control valve on a liquid chlorine service passes a leakage test at the shop (Class V, <0.5 ml/min at 200 PSIG water). When installed in the plant, the valve leaks noticeably in the closed position. The process operates at 100 PSIG with liquid chlorine at 70°F. What is the most likely cause of the difference?

**Correct Answer:**  
**Most likely cause: The valve was tested with water, but liquid chlorine has significantly different physical properties that affect sealing.** Liquid chlorine at 70°F has a much lower viscosity than water (Cl₂ viscosity ≈ 0.35 cP vs water ≈ 1.0 cP) and lower surface tension. Low viscosity fluids leak through smaller gaps that water cannot penetrate. The seat surfaces that provided Class V shutoff with water may have microscopic imperfections that water bridges over (surface tension) but chlorine flows through.

**Required Elements:**
- Viscosity/surface tension difference between water and Cl₂: mandatory | Lower viscosity penetrates smaller gaps: mandatory | Material compatibility concern: mandatory | Tighter shutoff class or different test fluid: required for full credit

**Common Wrong Answers:**
- "Valve was damaged during installation" — passed shop test, so physically intact | "Higher process pressure" — process is LOWER than test pressure (100 vs 200 PSIG) | "Wrong valve type" — passed the Class V test, just with the wrong fluid

**Reference:** Kuphaldt LIII Ch.25; ANSI/FCI 70-2; Chlorine Institute Pamphlet 6

---

## IUK-T3-DIAG-419
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A DCS analog output card drives a 4–20 mA signal to a control valve positioner. The DCS command is 50% (12 mA). The positioner receives only 10.5 mA. The cable resistance is 30Ω total and the DCS output is a voltage-source type with a 250Ω series resistor. What is happening?

**Correct Answer:**  
**The DCS output card is a voltage-source type, not a current-source type. With a voltage source, the output current depends on the total loop impedance, and any additional load reduces the current.** 

For a voltage-source output at 50% (targeting 12 mA):
The DCS outputs a voltage that, across the expected impedance, should produce 12 mA. Expected impedance: 250Ω (series) + positioner input impedance. If the positioner has an input impedance of ~500Ω (typical for a pneumatic positioner's I/P converter):

Expected: V = 12 mA × (250 + 500) = 12 × 750 = 9.0V
With cable resistance added: total R = 250 + 500 + 30 = 780Ω
Actual current: I = 9.0V / 780Ω = **11.54 mA** — not 10.5 mA

The 10.5 mA reading suggests higher-than-expected impedance. Possible additional resistance sources: corroded terminals, partially broken wire (increased resistance), or an additional device in the loop (chart recorder, indicator) that wasn't accounted for.

**Required Elements:**
- Voltage source vs current source distinction: mandatory | Loop impedance affects output: mandatory | Additional resistance in loop: mandatory | Impedance check: required for full credit

**Common Wrong Answers:**
- "DCS output card fault" — it's outputting the correct voltage for its configuration | "Positioner drawing too much current" — positioner is passive | "Cable too long" — 30Ω is modest

**Reference:** Kuphaldt LIII Ch.12; DCS Analog Output Specifications

---

## IUK-T3-DIAG-420
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
An oxygen analyzer (paramagnetic type) on an inert gas blanket system reads 0.8% O₂ when the system should be <0.1% O₂. A grab sample analyzed by a different lab instrument confirms 0.05% O₂. The analyzer was calibrated with certified zero gas (100% N₂) and span gas (1.0% O₂ in N₂) last week and passed. The sample system has a 1/4" SS sample line with a membrane dryer. What is the most likely cause?

**Correct Answer:**  
**Most likely cause: Air permeation through the membrane dryer.** Membrane dryers (Nafion or similar) remove moisture by allowing water vapor to permeate through a membrane to a dry sweep gas. However, these membranes are also slightly permeable to oxygen and nitrogen. At very low O₂ concentrations (<0.1%), even a small amount of air permeation through the membrane contributes a significant relative error. The atmosphere surrounding the membrane (ambient air at 20.9% O₂) permeates inward, contaminating the sample with atmospheric oxygen.

**Required Elements:**
- Membrane dryer O₂ permeation: mandatory | Low-concentration sensitivity to contamination: mandatory | Why calibration passed (higher concentration): mandatory | Alternative dryer technology: required for full credit

**Common Wrong Answers:**
- "Analyzer drift" — calibrated last week and passed | "Sample line leak" — would affect lab sample too (taken from same point) | "Process actually has 0.8% O₂" — grab sample confirms 0.05%

**Reference:** Kuphaldt LIII Ch.17; Servomex Paramagnetic O₂ Analyzer Application Guide

---

## IUK-T3-DIAG-421
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A motor-operated valve (MOV) used as a block valve fails to open when commanded from the DCS. The motor draws current briefly (confirmed by ammeter) then the overload trips. The valve was last operated 18 months ago and operated normally at that time. The motor is 480 VAC, 3-phase. What is the most likely cause?

**Correct Answer:**  
**Most likely cause: The valve internals are seized or stuck from corrosion/deposits accumulated over 18 months of non-operation, and the motor cannot develop enough torque to break the valve free.** When MOVs sit idle for extended periods, process deposits, corrosion products, or packing compression can bond the stem, plug, or wedge in position. The motor starts, encounters excessive torque demand, and the overload protection trips to prevent motor burnout.

**Required Elements:**
- Valve seized from non-operation: mandatory | Overload trips from excessive torque: mandatory | Manual operation test: mandatory | Periodic exercise program: required for full credit

**Common Wrong Answers:**
- "Motor failure" — motor draws current (proving it energizes) before overload trips | "Electrical wiring issue" — motor is running, just overloading | "DCS command error" — motor responds to command

**Reference:** Kuphaldt LIII Ch.25; IEEE C37.96 (MOV Protection); NUREG-1275 Vol.12 (MOV Performance)

---

## IUK-T3-DIAG-422
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
Two pressure transmitters on the same process tap, connected through a 5-valve manifold, show a 3 PSIG disagreement. Transmitter A reads 497 PSIG, Transmitter B reads 500 PSIG. When the equalizing valve is opened, both read 498.5 PSIG. When the equalizing valve is closed again, A returns to 497 and B to 500. Both passed calibration last month. What is happening?

**Correct Answer:**  
**Most likely cause: the two transmitters have different zero / calibration offsets, and the equalizing valve simply forces them to a shared midpoint when opened.**

The key clue is that the disagreement is repeatable:
- A = 497
- B = 500
- equalize open → both settle to **498.5**
- equalize closed → each returns to its prior indication.

That behavior is much more consistent with **instrument offset** than with a static-process or line-restriction problem. Under static conditions, a restriction should not sustain a permanent 3-psi pressure difference from the same tap.

So the best diagnosis is:
- one or both transmitters are offset,
- opening the equalizer averages the two pressures seen by the sensing elements,
- closing it reveals the individual instrument offsets again.

**Required Elements:**
- Zero offset on one or both transmitters: mandatory | Equalize valve averages the two readings: mandatory | Precision zero check required: mandatory | Static conditions eliminate restriction as cause: bonus

**Common Wrong Answers:**
- "Block valve restriction" — static conditions, no flow | "Impulse line blockage" — equalize returns them to average, proving both paths work | "Process pressure difference" — same tap

**Reference:** Kuphaldt LIII Ch.12; 5-Valve Manifold Operation

---

## IUK-T3-DIAG-423
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A magnetic flow meter on a water line reads zero flow. The pipe is full and flowing (verified by downstream discharge). The transmitter displays "Empty Pipe" alarm. The electrode resistance-to-ground tests at 2Ω for both electrodes (specification: 100Ω to 10MΩ). What is the most likely cause?

**Correct Answer:**  
**The electrodes are short-circuited to ground (pipe wall), reading 2Ω against a minimum specification of 100Ω.** This low resistance means the electrodes are electrically connected to the grounded pipe through a conductive path — likely conductive deposits (scale, metalite, or conductive biofilm) bridging from the electrode to the pipe wall, or a damaged electrode insulator. With the electrodes shorted to ground, the flow-induced voltage cannot develop between the electrodes (it's immediately shunted to ground). The transmitter cannot distinguish this from an empty pipe condition (also low impedance) → triggers "Empty Pipe" alarm and reads zero.

**Required Elements:**
- Electrode-to-ground short circuit: mandatory | 2Ω vs 100Ω minimum: mandatory | Flow voltage shunted to ground: mandatory | Cleaning/inspection: required for full credit

**Common Wrong Answers:**
- "Empty pipe" — pipe is verified full | "Transmitter failure" — correctly detecting the low electrode resistance | "Grounding issue" — the problem IS the grounding, but at the electrode, not the external system | "Wrong flow direction" — wouldn't cause zero reading

**Reference:** Kuphaldt LIII Ch.16; IEC 60534 (Magnetic Flow Meters)

---

## IUK-T3-DIAG-424
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A feedwater flow control valve on a boiler system hunts continuously (±5% oscillation around setpoint) when the boiler load is below 30%. Above 30% load, control is stable. The valve is a 4-inch globe with equal-percentage trim, Cv = 80. At 30% boiler load, the required Cv is approximately 8. What is the control problem?

**Correct Answer:**  
**The control valve is severely oversized for low-load operation.** At 30% boiler load requiring Cv = 8, the valve operates at 8/80 = 10% of its rated Cv. For an equal-percentage trim, 10% Cv corresponds to approximately 20-25% valve travel (depending on rangeability). At this low travel: 1) Small changes in valve position produce large changes in flow (high installed gain); 2) The valve is in the region where stiction has the greatest effect relative to the signal change; 3) The controller's proportional action produces very small signal changes that are within the valve's deadband; 4) The controller integral action winds up, overcorrects, and the cycle repeats.

**Required Elements:**
- Oversized valve at low load: mandatory | High installed gain at low travel: mandatory | Cv ratio analysis (8/80 = 10%): mandatory | Split range or gain scheduling fix: required for full credit

**Common Wrong Answers:**
- "PID tuning" — tuning can't overcome a valve that's 10× oversized | "Valve stiction" — contributes but not the root cause | "Boiler dynamics" — stable above 30% with same boiler

**Reference:** Kuphaldt LIII Ch.25 + Ch.29; ISA-75.01 (Valve Sizing)

---

## IUK-T3-DIAG-425
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A plant installs a new smart transmitter with HART 7 protocol. The existing HART modem (HART 5 compatible) can poll the transmitter and read the PV, but cannot access the advanced diagnostics menu. No error message is displayed — the diagnostics simply don't appear. What is happening?

**Correct Answer:**  
**HART protocol versions are backward compatible for basic functions (PV, range, trim) but advanced features require matching protocol versions.** HART 7 introduced new commands and device descriptions (DDs) that HART 5 equipment doesn't recognize. The HART 5 modem uses a Device Description (DD) file that doesn't include the HART 7 diagnostic commands. When the modem tries to access these commands, it simply doesn't find them in its DD library and doesn't display them. No error occurs because the modem doesn't know the commands exist — it's not a failure, it's an absence.

**Required Elements:**
- HART version compatibility (backward compatible for basic): mandatory | DD file missing HART 7 commands: mandatory | No error (commands simply absent): mandatory | DD update or modem upgrade: required for full credit

**Common Wrong Answers:**
- "Transmitter fault" — basic PV reads correctly | "Modem broken" — reads basic parameters fine | "HART disabled" — communication is established | "Diagnostics not supported" — they are supported in HART 7, just not visible to HART 5 tools

**Reference:** Kuphaldt LIII Ch.22; HART Communication Foundation; IEC 62591

---

## IUK-T3-DIAG-426
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A butterfly control valve on a cooling water system starts oscillating when the controller requests more than 80% opening. Below 80%, control is smooth. The actuator is a spring-return pneumatic with a positioner. The valve has a 60° rotation range (closed to full open). What is the most likely cause?

**Correct Answer:**  
**Most likely cause: The valve is entering the "stall" or "instability" region of its torque curve near full open.** Butterfly valves experience a torque reversal phenomenon: the hydrodynamic torque acting on the disc changes direction as the valve approaches full open. Near 60-70° opening (in a 0-90° range), the flow torque can reverse from closing to opening. If the valve's 60° range maps 80% travel to approximately 48° disc angle, this is approaching the unstable zone.

At this angle: 1) The hydrodynamic torque may oscillate between opening and closing as the flow interacts with the disc; 2) The actuator spring and positioner fight against the changing torque; 3) The positioner can't stabilize the valve because the process itself is providing oscillating force.

**Required Elements:**
- Butterfly torque reversal/instability at high opening: mandatory | High gain at near-full-open: mandatory | Travel limit or stronger actuator: mandatory | Disc angle analysis: bonus

**Common Wrong Answers:**
- "PID tuning" — stable below 80%, tuning isn't the issue | "Positioner fault" — positioner works fine below 80% | "Air supply insufficient" — would affect all positions | "Packing friction" — would affect all positions

**Reference:** Kuphaldt LIII Ch.25; ISA-75.01; Butterfly Valve Torque Characteristics

---

## IUK-T3-DIAG-427
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A plant's historian trends show that a temperature measurement and a flow measurement both step-change at the exact same timestamp — temperature drops 15°F and flow increases 8%. They stay at the new values. Both transmitters are on separate loops, separate power supplies, separate I/O cards, and measure different parts of the process. Is this a coincidence, or should it be investigated? What would you look for?

**Correct Answer:**  
**This should be investigated — simultaneous step changes on independent measurements suggest a real process event, not an instrumentation coincidence.** Unlike the DCS historian glitch scenario (where all measurements shift by the same percentage), these are two DIFFERENT magnitudes in DIFFERENT directions on DIFFERENT parameters — strongly suggesting a real process change.

**Required Elements:**
- Real process event (not instrumentation): mandatory | Different magnitudes and directions rule out data artifact: mandatory | Process investigation steps: mandatory | Common disturbance path: required for full credit

**Common Wrong Answers:**
- "Instrumentation coincidence" — extremely unlikely given the specifics | "DCS historian glitch" — different magnitudes/directions rule this out | "Ignore it" — step changes in safety-relevant parameters must be investigated

**Reference:** Process Safety Investigation Methodology; ISA-18.2 (Alarm Analysis)

---

## IUK-T3-DIAG-428
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A vortex flow meter on a saturated steam line at 150 PSIG shows intermittent zero readings lasting 1-3 seconds, then returns to normal flow indication. The steam system is stable and other flow indicators downstream confirm continuous flow. The vortex meter worked perfectly for 2 years. What is the most likely cause?

**Correct Answer:**  
**Most likely cause: Moisture (wet steam / condensate slugs) intermittently hitting the vortex shedder bar.** At 150 PSIG saturated steam, any heat loss in the piping causes condensation. Condensate slugs that reach the vortex meter: 1) Temporarily alter the vortex shedding pattern — the transition from gas to liquid and back disrupts the coherent vortex street; 2) The meter's signal processing algorithm rejects the disrupted signal as noise and reports zero flow; 3) Once the slug passes (1-3 seconds), normal vortex shedding resumes.

**Required Elements:**
- Condensate slugs disrupting vortex shedding: mandatory | Intermittent nature matches slug frequency: mandatory | Steam trap / insulation check: mandatory | Moisture separator: required for full credit

**Common Wrong Answers:**
- "Sensor failure" — returns to normal between events | "Electronics intermittent" — wouldn't correlate with steam conditions | "Below minimum velocity" — flow is confirmed continuous | "Pipe vibration" — would be continuous, not intermittent

**Reference:** Kuphaldt LIII Ch.16; Vortex Flow Meter Wet Steam Application Notes

---

## IUK-T3-DIAG-429
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A level transmitter (DP type) on an open atmospheric tank reads correctly at steady state, but whenever a batch discharge pump starts, the level reading jumps UP by 3% for about 10 seconds, then returns to the correct value. The pump suction is at the tank bottom. Why does the reading jump UP when liquid is being removed?

**Correct Answer:**  
**The reading jumps high because pump startup is creating a short-lived hydraulic pressure transient at the bottom measurement point — not because the actual level rises.**

The steady-state Bernoulli argument would predict a lower static pressure near the suction and therefore a lower indication. But the symptom is a **brief positive spike** that lasts only about **10 seconds**. That is the signature of a **startup transient / pressure wave / local hydraulic disturbance**, not a new steady-state head.

So the correct explanation is:
- pump starts,
- a transient pressure disturbance briefly increases pressure seen at the HP / bottom tap,
- DP rises momentarily,
- indicated level jumps up,
- then the transient decays and the reading returns to normal.

**Required Elements:**
- Pressure transient from pump start: mandatory | Temporary nature (10 seconds): mandatory | Dampening or snubber fix: mandatory | Tap relocation consideration: bonus

**Common Wrong Answers:**
- "Level actually rises" — pump is removing liquid, not adding | "Transmitter fault" — consistent and repeatable = process-related | "Electrical noise from pump motor" — would cause random noise, not consistent 3% jump

**Reference:** Kuphaldt LIII Ch.15; Process Measurement Best Practices

---

## IUK-T3-DIAG-430
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
An RTD temperature transmitter reads correctly from 0–300°F but reads progressively HIGH above 300°F, reaching +8°F error at 500°F. The RTD is a 3-wire Pt100. The cable run is 500 feet with 18 AWG copper extension wire. The transmitter was bench-calibrated with a decade box (resistance simulator) and passed perfectly. What is the most likely cause?

**Correct Answer:**  
**Most likely cause: The 3-wire RTD lead wire compensation is imperfect due to resistance mismatch between the lead wires, and this error increases with temperature because the RTD sensitivity (Ω/°F) decreases at higher temperatures while the fixed lead wire error remains constant — making it a larger percentage of the measurement.**

**Required Elements:**
- wire lead wire mismatch: mandatory | Error increases at higher temperature (percentage basis): mandatory | Bench cal bypasses cable: mandatory | 4-wire upgrade recommendation: required for full credit

**Common Wrong Answers:**
- "RTD element degradation" — bench cal passed perfectly | "Transmitter linearization error" — bench cal uses the same linearization | "Self-heating" — wouldn't increase with temperature in a properly designed circuit | "Wrong RTD curve" — would cause error across the entire range, not progressive

**Reference:** Kuphaldt LIII Ch.14; IEC 60751; 3-Wire RTD Compensation Theory

---

## IUK-T3-DIAG-431
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A level displacer transmitter on a propane (C₃) accumulator drum reads 15% higher than actual when ambient temperature drops from 90°F to 30°F overnight. The process temperature and pressure haven't changed. What is the most likely cause?

**Correct Answer:**  
**The torque tube stiffness changes with ambient temperature.** The torque tube (typically Ni-Span C or similar temperature-compensated alloy) connects the displacer to the transmitter. If the alloy's temperature compensation is imperfect, or if a non-compensated alloy was used, the torque tube becomes stiffer in cold ambient conditions. A stiffer tube produces less angular deflection for the same buoyant force → the transmitter reads as if there's more buoyant force (more liquid) → reads HIGH. This effect is proportional to the temperature change and independent of process conditions. **Fix:** Verify torque tube material matches specification; apply ambient temperature compensation if available; insulate the torque tube housing.

**Required Elements:**
- Torque tube stiffness change with temperature: mandatory | Direction correct (stiffer = reads high): mandatory | Ambient vs process temperature distinction: mandatory

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Reference:** Kuphaldt LIII Ch.15; Fisher/Emerson Displacer Transmitter Manual

---

## IUK-T3-DIAG-432
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A multipath ultrasonic flow meter (5-path) on a 20-inch crude oil pipeline shows good agreement with a prover at flow rates above 5 ft/s but reads 2% high below 3 ft/s. All 5 paths have good signal quality. What is the most likely cause?

**Correct Answer:**  
**At low velocities (below ~3 ft/s), the flow profile transitions from turbulent to transitional/laminar, and the meter's flow profile correction algorithm is optimized for turbulent flow.** In turbulent flow, the velocity profile is relatively flat — all 5 paths sample a representative velocity. In transitional flow, the profile becomes more parabolic, and the center paths see proportionally higher velocity relative to the wall paths. If the meter's algorithm assumes a turbulent profile, it over-estimates the average velocity at transitional Reynolds numbers. **Fix:** Enable the meter's Reynolds-number-dependent profile correction (most modern meters have this); verify the Reynolds number range for the crude oil viscosity at operating temperature; consider a different meter technology for consistently low-velocity applications.

**Required Elements:**
- Turbulent-to-transitional profile change: mandatory | Profile correction algorithm limitation: mandatory | Reynolds number dependency: mandatory

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Reference:** AGA Report No. 9; Kuphaldt LIII Ch.16

---

## IUK-T3-DIAG-433
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A pH control system on a waste neutralization tank oscillates wildly despite aggressive tuning attempts. The system adds caustic (NaOH) through a control valve to neutralize acidic waste. The titration curve shows that a 0.1% change in NaOH flow causes a 3 pH unit change near the setpoint of pH 7. What is the fundamental control problem?

**Correct Answer:**  
**The process gain is extremely non-linear and extremely high near pH 7.** The pH titration curve is essentially logarithmic — near pH 7 (the equivalence point for a strong acid/strong base neutralization), the slope is nearly vertical. A tiny change in reagent flow causes a massive pH change. This means: 1) The process gain at pH 7 is enormous — orders of magnitude higher than at pH 3 or pH 11; 2) No fixed PID tuning can handle this — gain that works at pH 5 is wildly too aggressive at pH 7; 3) The valve resolution at such small flow changes may be insufficient — the minimum controllable increment of the valve may produce a pH change of several units.

**Required Elements:**
- Non-linear titration curve / extreme gain at pH 7: mandatory | Fixed PID cannot handle variable gain: mandatory | Two-stage or gain scheduling solution: mandatory

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Reference:** Kuphaldt LIII Ch.29; ISA Practical Process Control (pH Control)

---

## IUK-T3-DIAG-434
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A vibrating wire pressure transducer (used for geotechnical monitoring) shows a slow drift of +2 PSI per month over 6 months. The process pressure hasn't changed (verified by a reference gauge). The transducer is installed in a wet underground environment at 55°F constant temperature. What is the most likely cause?

**Correct Answer:**  
**Moisture ingress into the transducer housing is changing the tension on the vibrating wire.** Vibrating wire transducers measure pressure by monitoring the resonant frequency of a tensioned wire. Moisture in the housing: 1) Corrodes the wire or its anchor points, changing the effective tension; 2) Adds mass to the wire, lowering its resonant frequency (which the electronics interpret as lower tension = higher pressure); 3) The slow, steady drift (2 PSI/month) is characteristic of gradual moisture accumulation rather than sudden failure. **Fix:** Replace the transducer with a sealed unit rated for the wet environment (IP68 or higher); verify the cable gland seal integrity; consider using a different pressure sensing technology less susceptible to moisture (piezoresistive with hermetic seal).

**Required Elements:**
- Moisture ingress: mandatory | Effect on vibrating wire (mass/corrosion): mandatory | Gradual drift matches slow ingress: mandatory | Sealed replacement: required for full credit

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Reference:** Vibrating Wire Transducer Theory; Geotechnical Monitoring Best Practices

---

## IUK-T3-DIAG-435
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A field-mounted temperature indicator (bimetallic thermometer) reads 50°F higher than a recently calibrated RTD transmitter at the same thermowell. The thermometer stem extends 6 inches into a 2-inch nozzle on a vessel operating at 400°F. The vessel wall is 1.5 inches thick carbon steel. What is the most likely cause?

**Correct Answer:**  
**Most likely cause: insufficient immersion combined with conducted heat from the hot nozzle / thermowell assembly.**

The bimetal thermometer stem is too short relative to the nozzle / wall geometry, so too much of the sensing length is influenced by the metal nozzle and thermowell rather than by the bulk process fluid.

Because the indicated value is **higher** than the RTD, the error is not the classic “too shallow and cooler ambient pulls it low” case. It is the opposite: the metal assembly around the thermometer is apparently hotter than the bulk fluid seen by the deeper, better-positioned RTD. The short, partially immersed bimetal element is averaging that conducted heat and reading high.

So the primary issue is still **immersion depth / stem conduction error**, but in the **high-reading direction** because of the local thermal environment.

**Required Elements:**
- Insufficient immersion depth: mandatory | Stem averaging / nozzle conduction: mandatory | Direction analysis (wall heat conduction): mandatory

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Reference:** Kuphaldt LIII Ch.14; ASME PTC 19.3

---

## IUK-T3-DIAG-436
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A Modbus TCP/IP poll of 50 remote I/O devices takes 8 seconds to complete one scan cycle. The control requirement is a 2-second update rate. The network bandwidth is adequate (100 Mbps Ethernet). What is the most likely bottleneck, and how can it be resolved?

**Correct Answer:**  
**The bottleneck is the serial nature of Modbus TCP polling — the master polls each device sequentially (request-response-request-response...), and the aggregate response latency of 50 devices dominates the scan time.** Each device takes approximately 8000/50 = 160 ms to respond. This includes: network round-trip time (~1 ms on Ethernet), plus the DEVICE response time (100-200 ms is common for Modbus slaves processing a request). Network bandwidth is NOT the bottleneck — it's the device-level response time accumulated over 50 sequential polls.

**Required Elements:**
- Sequential polling latency (not bandwidth): mandatory | Per-device response time analysis: mandatory | Multi-threaded or priority-based solution: mandatory

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Reference:** Kuphaldt LIII Ch.22; Modbus TCP/IP Specification

---

## IUK-T3-DIAG-437
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A guided wave radar (GWR) level transmitter on a vessel containing two liquids (water below, hydrocarbon above) suddenly reports a level that is 3 feet higher than actual. The interface between the two liquids has not changed. A recent process change increased the water temperature from 120°F to 200°F. What is the cause?

**Correct Answer:**  
**The increased water temperature reduced its dielectric constant, affecting the GWR signal propagation velocity through the water layer.** GWR measures distance by timing electromagnetic pulse reflections. The pulse velocity in a medium depends on its dielectric constant: v = c/√ε. Water's Dk drops significantly with temperature (80 at 68°F → ~55 at 200°F). With lower Dk, the pulse travels faster through the water, and the transmitter interprets the faster travel time as a shorter distance to the bottom reflection, making the APPARENT water layer thinner — causing the total level to appear HIGHER than actual. **Fix:** Re-configure the GWR's medium Dk for the new water temperature; use the GWR's interface measurement mode if available; add temperature compensation.

**Required Elements:**
- Water Dk change with temperature: mandatory | Propagation velocity effect: mandatory | Direction (reads higher): mandatory | Dk reconfiguration: required for full credit

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Reference:** Kuphaldt LIII Ch.15; Emerson GWR Application Guide

---

## IUK-T3-DIAG-438
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A control loop using a pneumatic I/P transducer (4-20 mA input, 3-15 PSI output) driving a diaphragm valve actuator exhibits a dead band of approximately 2% — the valve doesn't respond to signal changes smaller than 2%. A digital positioner on a similar valve on the adjacent loop has no observable dead band. What is the most likely cause and why doesn't the positioner have this issue?

**Correct Answer:**  
**The I/P transducer output has a characteristic dead band from its internal mechanism (nozzle-bapper, relay, spring friction).** Without closed-loop feedback, the I/P only changes its output when the input signal overcomes the internal friction and mechanical hysteresis. Changes smaller than the dead band produce no output change. **Why the positioner doesn't have this:** A digital positioner is a CLOSED-LOOP device — it reads the actual valve position (feedback) and continuously adjusts its pneumatic output until the valve reaches the commanded position. Even if the positioner's internal I/P has dead band, the feedback loop detects the valve hasn't moved and increases the drive signal until it does. The positioner essentially "pushes through" the dead band using its internal servo loop. **This is the fundamental advantage of a positioner over a standalone I/P.**

**Required Elements:**
- I/P dead band from mechanical friction: mandatory | No feedback in I/P (open loop): mandatory | Positioner has closed-loop feedback: mandatory | Positioner overcomes dead band via servo: required for full credit

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Reference:** Kuphaldt LIII Ch.25; ISA-75.25

---

## IUK-T3-DIAG-439
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A plant replaces all analog 4-20 mA flow transmitters with FOUNDATION Fieldbus transmitters. After conversion, operators report that flow readings are "noisier" than before, even though the FF transmitters have better specifications. The FF transmitters are configured with the same damping time constant as the old analog units. What is the most likely explanation?

**Correct Answer:**  
**The FOUNDATION Fieldbus transmitters report the DIGITAL process value with full resolution, while the old analog 4-20 mA signal was inherently filtered by the cable capacitance, DCS input card filtering, and A/D conversion.** The 4-20 mA current loop acts as a low-pass filter — high-frequency noise is attenuated by cable capacitance and inductance before reaching the DCS. The DCS input card also applies its own input filter. The digital FF value bypasses all of this — the raw digital PV goes from the transmitter directly to the DCS with no cable filtering. The FF transmitter's configured damping is the ONLY filter. If the analog system had 3+ stages of filtering (transmitter damping + cable + input card), and FF has only one (transmitter damping), the FF appears noisier even with better inherent accuracy. **Fix:** Increase the FF transmitter damping, or add a digital filter in the DCS function block to match the total filtering of the previous analog system.

**Required Elements:**
- Analog cable filtering removed in FF: mandatory | Multiple filter stages in analog vs single in FF: mandatory | Digital value = full resolution: mandatory | Additional damping as fix: required for full credit

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Reference:** Kuphaldt LIII Ch.22; ISA-50.02

---

## IUK-T3-DIAG-440
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A Coriolis meter on a liquid application shows accurate mass flow but the density reading is 0.5% lower than lab analysis. The meter was factory-calibrated on water and field-verified with a known density fluid. The process fluid is a hydrocarbon blend at 120°F. The meter tubes are 316SS. What is the most likely cause?

**Correct Answer:**  
**The meter's density calibration was verified with a different fluid at a different temperature, and the meter's density measurement has a small temperature-dependent error.** Coriolis density measurement derives from tube resonant frequency, which depends on the mass of the tube + fluid. Temperature affects both: the tube stiffness (which changes the relationship between frequency and density) and the fluid density itself. If the factory water calibration and field verification were both done near ambient temperature, but the process operates at 120°F, the tube's Young's modulus is slightly lower at 120°F, changing the frequency-density relationship. A 0.5% density error at 120°F is within the range of thermal coefficient mismatch. **Fix:** Perform a two-point density calibration at the operating temperature, or use the meter's temperature-compensated density mode with verified coefficients.

**Required Elements:**
- Temperature effect on tube stiffness/density calibration: mandatory | Factory cal at different conditions: mandatory | Temperature compensation as fix: mandatory

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Reference:** Kuphaldt LIII Ch.16; Emerson Micro Motion Density Calibration Guide

---

## IUK-T3-DIAG-442
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A turbine flow meter on a gasoline pipeline suddenly reads 40% higher than normal. Upstream and downstream pressures are normal. The product grade hasn't changed. A technician notices the meter's pre-amplifier has been recently replaced. What is the most likely cause?

**Correct Answer:**  
**The new pre-amplifier has a different gain or threshold setting, causing it to count blade-pass pulses AND harmonics (double or triple counting).** Turbine meter pre-amps must be tuned to the expected signal amplitude and frequency. If the gain is too high or the trigger threshold too low, the pre-amp may trigger on noise, reflections, or harmonic content of the blade-pass signal — effectively doubling the pulse count → 2× indicated flow. A 40% increase (not exactly 2×) suggests intermittent double-counting on some blades. **Fix:** Re-tune the pre-amplifier trigger level and gain; use an oscilloscope to verify clean pulse signals.

**Required Elements:**
- Pre-amplifier gain/threshold causing multiple counting: mandatory | Recent replacement correlation: mandatory | Oscilloscope verification: required for full credit

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Reference:** Kuphaldt LIII Ch.16; AGA Report No. 7

---

## IUK-T3-DIAG-443
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A control valve with a pneumatic piston actuator and a volume booster fails to respond quickly to step changes — it takes 8 seconds to stroke from 50% to 100%, compared to 2 seconds when the volume booster was new. The instrument air supply is at 100 PSIG. What is the most likely cause?

**Correct Answer:**  
**The volume booster's internal orifice or seat is partially blocked (contaminated), reducing its flow capacity.** Volume boosters amplify the positioner's pneumatic signal by supplying high-volume air directly from the supply to the actuator. If the booster's internal passages are contaminated (rust, pipe scale, moisture), its flow capacity drops — it can still reach the final pressure but takes longer. The 4× slower stroke (8 vs 2 seconds) indicates approximately 75% flow capacity reduction. **Fix:** Clean or replace the volume booster; install a filter/regulator upstream of the booster; verify instrument air quality (moisture, particulate per ISA-7.0.01).

**Required Elements:**
- Volume booster contamination reducing flow: mandatory | Slow stroke vs supply pressure: mandatory | Air quality as root cause: required for full credit

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Reference:** Kuphaldt LIII Ch.25; ISA-7.0.01 (Instrument Air Quality)

---

## IUK-T3-DIAG-444
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A differential pressure transmitter reading is observed to "ratchet" upward — each time the process flow cycles (start/stop), the reading increases by a small amount and never returns to its original zero. After 50 cycles, the zero has shifted by 15 inH₂O. What is the most likely cause?

**Correct Answer:**  
**The sensing diaphragm is yielding (permanently deforming) under cyclic pressure loading — a fatigue failure of the diaphragm.** Each pressure cycle stretches the diaphragm slightly beyond its elastic limit, creating a small permanent set. The permanent deformation shifts the zero upward. Over 50 cycles, these small plastic deformations accumulate to 15 inH₂O. This occurs when: the operating DP is near the transmitter's maximum rated DP, the pressure cycling is severe (large ΔP per cycle), or the diaphragm material has degraded (corrosion thinning). **Fix:** Replace the transmitter (diaphragm damage is not field-repairable); select a transmitter with higher overpressure rating; check if process pressure spikes are exceeding the transmitter's rated DP.

**Required Elements:**
- Diaphragm fatigue/plastic deformation: mandatory | Ratcheting mechanism (cumulative permanent set): mandatory | Near-maximum DP operation: mandatory | Transmitter replacement: required for full credit

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Reference:** Kuphaldt LIII Ch.12; Material Fatigue Theory

---

## IUK-T3-DIAG-445
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A plant has 20 identical temperature control loops on a reactor battery. 19 loops control within ±0.5°F of setpoint. Loop #7 controls within ±3°F despite identical tuning parameters, identical valves, identical transmitters, and identical process conditions. The valve, transmitter, and controller have all been individually tested and found to be within specification. What should you investigate?

**Correct Answer:**  
**The process dynamics of Loop #7 differ from the other 19, even though the equipment is "identical."** Possible process differences: 1) Dead time — Loop #7 may have a longer distance between the control element and the measurement point; 2) The heat transfer characteristics may differ (fouled heat exchanger, different jacket flow pattern); 3) Process disturbances may be larger on Loop #7 (proximity to a variable feed stream, cooling water variations); 4) The valve may be oversized for THIS particular reactor's flow requirement (same Cv but different required flow). **The key insight:** Identical equipment does NOT guarantee identical process dynamics. Control performance depends on the PROCESS, not just the hardware. **Investigation:** Perform a bump test on Loop #7 — put controller in manual, make a 5% output step change, record the response. Compare the time constant, dead time, and gain to the other 19 loops. The difference in dynamics will identify the root cause.

**Required Elements:**
- Process dynamics differ despite identical equipment: mandatory | Bump test comparison recommended: mandatory | Specific dynamic differences (dead time, gain): mandatory

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Reference:** Kuphaldt LIII Ch.28-29; ISA Practical PID Tuning

---

## IUK-T3-DIAG-446
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A Coriolis flow meter totalizer on a custody transfer metering station shows 500 barrels delivered, but the receiving tank's strapping table (calibrated volume vs. level) shows only 490 barrels received. The Coriolis meter was recently proved with a prover at 0.9998 meter factor. Both measurements are at the same temperature. What accounts for the 2% difference?

**Correct Answer:**  
**The most likely cause is entrained gas (air/vapor) in the pipeline.** The Coriolis meter measures the mass of everything passing through it — including gas bubbles. If the liquid entrains 2% gas by volume, the meter registers the gas as if it were liquid (the mass contribution of gas is negligible, but the VOLUME it displaces is not). The receiving tank level measurement only sees the liquid that actually arrives — the gas separates at the tank and vents. The prover test may have been performed under conditions with less or no gas entrainment. **Other possibilities:** Pipeline line pack (pressure changes in the pipeline between the meter and the tank); temperature differences despite the claim of "same temperature"; tank strapping table inaccuracy. **Fix:** Check for gas entrainment (install a sight glass before the meter); use the Coriolis meter's gas-void-fraction diagnostic; verify the prover test conditions match normal operating conditions.

**Required Elements:**
- Entrained gas as primary cause: mandatory | Gas measured by Coriolis but separates at tank: mandatory | Prover conditions may differ: mandatory | Gas diagnostic: required for full credit

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Reference:** API MPMS Chapter 5.6; Kuphaldt LIII Ch.16

---

## IUK-T3-DIAG-448
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
[MISSING]

**Correct Answer:**  
[MISSING]

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

---

## IUK-T3-DIAG-449
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
[MISSING]

**Correct Answer:**  
[MISSING]

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

---

## IUK-T3-DIAG-450
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
[MISSING]

**Correct Answer:**  
[MISSING]

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

---

## IUK-T3-DIAG-451
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
[MISSING]

**Correct Answer:**  
[MISSING]

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

---

## IUK-T3-DIAG-452
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
[MISSING]

**Correct Answer:**  
[MISSING]

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

---

## IUK-T3-DIAG-453
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
[MISSING]

**Correct Answer:**  
[MISSING]

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

---

## IUK-T3-DIAG-454
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
[MISSING]

**Correct Answer:**  
[MISSING]

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

---

## IUK-T3-DIAG-455
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
[MISSING]

**Correct Answer:**  
[MISSING]

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

---

## IUK-T3-DIAG-456
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
An ultrasonic flow meter on a hot condensate line (>212°F) loses signal intermittently. What is the most likely cause and corrective action?

**Correct Answer:**  
**Most likely cause: flash steam forming in the measurement path and disrupting acoustic coupling.** Hot condensate near saturation can partially flash as local pressure changes occur, creating vapor pockets that severely attenuate or scatter the ultrasonic signal. **Corrective action:** move the measurement to a subcooled section, increase back-pressure, or otherwise eliminate flashing conditions at the meter.

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

---

## IUK-T3-DIAG-457
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A DP transmitter on a tank with diaphragm seals reads correctly when cold but drifts +5 inH₂O when the process reaches 300°F. Diagnose the most likely cause.

**Correct Answer:**  
**Most likely cause: diaphragm-seal fill-fluid thermal expansion creating an asymmetric temperature error.** If the HP seal is driven hot while the LP side stays cooler, the fill-fluid expansion and capillary effects shift the apparent differential pressure. **Fix:** match seal/capillary configurations and temperatures as closely as possible, or use a design / compensation method intended for high-temperature seal service.

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

---

## IUK-T3-DIAG-458
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A valve positioner hunts continuously (about ±1%) even at a constant setpoint. What is the most likely cause?

**Correct Answer:**  
**Most likely cause: positioner gain too high for the valve friction / actuator dynamics.** The positioner over-corrects, overshoots, and reverses repeatedly. **Fix:** reduce positioner gain, increase damping / deadband as appropriate, and verify the valve is not adding excessive stiction.

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

---

## IUK-T3-DIAG-459
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A pressure switch rapidly opens and closes near its setpoint. What is causing the bounce?

**Correct Answer:**  
**Most likely cause: insufficient deadband (switch differential) combined with process noise near setpoint.** The switch repeatedly re-makes and breaks because the reset point is too close to the trip point. **Fix:** increase the differential, add a snubber if the process is noisy, or replace the switch with a transmitter/setpoint solution where tighter control logic is needed.

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

---

## IUK-T3-DIAG-460
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A thermocouple reads correctly on the positive side of zero but reads about -15°F when the actual temperature is known to be +10°F. Diagnose the likely fault.

**Correct Answer:**  
**Most likely cause: reversed thermocouple / extension-wire polarity at an intermediate junction.** A polarity reversal can make the cold-junction compensation act in the wrong direction and create a large low-temperature error, especially near ambient. **Fix:** verify polarity end-to-end and correct the reversed junction.

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

---

## IUK-T3-DIAG-461
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
An analyzer sample system has a 30-second transport delay, and the associated control loop oscillates with about a 60-second period. What is the likely control issue?

**Correct Answer:**  
**This is a classic dead-time-driven oscillation.** The transport lag is large relative to the controller aggressiveness, so PI action keeps integrating before the process feedback arrives. **Fix:** slow the loop substantially — especially integral action — and tune with the transport delay explicitly recognized.

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

---

## IUK-T3-DIAG-462
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A pressure transmitter reads correctly at 0% and 100% but reads 2% high at 50%. What is the most likely error type?

**Correct Answer:**  
**Most likely cause: non-linearity (mid-span bowing) rather than zero or span error.** The endpoints are correct, but the curve deviates in the middle. **Fix:** verify with a multi-point calibration and, if supported, apply the manufacturer’s linearization / correction method or replace the device if it is out of spec.

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

---

## IUK-T3-DIAG-463
**Tier:** T3 · Specialist/PhD  
**Type:** DIAG  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A flow totalizer in the DCS shows 10% more volume over 24 hours than the transmitter’s internal totalizer. What is the most plausible explanation?

**Correct Answer:**  
**Most likely cause: differences in sampling / numerical integration between the DCS totalizer and the transmitter’s internal totalizer.** If the flow is pulsating or noisy, a slower DCS scan/integration scheme can bias the total relative to the transmitter’s higher-rate internal integration. **Fix:** compare scan/update methods, increase host-side sampling if appropriate, or use the transmitter’s certified totalizer where required.

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

---

## IUK-T3-MAST200-003
**Block:** Mastery Exam (Kuphaldt)  
**Tier:** T3 · Specialist/PhD  
**Type:** SKETCH  
**Weight:** 3.5×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_mastery_textualized_IUK_MASTERY_INST200_x1_mastery_v01_textualized  
**Format:** iuk_mastery_textualized  
**Review status:** ai_drafted_needs_sme_distractors  
**Textualized from diagram:** YES  

**Question:**  
[Diagram: A boost DC-DC converter circuit shows a voltage supply (V_supply) connected in series with an inductor. The other side of the inductor is connected to a node. From this node, an NPN BJT transistor's collector is connected, with its emitter going to ground and its base receiving a pulse voltage (V_pulse). Also from this node, the anode of a diode is connected. The cathode of the diode is connected to a second node. From this second node, a capacitor is connected in parallel to ground, and a resistive load is also connected in parallel to ground.] During the transistor's 'on' period, describe the following for the components in the schematic: 1. Voltage polarity across the inductor (indicate which side is positive and which is negative). 2. Voltage polarity across the diode (indicate which side is positive and which is negative). 3. Direction of conventional current flow through the capacitor (describe the path).

**Correct Answer:**  
1. **Voltage polarity across the inductor:** During the transistor's 'on' period, the transistor acts as a closed switch, creating a path for current from V_supply, through the inductor, and through the transistor to ground. As the current through the inductor rapidly increases, the inductor generates a back-EMF to oppose this change. This self-induced voltage makes the end of the inductor connected to V_supply positive (+) relative to the end connected to the transistor's collector, which becomes negative (-).
2. **Voltage polarity across the diode:** When the transistor is 'on', its collector is pulled close to ground potential (Vce_sat). The anode of the diode is connected to this point. The cathode of the diode is connected to the output capacitor and load, which maintains a boosted output voltage (V_out) that is typically higher than V_supply. Since the anode is at a lower potential (near ground) than the cathode (at V_out), the diode is reverse-biased and effectively off. Therefore, the cathode side (output side) is positive (+) relative to the anode side (transistor side) which is negative (-).
3. **Direction of conventional current flow through the capacitor:** During the transistor's 'on' period, the diode is reverse-biased and off, disconnecting the output section (capacitor and load) from the input supply and inductor. To maintain the output voltage and supply current to the load, the capacitor discharges through the load. Therefore, conventional current flows out of the capacitor's positive plate (connected to the load) through the resistive load, and returns to the capacitor's negative plate (ground). So, the current within the capacitor flows from its top plate (connected to the load) downwards to its bottom plate (ground).

**Required Elements:**
- Inductor behavior during current increase (Lenz's Law)
- Diode biasing in a boost converter
- Capacitor discharge behavior
- Boost converter operation principles

**Common Wrong Answers:**
- [DRAFT — SME review required]
- [DRAFT — SME review required]

**Scoring Rubric:**
| Score | Criteria |
|-------|----------|
| Full | 10/10 — all 4 required elements present and accurate |
| Partial (high) | 7/10 — most elements correct |
| Partial (low) | 4/10 — partial answer, key element missing |
| Zero | 0/10 — incorrect or missing core concept |

**Reference:** Kuphaldt INST mastery

**Difficulty Rationale:** This question requires a detailed understanding of how a boost converter operates, specifically the transient behavior of an inductor, diode biasing, and capacitor discharge during the switch's ON period. It demands application of fundamental electrical principles within a specific circuit context, rather than simple recall.

---

## IUK-T3-MAST200-008
**Block:** Mastery Exam (Kuphaldt)  
**Tier:** T3 · Specialist/PhD  
**Type:** CALC  
**Weight:** 3.5×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_mastery_textualized_IUK_MASTERY_INST200_x1_mastery_v01_textualized  
**Format:** iuk_mastery_textualized  
**Review status:** ai_drafted_needs_sme_distractors  
**Textualized from diagram:** YES  

**Question:**  
[Diagram: An operational amplifier (op-amp) circuit. The op-amp is powered by a +12 V positive rail and a -12 V negative rail. The non-inverting input (+) is connected directly to ground. The inverting input (-) is connected to a node, which is simultaneously connected to the positive terminal of a 3.9 V DC voltage source (whose negative terminal is grounded) and the positive terminal of a 2.7 V DC voltage source (whose negative terminal is also grounded). The output is labeled V_out.] Calculate the output voltage (V_out) from this op-amp circuit, given the voltage source values shown in the diagram. Assume the op-amp is capable of "rail-to-rail" output voltage swings. Be sure to denote whether the output voltage is a positive or a negative value (with reference to ground).

**Correct Answer:**  
1. **Determine the voltage at the non-inverting input (V+):**
   The non-inverting input is connected to ground, so V+ = 0 V.

2. **Determine the voltage at the inverting input (V-):**
   The inverting input is connected to the positive terminals of two different DC voltage sources (3.9 V and 2.7 V), both referenced to ground. Directly connecting two different voltage sources to a single node, especially without current-limiting resistors, represents an ill-defined or potentially problematic circuit in a real-world scenario (as it violates KVL at the node or implies a short between sources). However, for the purpose of a theoretical problem that asks for a calculation, we must deduce the intended input. Both sources provide a positive voltage relative to ground. Regardless of whether the inverting input effectively sees 3.9 V, 2.7 V, or some combination (e.g., if one source dominates, or if there's a hypothetical sum like 3.9 V + 2.7 V = 6.6 V), the voltage V- will be a positive value.

3. **Determine the output voltage (V_out) for an open-loop op-amp:**
   This op-amp is configured in an open-loop comparator mode because there is no feedback from output to input. In this configuration, the output saturates to one of the supply rails based on the differential input voltage (V+ - V-).
   - If (V+ - V-) > 0, then V_out saturates to the positive rail (+12 V).
   - If (V+ - V-) < 0, then V_out saturates to the negative rail (-12 V).

   In this circuit:
   V+ = 0 V
   V- = (some positive value, whether 2.7 V, 3.9 V, or a combination thereof, it remains positive).

   Therefore, (V+ - V-) = 0 V - (positive value) = a negative value.

   Since (V+ - V-) is negative, the op-amp's output will saturate to the negative supply rail.

**Answer:**
V_out = -12 V

**Required Elements:**
- [DRAFT — SME to specify]

**Common Wrong Answers:**
- [DRAFT — SME review required]
- [DRAFT — SME review required]

**Scoring Rubric:**
| Score | Criteria |
|-------|----------|
| Full | 10/10 — all 1 required elements present and accurate |
| Partial (high) | 7/10 — most elements correct |
| Partial (low) | 4/10 — partial answer, key element missing |
| Zero | 0/10 — incorrect or missing core concept |

**Reference:** Kuphaldt INST mastery

**Difficulty Rationale:** Requires understanding of op-amp comparator operation, saturation, and power rail limits. The diagram presents an ambiguous connection for the inverting input, which could be interpreted as an invalid circuit. However, recognizing that all plausible positive input interpretations lead to the same output saturation state makes it solvable. This requires deeper understanding of op-amp behavior beyond just ideal calculations for common configurations.

---

## IUK-T3-MAST200-012
**Block:** Mastery Exam (Kuphaldt)  
**Tier:** T3 · Specialist/PhD  
**Type:** EXPLAIN  
**Weight:** 3.5×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_mastery_textualized_IUK_MASTERY_INST200_x1_mastery_v01_textualized  
**Format:** iuk_mastery_textualized  
**Review status:** ai_drafted_needs_sme_distractors  
**Textualized from diagram:** YES  

**Question:**  
[Diagram: A Buck (step-down) DC-DC converter circuit is shown. It consists of a voltage supply (V_supply) connected in series with an inductor. The inductor is connected to the collector of an NPN Bipolar Junction Transistor (BJT). The emitter of the BJT is connected to ground. The base of the BJT is controlled by a pulse voltage (V_pulse). A freewheeling diode is connected with its anode at the junction of the inductor and the BJT collector, and its cathode connected to the positive rail of the output. An output capacitor is connected in parallel with a load resistor, both across the output rails.] Describe the operation of this Buck converter circuit during its 'on period'.

**Correct Answer:**  
During the 'on period', the pulse voltage (V_pulse) turns 'on' (saturates) the NPN BJT transistor, causing it to act as a closed switch. This connects the voltage supply (V_supply) directly across the inductor. Current flows from V_supply, through the inductor, and through the conducting BJT to ground. The inductor's magnetic field stores energy, and the current through it increases approximately linearly (assuming V_supply is constant). During this period, the voltage at the anode of the freewheeling diode (junction of inductor and BJT collector) is approximately V_supply, while the output capacitor maintains the output voltage. Since V_supply is typically higher than the output voltage, the diode is reverse-biased and does not conduct. The output capacitor supplies the necessary current to the load, maintaining the output voltage.

**Required Elements:**
- BJT 'on' state
- inductor charging
- current path description
- diode state
- capacitor function for load

**Common Wrong Answers:**
- [DRAFT — SME review required]
- [DRAFT — SME review required]

**Scoring Rubric:**
| Score | Criteria |
|-------|----------|
| Full | 10/10 — all 5 required elements present and accurate |
| Partial (high) | 7/10 — most elements correct |
| Partial (low) | 4/10 — partial answer, key element missing |
| Zero | 0/10 — incorrect or missing core concept |

**Reference:** Kuphaldt INST mastery

**Difficulty Rationale:** Requires detailed knowledge of Buck converter operation, including component states, current paths, and energy transfer during the 'on' cycle.

---

## IUK-T3-MAST251-004
**Block:** Mastery Exam (Kuphaldt)  
**Tier:** T3 · Specialist/PhD  
**Type:** DIAGNOSE  
**Weight:** 3.5×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_mastery_textualized_IUK_MASTERY_INST251_x2_mastery_textualized  
**Format:** iuk_mastery_textualized  
**Review status:** ai_drafted_needs_sme_distractors  
**Textualized from diagram:** YES  

**Question:**  
[Diagram: A control system graph shows three lines over time: Process Variable (PV), Setpoint (SP), and Controller Output (Output), all measured in percentage (0% to 100%). Initially, PV and SP are stable at 50%, and Output is stable at 30%. At the first event, the Setpoint (SP) steps up from 50% to 60%. Concurrently, the Controller Output (Output) steps up from 30% to 40%. The Process Variable (PV) then rises, overshoots the 60% Setpoint slightly (reaching approximately 62-63%), and eventually settles at 60%. During this settling period, the Controller Output gradually decreases from 40% to approximately 30%. At a later second event, the Setpoint (SP) steps down from 60% to 40%. Concurrently, the Controller Output (Output) steps down from 30% to 20%. The Process Variable (PV) then falls, undershoots the 40% Setpoint slightly (reaching approximately 37-38%), and eventually settles at 40%. During this settling period, the Controller Output gradually increases from 20% to approximately 30%.] Based on the graphed response, determine whether the loop controller shows proportional action, integral action, or derivative action. Also, identify whether the controller's action is direct or reverse.

**Correct Answer:**  
The controller demonstrates both **proportional action** and **integral action**. 
*   **Proportional action** is evident from the immediate step change in the controller's output (Output) whenever there is a step change in the Setpoint (SP). For example, when SP steps up, Output steps up; when SP steps down, Output steps down.
*   **Integral action** is evident from the gradual adjustment of the output over time to eliminate the steady-state error and bring the Process Variable (PV) precisely to the Setpoint (SP). The output continues to change as long as an error exists, ensuring PV settles exactly at SP, not just near it. 
*   There is no clear evidence of **derivative action**, which would typically manifest as sharp, short-duration spikes in the output in response to the rate of change of the PV or SP.

The controller's action is **direct**. This is indicated because when the Setpoint (SP) increases, the Controller Output (Output) increases to drive the Process Variable (PV) towards the new setpoint. Conversely, when SP decreases, Output decreases. Also, when the PV increases above the SP, the controller decreases the Output to bring the PV back down, which is characteristic of direct action.

**Required Elements:**
- identification of proportional action
- explanation for proportional action
- identification of integral action
- explanation for integral action
- identification of absence of derivative action (or lack of clear evidence)
- identification of direct action
- explanation for direct action

**Common Wrong Answers:**
- [DRAFT — SME review required]
- [DRAFT — SME review required]

**Scoring Rubric:**
| Score | Criteria |
|-------|----------|
| Full | 10/10 — all 7 required elements present and accurate |
| Partial (high) | 7/10 — most elements correct |
| Partial (low) | 4/10 — partial answer, key element missing |
| Zero | 0/10 — incorrect or missing core concept |

**Reference:** Kuphaldt INST mastery

**Difficulty Rationale:** Requires detailed analysis and interpretation of a process trend graph, correlating changes in Setpoint, Process Variable, and Controller Output to accurately identify specific PID control actions and the overall controller direction (direct/reverse). This involves understanding fundamental control theory beyond simple recall.

---

## IUK-T3-PROC-169
**Tier:** T3 · Specialist/PhD  
**Type:** PROC  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A SIS engineer must conduct a partial stroke test (PST) on an ESD valve to reduce the proof test interval credit. Describe: (1) what a PST actually tests, (2) what dangerous failure modes it CANNOT detect, and (3) how the coverage factor is used in the PFD calculation.

**Correct Answer:**  
**(1) What a partial stroke test tests:**
A partial stroke test moves the ESD valve 10–20% of its travel (or another defined fraction) while the process remains online. It tests:
- The solenoid valve de-energizes on command and allows actuator to begin moving
- The actuator responds to the solenoid signal
- The valve stem is not seized or stuck at the current (open) position
- The valve begins to move in the correct (closing) direction
- Valve position feedback shows movement proportional to command

**Required Elements:**
- PST scope (stuck open detection) + at least three failure modes not detected + coverage factor formula and worked example.

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Reference:** IEC 61511-1 Annex F; IEC 62382; partial stroke testing actuator vendor documentation; RNNP methodology

---

## IUK-T3-PROC-329
**Tier:** T3 · Specialist/PhD  
**Type:** PROC  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
You need to calibrate a DP transmitter configured for 0–200 inH₂O range while it remains installed on a steam drum. The impulse lines have condensate-filled legs. You cannot isolate the transmitter from the process. Describe the procedure to perform an as-found/as-left calibration check without removing the transmitter.

**Correct Answer:**  
**Procedure for in-situ DP transmitter calibration on a live steam drum with wet legs:**

**Required Elements:**
- Equalizing valve procedure (close blocks, open equalize): mandatory
- 5-point as-found check before any adjustments: mandatory
- Return-to-service sequence (HP first): mandatory
- Condensate leg thermal equilibrium note: required for full credit

**Common Wrong Answers:**
- Adjusting zero before completing as-found check — loses the as-found data
- Opening LP before HP during return to service — can damage transmitter
- Forgetting to close block valves before opening equalize — could apply process DP to test equipment
- Ignoring condensate leg equilibrium — readings will drift for minutes

**Scoring Rubric:**
- Full (100%): Complete procedure with correct sequence + as-found/as-left + return-to-service + condensate note
- High (75%): Correct procedure with minor omissions
- Low (50%): General concept but wrong sequence or missing safety steps
- Zero: Dangerous procedure or completely wrong approach

**Reference:** Kuphaldt LIII Ch.12; ISA RP 31.1; Plant Calibration Best Practices

---

## IUK-T3-XDOM-017
**Tier:** T3 · Specialist/PhD  
**Type:** XDOM  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A grounding fault has been detected on a thermocouple circuit. The thermocouple is a Type K measuring a flue gas temperature in a fired heater. It is installed in a thermowell in a Class I Div 1 area. The thermocouple extension wire runs 200 feet through a conduit shared with other I/O to the control room. The DCS temperature reading is erratic and approximately 40°F high. Describe the fault, its cause, and the correct remediation. Also identify what installation errors may have led to this condition.

**Correct Answer:**  
**The fault:** A ground fault (partial or complete) has occurred in the thermocouple circuit. A thermocouple should be an isolated circuit with no connection to earth ground. When one conductor contacts ground anywhere in the circuit, the measurement becomes subject to ground loop currents.

**Required Elements:**
- Ground loop as fault mechanism: mandatory
- Insulation failure as cause: mandatory
- Megohm testing as diagnostic tool: mandatory
- Shared conduit as installation error: required
- Class I Div 1 conduit seal check: required for full credit

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Reference:** Kuphaldt LIII Ch.8 Temperature Measurement — Thermocouples; NEC Article 501; ISA RP12.6

---

## IUK-T3-XDOM-027
**Tier:** T3 · Specialist/PhD  
**Type:** XDOM  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A 4–20 mA flow transmitter in a Class I Division 1 area using an IS (intrinsically safe) barrier develops an intermittent signal that appears as spikes to 20 mA lasting 100–200 ms, occurring randomly 3–8 times per hour. The same behavior was observed on two different transmitters (the first was replaced thinking it was faulty). The HART signal is clean and reads normally when accessed. There are no ground fault alarms. What is causing this and how do you find it?

**Correct Answer:**  
**Key facts:**
- Two different transmitters show same behavior → rules out the transmitter itself
- HART reads clean → the sensor and primary measurement are fine
- Intermittent, random 20 mA spikes → something is momentarily forcing the loop current to maximum
- IS barrier circuit → additional impedance and restrictions in the circuit
- No ground fault alarms

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Scoring Rubric:**
Full credit = ruling out transmitter (two units) + EMI/transient as cause + IS barrier ground integrity + investigative method with scope.

**Reference:** IEC 60079-14; ISA RP12.6; IS barrier installation requirements

---

## IUK-T3-XDOM-040
**Tier:** T3 · Specialist/PhD  
**Type:** XDOM  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A safety instrumented function (SIF) with a 2-year proof test interval has been in service for 18 months without a proof test. The process engineer asks the instrument engineer: "Can we extend the proof test to 3 years? We'll add a second transmitter (1oo2 voting) to maintain the SIL." The instrument engineer must evaluate whether this is acceptable. Walk through the complete analysis required.

**Correct Answer:**  
**This is a significant functional safety decision that requires a formal analysis — it cannot be answered with a simple yes or no in the field.**

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Scoring Rubric:**
Full credit = PFD recalculation framework + 1oo2 improvement math + common cause factor + MOC requirement + cannot approve without formal documentation. MOC requirement specifically = mandatory.

**Reference:** IEC 61511-1 Clauses 11.9, 16; ISA-84; IEC 61508-6 Annex B

---

## IUK-T3-XDOM-081
**Tier:** T3 · Specialist/PhD  
**Type:** XDOM  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A SIS proof test report for a high-level shutdown on a pressure vessel shows: the LSHH switch activated at 88% level (setpoint: 90%). The logic solver received the signal and latched the trip output. The ESD valve received the trip signal and the positioner confirmed 0% open (fully closed). But the process level continued to rise to 96% before stabilizing. Identify what failed in the SIF and what should be investigated.

**Correct Answer:**  
**Each subsystem confirmed activation — but the level still rose 8 percentage points above setpoint before stabilizing. Something in the final element chain did not perform as required.**

**Required Elements:**
- [not specified in source]

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Scoring Rubric:**
Full credit = valve seat leak as primary + positioner vs. actual shutoff distinction + valve closure time analysis + investigation required before SIF is considered proven.

**Reference:** IEC 61511 proof test; ISA-84; control valve seat leakage (ANSI/FCI 70-2)

---

## IUK-T3-XDOM-164
**Tier:** T3 · Specialist/PhD  
**Type:** XDOM  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A plant SIS proof test schedule requires testing a SIL 2 high-pressure trip (PAH-SIS-201) every 12 months. During the proof test, the technician confirms the transmitter trips at setpoint, the SIS logic executes correctly, and the ESD valve closes completely. However, the written proof test procedure does not include verification of the solenoid valve that operates the ESD valve actuator. After six years of operation with no failures, an audit finds this gap. Why is the missing solenoid verification significant and what is its impact on the SIF's actual PFD?

**Correct Answer:**  
**The solenoid verification gap is a potentially critical compliance and safety failure — not an administrative oversight.**

**Required Elements:**
- Series subsystem analysis + solenoid as separate failure mode + PFD accumulation during TI + 6-year impact calculation + remediation.

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Reference:** IEC 61511-1 Clause 16 (proof testing); IEC 61508-6 Annex B; solenoid valve PFD contribution

---

## IUK-T3-XDOM-175
**Tier:** T3 · Specialist/PhD  
**Type:** XDOM  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
An instrument engineer is designing a seal system for a DP transmitter measuring differential pressure across a heat exchanger with process fluid at 450°F and 600 PSIG. The engineer selects silicone fill fluid for the remote seal capillaries (Dmax = 175°F, silicone temperature range to 400°F). The system will have 15-foot capillaries. What is wrong with this design and what fill fluid should be considered?

**Correct Answer:**  
**Two problems: wrong fill fluid temperature rating and thermal-induced measurement error from long capillaries.**

**Required Elements:**
- Fill fluid temp rating exceeded + appropriate alternative + capillary thermal head error + mitigation strategy.

**Common Wrong Answers:**
- [DRAFT — SME review required]

**Reference:** Rosemount/Emerson remote seal handbook; fill fluid selection guide; Kuphaldt LIII Ch.7; capillary thermal error analysis

---

## IUK-T3-XDOM-321
**Tier:** T3 · Specialist/PhD  
**Type:** XDOM  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A refinery has a fired heater with a combustion air fan controlled by a VFD (Variable Frequency Drive). Since installing the VFD, nearby RTD temperature transmitters on the process side show intermittent noise spikes of ±5°F. The spikes correlate with VFD speed changes. The RTDs are 3-wire Pt100 in conduit. What is the root cause and what are the solutions?

**Correct Answer:**  
**Root cause: Electromagnetic interference (EMI) from the VFD's pulse-width modulation (PWM) switching is coupling into the RTD signal circuits.**

**Required Elements:**
- VFD PWM switching as EMI source: mandatory
- Coupling mechanism (radiated, conducted, or ground): mandatory
- RTD signal vulnerability (low-level mV signal): mandatory
- Cable separation + shielding solutions: required for full credit

**Common Wrong Answers:**
- "RTD element damaged by VFD" — VFD doesn't physically affect the RTD element
- "Ground loop" — while grounding is involved, the specific mechanism is EMI from PWM switching
- "Power supply noise" — spikes correlate with VFD speed changes, not power supply
- "Process temperature actually changing" — changes are too fast (spikes) and correlate with VFD

**Scoring Rubric:**
- Full (100%): VFD PWM source + coupling mechanism + RTD vulnerability + multiple solutions
- High (75%): VFD EMI + solutions
- Low (50%): Identifies EMI but vague on mechanism
- Zero: Wrong root cause

**Reference:** Kuphaldt LIII Ch.14 + Ch.20 (Electrical Noise); IEEE 519; NEMA ICS 12

---

## IUK-T3-XDOM-350
**Tier:** T3 · Specialist/PhD  
**Type:** XDOM  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A chemical plant upgrades from a legacy DCS to a new DCS. During commissioning, a temperature control loop that uses cascade (primary: reactor temperature, secondary: cooling water flow) oscillates severely. The loop used the same PID tuning parameters as the old system. The secondary controller is a PI algorithm. The valve and instrumentation are unchanged. What cross-domain issue is likely causing the oscillation?

**Correct Answer:**  
**Most likely cause: The new DCS uses a different PID algorithm form (ISA standard form vs. parallel/independent form vs. series/interacting form) than the old DCS, making the transferred tuning parameters incompatible.**

**Required Elements:**
- PID algorithm form mismatch identified: mandatory
- At least two algorithm forms named and distinguished: mandatory
- Parameter conversion concept: mandatory
- Unit/convention differences (PB vs Kp, repeats vs time): required for full credit

**Common Wrong Answers:**
- "Tuning is just wrong" — tuning was proven in the old system; the parameters are right for the wrong algorithm
- "Scan rate difference" — would affect derivative, but question says PI on secondary
- "Signal scaling changed" — instrumentation unchanged
- "Control direction reversed" — would cause runaway, not oscillation

**Scoring Rubric:**
- Full (100%): Algorithm form mismatch + forms named + conversion + units
- High (75%): Algorithm form issue + conversion concept
- Low (50%): Identifies DCS difference but not specific algorithm issue
- Zero: Blames tuning or instrumentation

**Reference:** Kuphaldt LIII Ch.28–29; ISA Practical Process Control; Vendor DCS Algorithm Documentation

---

## IUK-T3-XDOM-372
**Tier:** T3 · Specialist/PhD  
**Type:** XDOM  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A natural gas compressor station has a vibration monitoring system with proximity probes (eddy current type) measuring shaft radial vibration. After a bearing replacement, the vibration readings show a steady 2.5 mils peak-to-peak at 1× running speed (3600 RPM), which exceeds the 2.0 mil alarm setpoint. However, the compressor sounds smooth, bearing temperatures are normal, and the phase angle is stable. The maintenance team suspects the vibration system, not the compressor. What should be investigated?

**Correct Answer:**  
**Most likely cause: Mechanical or electrical runout on the new shaft or journal surface being detected by the proximity probe.**

Eddy current proximity probes measure the distance between the probe tip and the shaft surface. They respond to ANY change in that gap — including:

1. **Mechanical runout:** The shaft surface is not perfectly round (out-of-round from machining) or not perfectly concentric with the bearing bore (eccentricity). This creates a 1× vibration signal even if the shaft is running smoothly
2. **Electrical runout:** Variations in the shaft surface's electrical conductivity or magnetic permeability (from heat treatment variations, hard spots, metallurgical inclusions, or residual magnetism) cause the probe to read a varying gap even with a geometrically perfect shaft

**Required Elements:**
- Mechanical and/or electrical runout: mandatory
- Bearing replacement as trigger: mandatory
- Slow-roll compensation concept: mandatory
- Healthy compressor indicators cited: required for full credit

**Common Wrong Answers:**
- "Real vibration from misalignment" — normal temps and stable phase contradict
- "Bearing defect" — brand new bearing, normal temperatures
- "Probe gap incorrect" — would cause a DC offset, not a 1× AC signal
- "Imbalance" — possible but the coincidence with bearing replacement and healthy indicators point to runout

**Scoring Rubric:**
- Full (100%): Runout + bearing replacement trigger + slow-roll compensation + health indicators
- High (75%): Runout + compensation concept
- Low (50%): Identifies measurement artifact but not specific mechanism
- Zero: Recommends shutting down compressor for vibration

**Reference:** API 670 (Machinery Protection Systems); Kuphaldt LIII Ch.13; Bently Nevada Fundamentals of Vibration

---

## IUK-T3-XDOM-411
**Tier:** T3 · Specialist/PhD  
**Type:** XDOM  
**Weight:** 2.0×  
**Safety Gate:** NO  
**Adversarial:** NO  
**Source:** IUK_v3_IUK_v3_T3_diagnostic  
**Format:** full_iuk  
**Review status:** source_verified  

**Question:**  
A plant replaced a traditional 4–20 mA control system with a WirelessHART (IEC 62591) network for 30 temperature monitoring points on a reactor complex. The system worked well for 2 months. After a new metal-clad building was erected adjacent to the reactor complex, 8 of the 30 wireless transmitters began showing intermittent communication failures. What multi-domain factors should be investigated?

**Correct Answer:**  
This requires integrating wireless communication, RF propagation, civil/structural, and process instrumentation knowledge.

**Required Elements:**
- RF blockage from metal building: mandatory | Mesh network routing disruption: mandatory | 2.4 GHz propagation characteristics: mandatory | Repeater/gateway solutions: required for full credit

**Common Wrong Answers:**
- "Battery depletion" — 2 months is well within battery life | "Interference from building equipment" — the 8 specific devices affected correlate with building location | "Transmitter failures" — 8 simultaneous failures is implausible

**Reference:** IEC 62591 (WirelessHART); Kuphaldt LIII Ch.22; ISA-100.11a

---
