function solution(participant: any[], completion: any[]) {
  
  if (participant.length < 1 || 100000 < participant.length) throw new Error('1 <= participant <= 100000');
  if (participant.length - 1 !== completion.length) throw new Error('completion + 1 = participant');

  const pMap = new Map<string, number>();
  participant.forEach(p => {
    let value: number|undefined = pMap.get(p);
    pMap.set(p, value === undefined || value === null ? 1 : ++value);
  });

  completion.forEach(c => {
    let value: number|undefined = pMap.get(c);
    pMap.set(c, value === undefined || value === null ? 0 : --value);
  });

  let answer = '';
  for (const [k, v] of pMap) {
    if (v === 0)  continue;
    answer = k;
    break;
  }
  return answer;
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