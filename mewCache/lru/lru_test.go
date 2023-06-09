package lru

import (
	"reflect"
	"testing"
)

type String string

func (s String) Len() int {
	return len(s)
}

var (
	cacheKey1 = "cacheKey1"
	cacheKey2 = "cachekey2"
	cacheKey3 = "cachekey3"
	cacheVal1 = "111"
	cacheVal2 = "222"
	cacheVal3 = "333"
)

func TestAdd(t *testing.T) {
	lru := New(int64(0), nil)
	lru.Add(cacheKey1, String(cacheVal1))
	lru.Add(cacheKey1, String(cacheVal2))

	if lru.nbytes != int64(len(cacheKey1)+len(cacheVal2)) {
		t.Fatal("expected 6 but got", lru.nbytes)
	}
}

func TestGet(t *testing.T) {

	lru := New(int64(0), nil)
	lru.Add(cacheKey1, String(cacheVal1))
	if v, ok := lru.Get(cacheKey1); !ok || string(v.(String)) != cacheVal1 {
		t.Fatalf("cache hit cacheKey failed")
	}

	if _, ok := lru.Get(cacheKey2); ok {
		t.Fatalf("cache miss cacheKey2 failed")
	}
}

func TestOnEvicted(t *testing.T) {
	keys := make([]string, 0)
	callback := func(key string, value Value) {
		keys = append(keys, key)
	}

	lru := New(int64(12), callback)
	lru.Add(cacheKey1, String(cacheVal1))
	lru.Add(cacheKey2, String(cacheVal2))
	lru.Add(cacheKey3, String(cacheVal3))

	expect := []string{cacheKey1, cacheKey2}
	if !reflect.DeepEqual(expect, keys) {
		t.Fatalf("Call OnEvicted failed, expect keys equals to %s", expect)
	}
}

func TestRemoveOldest(t *testing.T) {
	cap := len(cacheKey1 + cacheVal1 + cacheKey2 + cacheVal2)
	lru := New(int64(cap), nil)
	lru.Add(cacheKey1, String(cacheVal1))
	lru.Add(cacheKey2, String(cacheVal2))
	lru.Add(cacheKey3, String(cacheVal3))

	if _, ok := lru.Get(cacheKey1); ok || lru.Len() != 2 {
		t.Errorf("Removeoldest cacheKey failed: %v, len: %d", ok, lru.Len())
	}
}
