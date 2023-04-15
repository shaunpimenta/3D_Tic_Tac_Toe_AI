using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class HitBox : MonoBehaviour {
    [SerializeField] private MeshRenderer _renderer;

    [SerializeField] private GameObject _x;
    [SerializeField] private GameObject _o;

    private int _type = -1;
    public int Type => _type;
        public int BoxNumber;

    private bool _markerPlaced = false;

    private void Start() {
        _renderer.enabled = false;
    }

    private void OnMouseOver() {
        if (GameManager.Instance.GameEnd || GameManager.Instance.DevMode || _markerPlaced) {
            return;
        }

        _renderer.enabled = true;
        Vector3 clickPos = Input.mousePosition;
    clickPos.z = Camera.main.nearClipPlane;
    Vector3 worldPos = Camera.main.ScreenToWorldPoint(clickPos);

    Collider collider = GetComponent<Collider>();
    if (collider.bounds.Contains(worldPos))
    {
        Debug.Log("Hitbox clicked at " + worldPos);
    }
    }

    private void OnMouseExit() {
        _renderer.enabled = false;
    }

    private void OnMouseUpAsButton() {
        if (GameManager.Instance.GameEnd || GameManager.Instance.DevMode || _markerPlaced) {
            return;
        }


        _renderer.enabled = false;
        _markerPlaced = true;

        _type = GameManager.Instance.Turn;
        var markerToSpawn = _type == 0 ? _x : _o;
        Instantiate(markerToSpawn, transform);
        Debug.Log(transform.position);

        GameManager.Instance.MoveMade();
                Debug.Log("Box " + BoxNumber + " clicked");


        // Debug.Log("compile");
    }
}