function solution(participant: any[], completion: any[]) {
  
  if (participant.length < 1 || 100000 < participant.length) throw new Error('1 <= participant <= 100000');
  if (participant.length - 1 !== completion.length) throw new Error('completion + 1 = participant');

  const pMap = new Map<string, number>();
  for (let i = 0, len = participant.length; i < len; i++) {
    const p: string = participant[i],
        c: string = completion[i];
    pMap.set(p, (pMap.get(p) || 0) + 1);
    pMap.set(c, (pMap.get(c) || 0) - 1);
  }

  for (const [k, v] of pMap) {
    if (v > 0)  return k;
  }

  return null;
}

// "leo"
let participant: string[] = ["leo", "kiki", "eden"]
let completion: string[] = ["eden", "kiki"]
console.log(solution(participant, completion))

// "vinko"
participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
completion = ["josipa", "filipa", "marina", "nikola"]
console.log(solution(participant, completion))

// "mislav"
participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]
console.log(solution(participant, completion))