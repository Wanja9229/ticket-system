'use client';

import { useState } from 'react';
import styles from './page.module.css';

export default function FunctionsExp() {
  const [code, setCode] = useState('// 티켓 가격 계산 함수를 만들어보세요!\n\n');
  const [output, setOutput] = useState('');
  const [showHint, setShowHint] = useState(false);
  const [showAnswer, setShowAnswer] = useState(false);

  const runCode = () => {
    try {
      const userFunction = new Function(`
        let result = '';
        ${code}
        
        // 함수 테스트 (사용자가 함수를 만들었는지 확인)
        if (typeof calculatePrice === 'function') {
          result += "✅ calculatePrice 함수가 정의되었습니다!\\n";
          
          try {
            const test1 = calculatePrice(100000, true);
            const test2 = calculatePrice(80000, false);
            result += "🎫 VIP 티켓 (10만원): " + test1 + "원\\n";
            result += "🎫 일반 티켓 (8만원): " + test2 + "원\\n";
          } catch (e) {
            result += "❌ 함수 실행 중 오류: " + e.message + "\\n";
          }
        } else {
          result += "❌ calculatePrice 함수를 찾을 수 없습니다.\\n";
        }
        
        return result;
      `);
      
      const result = userFunction();
      setOutput(result);
    } catch (error) {
      setOutput(`오류 발생: ${error.message}`);
    }
  };

  const checkAnswer = () => {
    const hasFunction = code.includes('function') || code.includes('=>');
    const hasCalculatePrice = code.includes('calculatePrice');
    const hasReturn = code.includes('return');
    const hasIfCondition = code.includes('if') || code.includes('?');

    if (hasFunction && hasCalculatePrice && hasReturn && hasIfCondition) {
      setOutput('🎉 완벽합니다! 함수와 조건문을 잘 활용하셨네요!');
    } else {
      let feedback = '❌ 아직 조건을 모두 만족하지 않았어요.\n\n';
      if (!hasFunction) feedback += '• function 키워드나 화살표 함수를 사용하세요\n';
      if (!hasCalculatePrice) feedback += '• 함수명이 calculatePrice인지 확인하세요\n';
      if (!hasReturn) feedback += '• return으로 값을 반환하세요\n';
      if (!hasIfCondition) feedback += '• if문이나 삼항연산자로 VIP 조건을 확인하세요\n';
      setOutput(feedback);
    }
  };

  return (
    <div className={`${styles.expContainer} functions-exp`}>
      <div className={styles.problemSection}>
        <h1>🎯 실습 2: 함수 만들기</h1>
        
        <div className={styles.mission}>
          <h2>📋 미션</h2>
          <p><strong>티켓 가격을 계산하는 함수를 만들어보세요!</strong></p>
          
          <div className={styles.requirements}>
            <h3>✅ 조건</h3>
            <ul>
              <li>함수명: <code>calculatePrice</code></li>
              <li>매개변수: <code>basePrice</code> (기본가격), <code>isVip</code> (VIP 여부)</li>
              <li>VIP이면 기본가격의 1.5배, 아니면 그대로 반환</li>
              <li><code>return</code>으로 계산된 가격 반환하기</li>
            </ul>
          </div>

          <div className={styles.example}>
            <h3>💡 예시</h3>
            <p>기본가격 100,000원이고 VIP이면 150,000원을 반환하는 함수</p>
          </div>
        </div>
      </div>

      <div className={styles.editorSection}>
        <h2>📝 코드 에디터</h2>
        <textarea
          value={code}
          onChange={(e) => setCode(e.target.value)}
          className={styles.codeEditor}
          placeholder="여기에 JavaScript 함수를 작성하세요..."
          rows={10}
        />
        
        <div className={styles.buttonGroup}>
          <button onClick={runCode} className={styles.runBtn}>
            🚀 함수 테스트
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
        <h2>📤 테스트 결과</h2>
        <div className={styles.output}>
          {output || '함수를 테스트하면 결과가 여기에 나타납니다.'}
        </div>
      </div>

      {showHint && (
        <div className={styles.hintSection}>
          <h2>💡 힌트</h2>
          <div className={styles.hintContent}>
            <p><strong>1단계:</strong> 함수 선언하기</p>
            <pre>{`function calculatePrice(basePrice, isVip) {
  // 여기에 로직 작성
}`}</pre>
            
            <p><strong>2단계:</strong> VIP 조건 확인하기</p>
            <pre>{`if (isVip) {
  // VIP이면 1.5배
} else {
  // 아니면 그대로
}`}</pre>
            
            <p><strong>3단계:</strong> 결과 반환하기</p>
            <pre>{`return 계산된_가격;`}</pre>
          </div>
        </div>
      )}

      {showAnswer && (
        <div className={styles.answerSection}>
          <h2>📖 정답 예시</h2>
          <div className={styles.answerTabs}>
            <h3>방법 1: function 키워드</h3>
            <pre className={styles.answerCode}>{`function calculatePrice(basePrice, isVip) {
  if (isVip) {
    return basePrice * 1.5;
  } else {
    return basePrice;
  }
}`}</pre>
            
            <h3>방법 2: 삼항 연산자</h3>
            <pre className={styles.answerCode}>{`function calculatePrice(basePrice, isVip) {
  return isVip ? basePrice * 1.5 : basePrice;
}`}</pre>
            
            <h3>방법 3: 화살표 함수</h3>
            <pre className={styles.answerCode}>{`const calculatePrice = (basePrice, isVip) => {
  return isVip ? basePrice * 1.5 : basePrice;
};`}</pre>
          </div>
        </div>
      )}

      <div className={styles.navigation}>
        <a href="/study/week1/exp/variables" className={`${styles.navBtn} ${styles.back}`}>
          ← 이전: 변수 실습
        </a>
        <a href="/study/week1/exp/arrays" className={`${styles.navBtn} ${styles.next}`}>
          다음: 배열 실습 →
        </a>
      </div>
    </div>
  );
}
