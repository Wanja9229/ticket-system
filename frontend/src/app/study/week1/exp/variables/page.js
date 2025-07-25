'use client';

import { useState } from 'react';
import styles from './page.module.css';

export default function VariablesExp() {
  const [code, setCode] = useState('// 여기에 코드를 작성하세요!\n\n');
  const [output, setOutput] = useState('');
  const [showHint, setShowHint] = useState(false);
  const [showAnswer, setShowAnswer] = useState(false);

  const runCode = () => {
    try {
      // 사용자 코드 실행을 위한 함수 생성
      const userFunction = new Function(`
        let result = '';
        ${code}
        return result;
      `);
      
      const result = userFunction();
      setOutput(result || '코드가 실행되었습니다!');
    } catch (error) {
      setOutput(`오류 발생: ${error.message}`);
    }
  };

  const checkAnswer = () => {
    const hasLet = code.includes('let') || code.includes('const');
    const hasTicketInfo = code.includes('티켓') || code.includes('ticket') || code.includes('콘서트') || code.includes('concert');
    const hasOutput = code.includes('console.log') || code.includes('result +=');

    if (hasLet && hasTicketInfo && hasOutput) {
      setOutput('🎉 정답입니다! 변수를 잘 활용하셨네요!');
    } else {
      setOutput('❌ 아직 조건을 모두 만족하지 않았어요. 힌트를 확인해보세요!');
    }
  };

  return (
    <div className={`${styles.expContainer} variables-exp`}>
      <div className={styles.problemSection}>
        <h1>🎯 실습 1: 변수와 상수 연습</h1>
        
        <div className={styles.mission}>
          <h2>📋 미션</h2>
          <p><strong>티켓 정보를 저장하는 변수들을 만들어보세요!</strong></p>
          
          <div className={styles.requirements}>
            <h3>✅ 조건</h3>
            <ul>
              <li><code>let</code> 또는 <code>const</code>를 사용해서 변수 3개 이상 만들기</li>
              <li>티켓 관련 정보 저장하기 (이름, 가격, 좌석번호 등)</li>
              <li><code>console.log()</code> 또는 <code>result +=</code>로 결과 출력하기</li>
            </ul>
          </div>

          <div className={styles.example}>
            <h3>💡 예시</h3>
            <p>콘서트 티켓의 이름, 가격, 좌석번호를 변수에 저장하고 출력해보세요!</p>
          </div>
        </div>
      </div>

      <div className={styles.editorSection}>
        <h2>📝 코드 에디터</h2>
        <textarea
          value={code}
          onChange={(e) => setCode(e.target.value)}
          className={styles.codeEditor}
          placeholder="여기에 JavaScript 코드를 작성하세요..."
          rows={12}
        />
        
        <div className={styles.buttonGroup}>
          <button onClick={runCode} className={styles.runBtn}>
            🚀 코드 실행
          </button>
          <button onClick={checkAnswer} className={styles.checkBtn}>
            ✅ 정답 확인
          </button>
          <button onClick={() => setShowHint(!showHint)} className={styles.hintBtn}>
            💡 힌트 {showHint ? '숨기기' : '보기'}
          </button>
          <button onClick={() => setShowAnswer(!showAnswer)} className={styles.answerBtn}>
            📖 정답 {showAnswer ? '숨기기' : '보기'}
          </button>
        </div>
      </div>

      <div className={styles.resultSection}>
        <h2>📤 실행 결과</h2>
        <div className={styles.output}>
          {output || '코드를 실행하면 결과가 여기에 나타납니다.'}
        </div>
      </div>

      {showHint && (
        <div className={styles.hintSection}>
          <h2>💡 힌트</h2>
          <div className={styles.hintContent}>
            <p><strong>1단계:</strong> <code>const</code>를 사용해서 콘서트 이름을 저장해보세요</p>
            <pre>{`const concertName = "IU 콘서트";`}</pre>
            
            <p><strong>2단계:</strong> <code>let</code>을 사용해서 가격과 좌석을 저장해보세요</p>
            <pre>{`let price = 150000;
let seat = "A1";`}</pre>
            
            <p><strong>3단계:</strong> 결과를 출력해보세요</p>
            <pre>{`console.log("콘서트:", concertName);
console.log("가격:", price + "원");
console.log("좌석:", seat);`}</pre>
          </div>
        </div>
      )}

      {showAnswer && (
        <div className={styles.answerSection}>
          <h2>📖 정답 예시</h2>
          <pre className={styles.answerCode}>{`// 티켓 정보 변수 생성
const eventName = "IU 2024 콘서트";
const venue = "잠실실내체육관";
let ticketPrice = 150000;
let seatNumber = "A1";
let isVip = true;

// 정보 출력
console.log("🎫 티켓 정보");
console.log("이벤트:", eventName);
console.log("장소:", venue);
console.log("가격:", ticketPrice.toLocaleString() + "원");
console.log("좌석:", seatNumber);
console.log("VIP 여부:", isVip ? "VIP석" : "일반석");

// 또는 result 변수 사용
result += "🎫 티켓 정보\\n";
result += "이벤트: " + eventName + "\\n";
result += "가격: " + ticketPrice.toLocaleString() + "원\\n";
result += "좌석: " + seatNumber + "\\n";`}</pre>
        </div>
      )}

      <div className={styles.navigation}>
        <a href="/study/week1" className={`${styles.navBtn} ${styles.back}`}>
          ← Week 1 메인으로
        </a>
        <a href="/study/week1/exp/functions" className={`${styles.navBtn} ${styles.next}`}>
          다음: 함수 실습 →
        </a>
      </div>
    </div>
  );
}
