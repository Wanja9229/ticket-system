'use client';

import { useState } from 'react';

export default function Objects() {
  const [output, setOutput] = useState('');

  const runExample = () => {
    let result = '';

    // 1. 객체 생성과 기본 접근
    result += `1. 객체 생성과 기본 접근:\n`;
    const ticket = {
      id: 'T001',
      eventName: '2024 K-POP 콘서트',
      seat: 'A1',
      price: 150000,
      isVip: true,
      purchaseDate: '2024-07-25'
    };

    result += `   티켓 ID: ${ticket.id}\n`;
    result += `   이벤트명: ${ticket.eventName}\n`;
    result += `   좌석: ${ticket.seat}\n`;
    result += `   가격: ${ticket.price.toLocaleString()}원\n`;
    result += `   VIP 여부: ${ticket.isVip}\n\n`;

    // 2. 객체 속성 추가/수정/삭제
    result += `2. 객체 속성 조작:\n`;
    const customer = {
      name: '김철수',
      email: 'kim@email.com'
    };

    // 속성 추가
    customer.phone = '010-1234-5678';
    customer['address'] = '서울시 강남구';

    // 속성 수정
    customer.name = '김철수님';

    result += `   고객명: ${customer.name}\n`;
    result += `   이메일: ${customer.email}\n`;
    result += `   전화번호: ${customer.phone}\n`;
    result += `   주소: ${customer.address}\n`;

    // 속성 삭제
    delete customer.address;
    result += `   주소 삭제 후: ${customer.address || '없음'}\n\n`;

    setOutput(result);
  };

  return (
    <div className="example-container">
      <div className="example-info">
        <h3>🎯 학습 목표</h3>
        <ul>
          <li><strong>객체 기초</strong>: 생성, 접근, 수정</li>
          <li><strong>메서드</strong>: 객체 안의 함수 정의</li>
          <li><strong>구조 분해</strong>: 객체에서 값 추출하기</li>
          <li><strong>내장 메서드</strong>: Object.keys, values, entries</li>
          <li><strong>객체 복사</strong>: 얕은 복사와 깊은 복사</li>
          <li><strong>실전 활용</strong>: 티켓 시스템 객체 설계</li>
        </ul>
      </div>

      <div className="code-section">
        <h3>📝 코드 예제</h3>
        <pre className="code-block">{`// 1. 객체 생성 (3가지 방법)
const ticket1 = {            // 객체 리터럴 (가장 일반적)
  seat: 'A1',
  price: 150000
};

const ticket2 = new Object(); // 생성자 함수
ticket2.seat = 'A2';
ticket2.price = 150000;

// 2. 속성 접근 (2가지 방법)
console.log(ticket.seat);    // 점 표기법 (일반적)
console.log(ticket['seat']); // 대괄호 표기법 (동적 접근)

// 3. 메서드 정의
const calculator = {
  price: 100000,
  discount: 0.1,
  
  getFinalPrice() {  // ES6 단축 문법
    return this.price * (1 - this.discount);
  }
};

// 4. 구조 분해 할당
const event = { name: '콘서트', date: '2024-08-15', price: 150000 };
const { name, date, price } = event;  // 한 번에 변수 생성

// 5. 객체 메서드들
Object.keys(event);      // ['name', 'date', 'price']
Object.values(event);    // ['콘서트', '2024-08-15', 150000]
Object.entries(event);   // [['name', '콘서트'], ...]

// 6. 객체 복사
const copy1 = { ...event };        // 얕은 복사 (스프레드)
const copy2 = Object.assign({}, event); // 얕은 복사 (assign)`}</pre>
      </div>

      <div className="interactive-section">
        <button onClick={runExample} className="run-button">
          🚀 예제 실행하기
        </button>
        
        {output && (
          <div className="output-section">
            <h4>📤 실행 결과:</h4>
            <pre className="output">{output}</pre>
          </div>
        )}
      </div>

      <div className="tips-section">
        <h3>💡 실무 팁</h3>
        <div className="tip">
          <strong>객체 속성명은 일관성 있게!</strong>
          <p>✅ camelCase: <code>firstName, eventDate, ticketPrice</code><br/>
             ❌ 섞어쓰기: <code>first_name, eventDate, ticket-price</code></p>
        </div>
        <div className="tip">
          <strong>구조 분해 할당을 적극 활용하기!</strong>
          <p>❌ <code>const name = user.name; const email = user.email;</code><br/>
             ✅ <code>const &#123;name, email&#125; = user;</code></p>
        </div>
        <div className="tip">
          <strong>객체 복사 시 중첩 객체 주의하기!</strong>
          <p>얕은 복사: <code>&#123;...obj&#125;</code> (1단계만 복사)<br/>
             깊은 복사: <code>JSON.parse(JSON.stringify(obj))</code></p>
        </div>
      </div>

      <style>{`
        .example-container {
          border: 1px solid #e1e5e9;
          border-radius: 8px;
          padding: 20px;
          margin: 20px 0;
        }

        .example-info ul {
          background: #f8f9fa;
          padding: 15px;
          border-radius: 6px;
          margin: 10px 0;
          columns: 2;
          column-gap: 30px;
        }

        .example-info li {
          margin: 8px 0;
          break-inside: avoid;
        }

        .code-section {
          margin: 20px 0;
        }

        .code-block {
          background: #2d3748;
          color: #e2e8f0;
          padding: 20px;
          border-radius: 6px;
          overflow-x: auto;
          font-family: 'Fira Code', monospace;
          line-height: 1.5;
          font-size: 14px;
        }

        .interactive-section {
          margin: 20px 0;
          text-align: center;
        }

        .run-button {
          background: #e53e3e;
          color: white;
          border: none;
          padding: 12px 24px;
          border-radius: 6px;
          font-size: 16px;
          cursor: pointer;
          transition: background 0.2s;
        }

        .run-button:hover {
          background: #c53030;
        }

        .output-section {
          margin-top: 20px;
          text-align: left;
        }

        .output {
          background: #1a202c;
          color: #68d391;
          padding: 15px;
          border-radius: 6px;
          border-left: 4px solid #e53e3e;
          font-family: monospace;
          white-space: pre-wrap;
          max-height: 400px;
          overflow-y: auto;
        }

        .tips-section {
          margin-top: 30px;
          background: #fffaf0;
          padding: 20px;
          border-radius: 6px;
          border-left: 4px solid #ed8936;
        }

        .tip {
          margin: 15px 0;
          padding: 10px;
          background: white;
          border-radius: 4px;
        }

        .tip strong {
          color: #c05621;
        }

        code {
          background: #edf2f7;
          padding: 2px 6px;
          border-radius: 3px;
          font-family: monospace;
          color: #2d3748;
        }

        @media (max-width: 768px) {
          .example-info ul {
            columns: 1;
          }
        }
      `}</style>
    </div>
  );
}
