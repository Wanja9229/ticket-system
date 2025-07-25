'use client';

import BasicVariables from '@/study/week1/BasicVariables';
import DataTypes from '@/study/week1/DataTypes';
import Functions from '@/study/week1/Functions';
import Arrays from '@/study/week1/Arrays';
import Objects from '@/study/week1/Objects';
import TicketExample from '@/study/week1/TicketExample';
import styles from './page.module.css';

export default function StudyWeek1() {
  return (
    <div className={styles.studyContainer}>
      <header className={styles.studyHeader}>
        <h1>🚀 Week 1: JavaScript 핵심 기초</h1>
        <p className={styles.subtitle}>변수, 함수, 배열, 객체 마스터하기</p>
        <div className={styles.studyInfo}>
          <span>📚 학습시간: 4-6시간</span>
          <span>🎯 목표: JavaScript 기본 문법 완전 정복</span>
        </div>
      </header>

      <nav className={styles.studyNav}>
        <h2>📋 학습 목차</h2>
        <ul>
          <li><strong>Day 1</strong>: JavaScript 문법 기초</li>
          <li><strong>Day 2</strong>: 배열, 함수, 객체</li>
        </ul>
      </nav>

      <main className={styles.studyContent}>
        {/* 1. 기본 변수 */}
        <section className={styles.studySection}>
          <h2>1️⃣ 변수와 상수</h2>
          <p>JavaScript에서 데이터를 저장하는 방법을 배워봅시다.</p>
          <BasicVariables />
        </section>

        {/* 2. 데이터 타입 */}
        <section className={styles.studySection}>
          <h2>2️⃣ 데이터 타입</h2>
          <p>JavaScript의 다양한 데이터 타입들을 알아봅시다.</p>
          <DataTypes />
        </section>

        {/* 3. 함수 */}
        <section className={styles.studySection}>
          <h2>3️⃣ 함수</h2>
          <p>코드를 재사용하고 구조화하는 함수를 배워봅시다.</p>
          <Functions />
        </section>

        {/* 4. 배열 */}
        <section className={styles.studySection}>
          <h2>4️⃣ 배열</h2>
          <p>여러 데이터를 관리하는 배열과 유용한 메서드들을 알아봅시다.</p>
          <Arrays />
        </section>

        {/* 5. 객체 */}
        <section className={styles.studySection}>
          <h2>5️⃣ 객체</h2>
          <p>연관된 데이터를 그룹화하는 객체를 배워봅시다.</p>
          <Objects />
        </section>

        {/* 6. 종합 예제 */}
        <section className={styles.studySection}>
          <h2>🎫 종합 예제: 티켓 관리 시스템</h2>
          <p>배운 내용을 모두 활용한 실전 예제입니다.</p>
          <TicketExample />
        </section>

        {/* 7. 실습 섹션 */}
        <section className={styles.studySection}>
          <h2>📝 직접 연습하기</h2>
          <p>빈 코드 에디터에서 직접 타이핑하며 연습해보세요!</p>
          
          <div className="practice-grid">
            <div className="practice-card">
              <h3>📁 변수 실습</h3>
              <p>티켓 정보를 저장하는 변수 만들기</p>
              <a href="/study/week1/exp/variables" className="practice-btn">
                실습 시작 →
              </a>
            </div>
            
            <div className="practice-card">
              <h3>⚙️ 함수 실습</h3>
              <p>가격 계산 함수 만들기</p>
              <a href="/study/week1/exp/functions" className="practice-btn">
                실습 시작 →
              </a>
            </div>
            
            <div className="practice-card">
              <h3>🗋 배열 실습</h3>
              <p>좌석 목록 관리하기</p>
              <a href="#" className="practice-btn disabled">
                준비 중
              </a>
            </div>
            
            <div className="practice-card">
              <h3>🗺️ 객체 실습</h3>
              <p>티켓 정보 객체 만들기</p>
              <a href="#" className="practice-btn disabled">
                준비 중
              </a>
            </div>
          </div>
        </section>
      </main>

      <footer className={styles.studyFooter}>
        <div className={styles.nextStep}>
          <h3>🎯 다음 단계</h3>
          <p>Week 2에서는 React 컴포넌트와 상태 관리를 배워봅시다!</p>
          <a href="/study/week2" className={styles.nextLink}>Week 2로 이동 →</a>
        </div>
      </footer>
    </div>
  );
}
